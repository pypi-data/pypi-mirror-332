import matplotlib.pyplot as plt
import numpy as np


class BarPlot:
    """
    A class for creating bar plots with customizable properties.

    The BarPlot class provides a simplified interface for creating bar plots
    with customizable axis limits and bar properties such as width and line weight.

    Parameters
    ----------
    x : array-like
        The x-coordinates of the bars.
    y : array-like
        The heights of the bars.
    lowerlimx : float, optional
        Lower limit of the x-axis. Default is None (auto-determined as 90% of minimum x).
    lowerlimy : float, optional
        Lower limit of the y-axis. Default is None (auto-determined as 90% of minimum y).
    upperlimx : float, optional
        Upper limit of the x-axis. Default is None (auto-determined as 110% of maximum x).
    upperlimy : float, optional
        Upper limit of the y-axis. Default is None (auto-determined as 110% of maximum y).
    wd : float, optional
        The width of the bars. Default is None (uses default width of 1).
    lw : float, optional
        The linewidth of the bar edges. Default is None (uses default linewidth of 1).

    Examples
    --------
    >>> # Basic bar plot
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [10, 15, 7, 12, 9]
    >>> bar = BarPlot(x, y)
    >>> bar.plot()

    >>> # Bar plot with custom width and axis limits
    >>> bar = BarPlot(x, y, lowerlimx=0, upperlimx=6, wd=0.5)
    >>> bar.plot()

    >>> # Bar plot with custom linewidth
    >>> bar = BarPlot(x, y, lw=2)
    >>> bar.plot()
    """

    def __init__(
        self,
        x,
        y,
        lowerlimx=None,
        lowerlimy=None,
        upperlimx=None,
        upperlimy=None,
        wd=None,
        lw=None,
    ):
        self.x = x
        self.y = y
        self.lowerlimx = lowerlimx
        self.lowerlimy = lowerlimy
        self.upperlimx = upperlimx
        self.upperlimy = upperlimy

        # Set default axis limits if not provided
        # Lower limit for x-axis/y-axis
        if self.lowerlimx is None:
            self.lowerlimx = np.min(x) * 0.9
        if self.lowerlimy is None:
            self.lowerlimy = np.min(y) * 0.9
        # Upper limit for x-axis/y-axis
        if self.upperlimx is None:
            self.upperlimx = np.max(x) * 1.1
        if self.upperlimy is None:
            self.upperlimy = np.max(y) * 1.1

        self.width = wd
        self.linewidth = lw

        # Set default width and linewidth if not provided
        if self.linewidth is None:
            self.linewidth = 1
        if self.width is None:
            self.width = 1

    def plot(self):
        """
        Create and display the bar plot.

        This method creates a matplotlib figure and plots the data
        as bars with the specified properties. It applies all configured
        settings such as bar width, linewidth, and axis limits before
        displaying the plot.

        Returns
        -------
        None
            The plot is displayed but not returned.
        """
        plt.style.use("_mpl-gallery")
        fig, ax = plt.subplots()
        ax.bar(self.x, self.y, width=self.width, edgecolor="black", linewidth=1)
        ax.set(
            xlim=(self.lowerlimx, self.upperlimx),
            xticks=np.arange(self.lowerlimx + 1, self.upperlimx),
            ylim=(self.lowerlimy, self.upperlimy),
            yticks=np.arange(self.lowerlimy + 1, self.upperlimy),
        )
        plt.show()
