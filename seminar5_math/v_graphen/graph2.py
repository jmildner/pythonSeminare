import matplotlib.pyplot as plt
from sympy import solve

from tools import mytools as mt
from sympy.abc import x


def graph2():
    mt.h2("graph with high point and low point - (x3 - 10x2)")
    xl = []
    yl = []
    y1l = []
    y2l = []
    for i in range(-6, 12):
        x = i
        xl.append(x)
        # yl.append(x ** 3 - 10 * x ** 2)
        # y1l.append(3 * x ** 2 - 20 * x)
        # y2l.append(6 * x - 20)
        yl.append(2 * x ** 3 - 16 * x ** 2 + 100)
        y1l.append(6 * x ** 2 - 32 * x)
        y2l.append(12 * x - 32)
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
    erg = solve(6 * x ** 2 - 32 * x, x)
    print(erg)
    for e in erg:
        print(float(e), float(12 * e ** 2 - 32 * e))


def main():
    extreme_points()
    graph2()
    print("\n*** end of graph2 ***")


if __name__ == "__main__":
    main()
