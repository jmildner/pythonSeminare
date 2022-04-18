import matplotlib.pyplot as plt
from sympy import solve

from tools import mytools as mt
from sympy.abc import x


def graph2():
    mt.h2("graph with high point and low point - (x3 - 2x)")
    xl = []
    yl = []
    y1l = []
    y2l = []
    for i in range(-40 ,41):
        x = i/10
        xl.append(x)
        yl.append(x ** 3 - 3 * x)
        y1l.append(3 * x ** 2 - 3)
        y2l.append(6 * x)

    print(xl)
    print(yl)
    print(y1l)
    print(y2l)

    plt.plot(xl, yl)
    plt.plot(xl, y1l, linestyle="dotted")
    plt.plot(xl, y2l, linestyle="dotted")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    plt.show()


def extreme_points():
    mt.h2("max points")
    erg = solve(3 * x ** 2 -3, x)
    for e in erg:
        print(float(e))


def main():
    extreme_points()
    graph2()
    print("\n*** end of graph2 ***")


if __name__ == "__main__":
    main()
