from typing import List

import torch
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import gridspec


def set_axs_attribute(axs):
    for ax in list(axs.flatten()):
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)


def fmt(x, pos):
    """
    Format color bar labels to show scientific label
    """
    a, b = '{:.1e}'.format(x).split('e')
    b = int(b)
    # return r'${} \ e^{{{}}}$'.format(a, b)
    if pos % 3 == 0 and b != 0:
        return r'${} \ e^{{{}}}$'.format(a, b)
    else:
        return r'${}$'.format(a)


def fill_subplots(img: torch.Tensor, axs, img_name='', fontsize=6, cmap='gray',
                  fig: plt.Figure=None, show_colorbar=False, normalize=True):
    if cmap == 'gray' and normalize:  # map image to 0...1
        img = (img - img.min())/(img.max() - img.min())
    elif cmap is None:  # cliping data to 0...255
        img[img < 0] = 0
        img[img > 255] = 255

    shape = img.shape[-3:]
    img0 = axs[0].imshow(img[0, :, int(shape[0] / 2), :, :].permute(dims=(1, 2, 0)).squeeze().numpy(), cmap=cmap)
    axs[0].set_title(f'{img_name} central slice \n in sagittal view', fontsize=fontsize)
    img1 = axs[1].imshow(img[0, :, :, int(shape[1] / 2), :].permute(dims=(1, 2, 0)).squeeze().numpy(), cmap=cmap)
    axs[1].set_title(f'{img_name} central slice \n in coronal view', fontsize=fontsize)
    img2 = axs[2].imshow(img[0, :, :, :, int(shape[0] / 2)].permute(dims=(1, 2, 0)).squeeze().numpy(), cmap=cmap)
    axs[2].set_title(f'{img_name} central slice \n in axial view', fontsize=fontsize)
    if show_colorbar and fig is not None:
        set_colorbar(img0, axs[0], fig, fontsize)
        set_colorbar(img1, axs[1], fig, fontsize)
        set_colorbar(img2, axs[2], fig, fontsize)


def set_colorbar(img, ax, fig, fontsize):
    cb = fig.colorbar(img, ax=ax, orientation='horizontal', format=ticker.FuncFormatter(fmt), pad=0.2)
    cb.ax.tick_params(labelsize=fontsize)


def init_figure(ncol, nrow) -> (List[plt.Axes], plt.Figure):
    fig = plt.figure(figsize=(2 * ncol + 1, 2 * nrow + 1))  # , constrained_layout=True)
    spec = gridspec.GridSpec(nrow, ncol, figure=fig,
                             wspace=0.2, hspace=0.2,
                             top=1. - 0.5 / (nrow + 1), bottom=0.5 / (nrow + 1),
                             left=0.5 / (ncol + 1), right=1 - 0.5 / (ncol + 1))
    # spec = fig.add_gridspec(ncols=3, nrows=5, width_ratios=[0.5]*3, height_ratios=[1]*5)
    # spec.update(wspace=0.025, hspace=0.05)
    axs = []
    for i in range(nrow):
        tmp = []
        for j in range(ncol):
            ax = fig.add_subplot(spec[i, j])
            tmp.append(ax)
        axs.append(tmp)
    axs = np.asarray(axs)
    return axs, fig
