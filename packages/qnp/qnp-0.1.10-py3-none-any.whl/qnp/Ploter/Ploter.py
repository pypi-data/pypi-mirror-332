import matplotlib.pyplot as plt


def twin_plot_decorator(
    title="",
    x_label="",
    ax1_y_label="",
    ax2_y_label="",
    ax1_color="tab:red",
    ax2_color="tab:blue",
):
    def decorator(ploter_function):
        def wrapper():
            fig, ax1 = plt.subplots()
            plt.title(title)

            ax1.set_xlabel(x_label)
            ax1.set_ylabel(ax1_y_label, color=ax1_color)
            ax1.tick_params(axis="y", labelcolor=ax1_color)

            # instantiate a second Axes that shares the same x-axis
            ax2 = ax1.twinx()

            ax2.set_ylabel(ax2_y_label, color=ax2_color)
            ax2.tick_params(axis="y", labelcolor=ax2_color)

            fig.tight_layout()

            ploter_function(ax1, ax2)

            ax1.legend()
            ax2.legend()

        wrapper()

    return decorator
