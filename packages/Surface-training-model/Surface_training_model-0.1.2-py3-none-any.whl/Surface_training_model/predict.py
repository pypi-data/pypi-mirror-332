import argparse
import logging
import os

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms

from utils.data_loading import BasicDataset
from unet import U_Net
from unet import UNet
from unet import AttU_Net
from unet import HighResolutionNet
from utils.utils import plot_img_and_mask
from utils.utils import back_img
import pdb

def predict_img(net,
                full_img,
                device,
                scale_factor=1,
                out_threshold=0.5):
    net.eval()
    img = torch.from_numpy(BasicDataset.preprocess(None, full_img, scale_factor, is_mask=False))
    img = img.unsqueeze(0)
    img = img.to(device=device, dtype=torch.float32)

    with torch.no_grad():
        output = net(img).cpu()
        output = F.interpolate(output, (full_img.size[1], full_img.size[0]), mode='bilinear')
        if net.n_classes > 1:
            mask = output.argmax(dim=1)
        else:
            mask = torch.sigmoid(output) > out_threshold

    return mask[0].long().squeeze().numpy()


def get_args():
    parser = argparse.ArgumentParser(description='Predict masks from input images')
    parser.add_argument('--model', '-m', default='/media/gml/data/fdf/learning/Pytorch-UNet/checkpoints/HRnet_full_bind/checkpoint_epoch10.pth', metavar='FILE',
                        help='Specify the file in which the model is stored')
    parser.add_argument('--input_txt', '-it', metavar='INPUT_TXT', help='Path to the txt file containing input filenames', required=True)
    parser.add_argument('--input_dir', '-id', metavar='INPUT_DIR', help='Directory of input tif files', required=True)
    parser.add_argument('--output_dir', '-od', metavar='OUTPUT_DIR', help='Directory to save output png files', required=True)
    parser.add_argument('--viz', '-v', action='store_true',
                        help='Visualize the images as they are processed')
    parser.add_argument('--no-save', '-n', action='store_true', help='Do not save the output masks')
    parser.add_argument('--mask-threshold', '-t', type=float, default=0.5,
                        help='Minimum probability value to consider a mask pixel white')
    parser.add_argument('--scale', '-s', type=float, default=0.5,
                        help='Scale factor for the input images')
    parser.add_argument('--bilinear', action='store_true', default=False, help='Use bilinear upsampling')
    parser.add_argument('--classes', '-c', type=int, default=2, help='Number of classes')
    
    return parser.parse_args()


def load_file_list(txt_file):
    with open(txt_file, 'r') as f:
        file_list = f.read().splitlines()
    return file_list


def mask_to_image(mask: np.ndarray, mask_values):
    if isinstance(mask_values[0], list):
        out = np.zeros((mask.shape[-2], mask.shape[-1], len(mask_values[0])), dtype=np.uint8)
    elif mask_values == [0, 1]:
        out = np.zeros((mask.shape[-2], mask.shape[-1]), dtype=bool)
    else:
        out = np.zeros((mask.shape[-2], mask.shape[-1]), dtype=np.uint8)

    if mask.ndim == 3:
        mask = np.argmax(mask, axis=0)

    for i, v in enumerate(mask_values):
        out[mask == i] = v

    return Image.fromarray(out)


if __name__ == '__main__':
    args = get_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    file_list = load_file_list(args.input_txt)
    in_files = []
    out_files = []

    for tif_file in os.listdir(args.input_dir):
        if tif_file.endswith('.tif'):
            in_files.append(os.path.join(args.input_dir, tif_file))
            out_files.append(os.path.join(args.output_dir, tif_file.replace('.tif', '.png')))
    net = HighResolutionNet(n_channels=1, n_classes=args.classes, bilinear=args.bilinear)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    logging.info(f'Loading model {args.model}')
    logging.info(f'Using device {device}')

    net.to(device=device)
    state_dict = torch.load(args.model, map_location=device, weights_only=True)
    mask_values = state_dict.pop('mask_values', [0, 1])
    net.load_state_dict(state_dict)

    logging.info('Model loaded!')

    for i, filename in enumerate(in_files):
        if os.path.exists(filename):
            logging.info(f'Predicting image {filename} ...')
            img = Image.open(filename)

            try:
                mask = predict_img(net=net,
                                full_img=img,
                                scale_factor=args.scale,
                                out_threshold=args.mask_threshold,
                                device=device)

                if not args.no_save:
                    out_filename = out_files[i]
                    os.makedirs(os.path.dirname(out_filename), exist_ok=True)
                    result = mask_to_image(mask, mask_values)
                    result.save(out_filename)
                    logging.info(f'Mask saved to {out_filename}')
                    # 保存带加粗红色预测标注的图像
                    overlay_filename = os.path.splitext(out_filename)[0] + "_overlay.png"
                    back_img(img, mask, overlay_filename)
                    logging.info(f'Red overlay image with thick mask saved to {overlay_filename}')

                if args.viz:
                    logging.info(f'Visualizing results for image {filename}, close to continue...')
                    back_img(img, mask)
            except torch.cuda.OutOfMemoryError:
                logging.error(f'CUDA out of memory while processing {filename}. Skipping this file.')
                torch.cuda.empty_cache()
        else:
            logging.warning(f'File {filename} does not exist')