import torch
import torch.nn.functional as F
from tqdm import tqdm

from Surface_training_model.utils.dice_score import multiclass_dice_coeff, dice_coeff


@torch.inference_mode()
def evaluate(net, dataloader, device, amp):
    net.eval()
    num_val_batches = len(dataloader)
    dice_score = 0

    # iterate over the validation set
    with torch.autocast(device.type if device.type != 'mps' else 'cpu', enabled=amp):
        for batch in tqdm(dataloader, total=num_val_batches, desc='Validation round', unit='batch', leave=False):
            image, mask_true = batch['image'], batch['mask']

            # move images and labels to correct device and type
            image = image.to(device=device, dtype=torch.float32, memory_format=torch.channels_last)
            mask_true = mask_true.to(device=device, dtype=torch.long)

            # predict the mask
            mask_pred = net(image)

            if net.n_classes == 1:
                assert mask_true.min() >= 0 and mask_true.max() <= 1, 'True mask indices should be in [0, 1]'
                mask_pred = (F.sigmoid(mask_pred) > 0.5).float()
                #调整尺寸以匹配
                mask_pred = mask_pred.squeeze(1)
                mask_true = mask_true.float()
                # compute the Dice score
                dice_score += dice_coeff(mask_pred, mask_true, reduce_batch_first=False)
            else:
                assert mask_true.min() >= 0 and mask_true.max() < net.n_classes, 'True mask indices should be in [0, n_classes['
                # convert to one-hot format
                mask_true = F.one_hot(mask_true, net.n_classes).permute(0, 3, 1, 2).float()
                mask_pred = F.one_hot(mask_pred.argmax(dim=1), net.n_classes).permute(0, 3, 1, 2).float()
                # compute the Dice score, ignoring background
                dice_score += multiclass_dice_coeff(mask_pred[:, 1:], mask_true[:, 1:], reduce_batch_first=False)

    net.train()
    return dice_score / max(num_val_batches, 1)

# import torch
# import torch.nn.functional as F
# from tqdm import tqdm

# from utils.dice_score import multiclass_dice_coeff, dice_coeff

# def f_score(input: torch.Tensor, target: torch.Tensor, beta: float = 1, epsilon: float = 1e-6):
#     assert input.size() == target.size()
#     assert input.dim() == 3 or input.dim() == 4

#     sum_dim = (-1, -2) if input.dim() == 3 else (-1, -2, -3)

#     inter = (input * target).sum(dim=sum_dim)
#     precision = inter / (input.sum(dim=sum_dim) + epsilon)
#     recall = inter / (target.sum(dim=sum_dim) + epsilon)

#     f_score = (1 + beta**2) * (precision * recall) / (beta**2 * precision + recall + epsilon)
#     return f_score.mean()

# def miou(input: torch.Tensor, target: torch.Tensor, epsilon: float = 1e-6):
#     assert input.size() == target.size()
#     assert input.dim() == 3 or input.dim() == 4

#     sum_dim = (-1, -2) if input.dim() == 3 else (-1, -2, -3)

#     inter = (input * target).sum(dim=sum_dim)
#     union = input.sum(dim=sum_dim) + target.sum(dim=sum_dim) - inter

#     miou = (inter + epsilon) / (union + epsilon)
#     return miou.mean()

# @torch.inference_mode()
# def evaluate(net, dataloader, device, amp):
#     net.eval()
#     num_val_batches = len(dataloader)
#     dice_score = 0
#     f1_score_total = 0
#     miou_total = 0

#     # iterate over the validation set
#     with torch.autocast(device.type if device.type != 'mps' else 'cpu', enabled=amp):
#         for batch in tqdm(dataloader, total=num_val_batches, desc='Validation round', unit='batch', leave=False):
#             image, mask_true = batch['image'], batch['mask']

#             # move images and labels to correct device and type
#             image = image.to(device=device, dtype=torch.float32, memory_format=torch.channels_last)
#             mask_true = mask_true.to(device=device, dtype=torch.long)

#             # predict the mask
#             mask_pred = net(image)

#             if net.n_classes == 1:
#                 assert mask_true.min() >= 0 and mask_true.max() <= 1, 'True mask indices should be in [0, 1]'
#                 mask_pred = (F.sigmoid(mask_pred) > 0.5).float()
#                 # compute the Dice score
#                 dice_score += dice_coeff(mask_pred, mask_true, reduce_batch_first=False)
#                 # compute F1-score and mIoU
#                 f1_score_total += f_score(mask_pred, mask_true)
#                 miou_total += miou(mask_pred, mask_true)
#             else:
#                 assert mask_true.min() >= 0 and mask_true.max() < net.n_classes, 'True mask indices should be in [0, n_classes['
#                 # convert to one-hot format
#                 mask_true = F.one_hot(mask_true, net.n_classes).permute(0, 3, 1, 2).float()
#                 mask_pred = F.one_hot(mask_pred.argmax(dim=1), net.n_classes).permute(0, 3, 1, 2).float()
#                 # compute the Dice score, ignoring background
#                 dice_score += multiclass_dice_coeff(mask_pred[:, 1:], mask_true[:, 1:], reduce_batch_first=False)
#                 # compute F1-score and mIoU
#                 f1_score_total += f_score(mask_pred[:, 1:], mask_true[:, 1:])
#                 miou_total += miou(mask_pred[:, 1:], mask_true[:, 1:])

#     net.train()
#     avg_dice_score = dice_score / max(num_val_batches, 1)
#     avg_f1_score = f1_score_total / max(num_val_batches, 1)
#     avg_miou = miou_total / max(num_val_batches, 1)
    
#     return avg_dice_score, avg_f1_score, avg_miou