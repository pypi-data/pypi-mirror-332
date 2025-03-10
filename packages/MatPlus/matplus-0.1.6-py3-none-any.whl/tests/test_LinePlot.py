import matplotlib.pyplot as plt
from MatPlus.LinePlot import LinePlot


def test_lineplot_creation():
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot = LinePlot(x, y)
    assert plot.x == x
    assert plot.y == y
    assert plot.lowerlimx is None
    assert plot.upperlimx is None
    assert plot.lowerlimy is None
    assert plot.upperlimy is None


def test_lineplot_with_limits():
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot = LinePlot(x, y, lowerlimx=0, upperlimx=4, lowerlimy=0, upperlimy=4)
    assert plot.lowerlimx == 0
    assert plot.upperlimx == 4
    assert plot.lowerlimy == 0
    assert plot.upperlimy == 4


def test_multiple_lines():
    x = [[1, 2, 3], [4, 5, 6]]
    y = [[1, 2, 3], [4, 5, 6]]
    plot = LinePlot(x, y)
    assert len(plot.x) == 2
    assert len(plot.y) == 2


def test_plot_creation():
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot = LinePlot(x, y)
    plot.plot()
    plt.close()  # Cleanup


def test_plot_with_parameters():
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot = LinePlot(x, y, lowerlimx=0, upperlimx=4, lowerlimy=0, upperlimy=4, lw=2.0)
    plot.plot()
    plt.close()  # Cleanup
