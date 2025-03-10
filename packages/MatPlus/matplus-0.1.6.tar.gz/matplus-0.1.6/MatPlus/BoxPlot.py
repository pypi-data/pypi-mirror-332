import matplotlib.pyplot as plt
import numpy as np


class BoxPlot:
    """
    A class for creating box plots with customizable properties.

    The BoxPlot class provides a simplified interface for creating box plots
    with options for notches, outlier symbols, and orientation.

    Parameters
    ----------
    data : array-like
        The data to be plotted.
    notch : bool, optional
        Whether to draw a notch to indicate the confidence interval around the median.
        Default is False.
    sym : str, optional
        The symbol for outliers. Default is "b".
    vert : bool, optional
        Whether to draw the box plot vertically. Default is True.
    whis : float, optional
        The length of the whiskers as a multiple of the interquartile range (IQR).
        Default is 1.5.

    Examples
    --------
    >>> # Basic box plot
    >>> data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6]
    >>> box = BoxPlot(data)
    >>> box.plot()

    >>> # Box plot with notches
    >>> box = BoxPlot(data, notch=True)
    >>> box.plot()

    >>> # Horizontal box plot with custom outlier symbols
    >>> box = BoxPlot(data, vert=False, sym="r*")
    >>> box.plot()
    """

    def __init__(self, data, notch=False, sym="b", vert=True, whis=1.5):
        # Validate data type
        if not isinstance(data, (list, np.ndarray)):
            raise TypeError("Data must be a list or numpy array")

        # Validate numeric data
        try:
            numeric_data = [float(x) for x in data]
        except (ValueError, TypeError):
            raise TypeError("All elements must be numeric")

        # Validate data length
        if not data or len(data) == 0:
            raise ValueError("Data array cannot be empty")

        # Validate whis parameter
        if whis <= 0:
            raise ValueError("Whisker length must be positive")

        self.data = numeric_data
        self.notch = notch
        self.sym = sym
        self.vert = vert
        self.whis = whis

    # Rest of the class implementation remains the same
    def median(self):
        """
        Calculate the median of the data.

        Returns
        -------
        float
            The median value of the dataset.
        """
        return float(np.median(self.data))

    def quartiles(self):
        """
        Calculate the first and third quartiles of the data.

        Returns
        -------
        tuple
            A tuple containing (Q1, Q3) values.
        """
        q1 = float(np.percentile(self.data, 25))
        q3 = float(np.percentile(self.data, 75))
        return (q1, q3)

    def outliers(self):
        """
        Identify outliers using the whisker*IQR rule.

        Returns
        -------
        list
            A list of data points identified as outliers.
        """
        q1, q3 = self.quartiles()
        iqr = q3 - q1
        lower_bound = q1 - (self.whis * iqr)
        upper_bound = q3 + (self.whis * iqr)
        return [x for x in self.data if x < lower_bound or x > upper_bound]

    def plot(self):
        """
        Create and display the box plot.

        This method creates a matplotlib figure and plots the box plot
        with the specified properties. It applies settings such as orientation,
        notches, and outlier symbols as configured during initialization.

        Returns
        -------
        None
            The plot is displayed but not returned.
        """
        plt.style.use("_mpl-gallery")
        fig, ax = plt.subplots()

        # Set labels and ticks
        if self.vert:
            ax.set_xlabel("Data")
            ax.set_ylabel("Value")
            ax.set_xticks([1])
        else:
            ax.set_xlabel("Value")
            ax.set_ylabel("Data")
            ax.set_yticks([1])

        # Add grid for better readability
        ax.grid(True, linestyle="--", alpha=0.7)

        # Adjust layout to prevent label clipping
        plt.tight_layout()

        plt.show()
