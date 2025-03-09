import matplotlib.pyplot as plt

plt.style.use("_mpl-gallery")


class LinePlot:
    """
    A class for creating line plots using matplotlib.

    The LinePlot class provides a simplified interface for creating line plots
    with customizable axis limits and line properties. It supports plotting
    multiple lines on the same figure.

    Parameters
    ----------
    x : list or list of lists
        The x-coordinates of the line(s). For multiple lines, provide a list of lists.
    y : list or list of lists
        The y-coordinates of the line(s). For multiple lines, provide a list of lists.
    lowerlimx : float, optional
        Lower limit of the x-axis. Default is None (auto-determined).
    lowerlimy : float, optional
        Lower limit of the y-axis. Default is None (auto-determined).
    upperlimx : float, optional
        Upper limit of the x-axis. Default is None (auto-determined).
    upperlimy : float, optional
        Upper limit of the y-axis. Default is None (auto-determined).
    lw : float, optional
        Line width for the plot. Default is None (uses matplotlib default).

    Examples
    --------
    >>> # Single line plot
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [1, 4, 9, 16, 25]
    >>> line_plot = LinePlot(x, y)
    >>> line_plot.plot()

    >>> # Multiple line plot
    >>> x = [[1, 2, 3], [1, 2, 3, 4]]
    >>> y = [[1, 2, 3], [4, 3, 2, 1]]
    >>> line_plot = LinePlot(x, y, lowerlimx=0, upperlimx=5)
    >>> line_plot.plot()
    """

    def __init__(
        self,
        x,
        y,
        lowerlimx=None,
        lowerlimy=None,
        upperlimx=None,
        upperlimy=None,
        lw=None,
    ):
        self.x = x
        self.y = y
        self.lowerlimx = lowerlimx
        self.lowerlimy = lowerlimy
        self.upperlimx = upperlimx
        self.upperlimy = upperlimy
        self.linewidth = lw

    def plot(self):
        """
        Create and display a line plot.

        This method creates a matplotlib figure and plots the data
        provided during initialization. If multiple lines were provided,
        all lines will be displayed on the same plot.

        Returns
        -------
        None
            The plot is displayed but not returned.
        """
        plt.figure()
        for x_data, y_data in zip(self.x, self.y):
            plt.plot(x_data, y_data, linewidth=self.linewidth)
        plt.xlim(self.lowerlimx, self.upperlimx)
        plt.ylim(self.lowerlimy, self.upperlimy)
        plt.show()
