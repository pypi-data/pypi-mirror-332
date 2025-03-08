from . import *


def heatmap(
    m: torch.Tensor,
    cmap: str = "Reds",
    label_x: str = "",
    label_y: str = "",
    title: str = "",
):
    if m.ndim == 4:
        nrow, ncol = m.size()[:2]
    else:
        nrow, ncol = 1, 1
    fig, axes = plt.subplots(nrow, ncol, squeeze=False)
    for i in range(nrow):
        for j in range(ncol):
            ax = axes[i, j]
            if m.ndim == 4:
                ax.imshow(m[i, j].detach().cpu().numpy(), cmap=cmap)
            else:
                ax.imshow(m.detach().cpu().numpy(), cmap=cmap)
            ax.set_xlabel(label_x)
            ax.set_ylabel(label_y)
            ax.set_title(title)
    fig.colorbar(ax.get_images()[0], ax=axes, orientation="vertical")


def kernel_regression(
    y_hat: torch.Tensor,
    y_true: torch.Tensor,
    x_test: torch.Tensor,
    y_train: torch.Tensor,
    x_train: torch.Tensor,
):
    plt.plot(x_test, y_true, label="True")
    plt.plot(x_test, y_hat, label="Predict", color="blue")
    plt.scatter(x_train, y_train, label="Train", color="red")
    plt.legend()
