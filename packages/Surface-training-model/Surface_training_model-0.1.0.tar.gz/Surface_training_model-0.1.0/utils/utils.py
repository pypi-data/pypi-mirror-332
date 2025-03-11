import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np
from scipy.ndimage import binary_dilation

def plot_img_and_mask(img, mask):
    classes = mask.max() + 1
    fig, ax = plt.subplots(1, classes + 1)
    ax[0].set_title('Input image')
    ax[0].imshow(img)
    for i in range(classes):
        ax[i + 1].set_title(f'Mask (class {i + 1})')
        ax[i + 1].imshow(mask == i)
    plt.xticks([]), plt.yticks([])
    plt.show()

def back_img(img: Image.Image, mask: np.ndarray, output_filename: str, alpha: float = 0.5):
    """
    保存带有透明红色掩码叠加的图像
    :param img: 输入图像 (PIL Image)
    :param mask: 预测掩码 (NumPy array)
    :param output_filename: 保存的输出文件名
    :param alpha: 红色掩码的透明度 (0.0 全透明, 1.0 不透明)
    """
    # 创建红色掩码
    red_mask = np.zeros((mask.shape[0], mask.shape[1], 3), dtype=np.uint8)
    red_mask[mask == 1] = [255, 0, 0]  # 掩码部分显示为红色
    
    # 将输入图像转换为 NumPy 格式
    img_np = np.array(img.convert("RGB"))
    
    # 将红色掩码叠加到输入图像上，并引入透明度
    overlay = np.clip((1 - alpha) * img_np + alpha * red_mask, 0, 255).astype(np.uint8)
    
    # 将叠加后的图像转换回 PIL Image 格式并保存
    overlay_img = Image.fromarray(overlay)
    overlay_img.save(output_filename)
    print(f"保存了带透明红色标注的图像到 {output_filename}")


