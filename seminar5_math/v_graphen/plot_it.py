from matplotlib import pyplot as plt
from sympy.abc import x
from tools import mytools


def plot_it(title, graphs, axis_ranges):
    # graphs is a list of graphs with x_values and y_values
    # axis_ranges is a dictionary with none, x and/or y range
    plt.suptitle(title)

    if axis_ranges:
        try:
            if axis_ranges["xr"]:
                xrange = axis_ranges["xr"]
                plt.xlim(xrange[0], xrange[1])
        except KeyError:
            pass

        try:
            if axis_ranges["yr"]:
                yrange = axis_ranges["yr"]
                plt.ylim(yrange[0], yrange[1])
        except KeyError:
            pass

    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))

    for graph in graphs:
        print(graph)
        print(graph[1])
        plt.plot(graph[0], graph[1])

    plt.show()


def fill_graph(f):
    g = []
    xlist = []
    ylist = []

    for i in range(-1000, 1001):
        xw = i / 100
        try:
            yw = float(f.subs(x,xw))
            xlist.append(xw)
            ylist.append(yw)
        except TypeError:
            pass

    g.append(xlist)
    g.append(ylist)

    return (g)


def invoke_plot_it():
    graphs = []
    graphs.append(fill_graph(f=2 * x - 3))
    graphs.append(fill_graph(f=x ** 2 + 5))
    graphs.append(fill_graph(f=(1 / x**2) -5))

    plot_it("title", graphs, None)

    axis_ranges = {"xr": [-10, 10], "yr": [-20, 50]}
    plot_it("title", graphs, axis_ranges)

    axis_ranges = {"xr": [-10, 10]}
    plot_it("title", graphs, axis_ranges)

    axis_ranges = {"yr": [-10, 20]}
    plot_it("title", graphs, axis_ranges)


def main():
    mytools.h1("plot_it()")
    invoke_plot_it()
    print("\n*** end of plot_it ***")


if __name__ == "__main__":
    main()
