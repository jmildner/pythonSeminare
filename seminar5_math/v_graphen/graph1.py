import matplotlib.pyplot as plt
from sympy import symbols

from tools import mytools as mt


def graph2(x,f):
    mt.h2("downward open parable - (-4x2 + 60)")
    print(x,f)
    xl = []
    yl = []
    y1l = []
    y2l = []

    for i in range(-60, 61):
        w = i / 10
        xl.append(w)
        erg=f.subs(x,w)
        abl1=f.diff(x)
        print("xxx",erg,type(erg))
        print("ab1", f.subs(abl1,w), type(erg))
        yl.append(erg)
        y1l.append(-8 * x)
        y2l.append(-8)
    print(xl)
    print(yl)
    print(y1l)
    print(y2l)
    plt.plot(xl, yl, linestyle="dotted")
    #plt.plot(xl, y1l, linestyle="dotted")
    plt.plot(xl, y2l, linestyle="dotted")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    plt.show()


def graph1():
    mt.h2("downward open parable - (-4x2 + 60)")
    xl = []
    yl = []
    y1l = []
    y2l = []
    for i in range(-60, 61):
        x = i / 10
        xl.append(x)
        yl.append(-4 * x ** 2 + 60)
        y1l.append(-8 * x)
        y2l.append(-8)
    print(xl)
    print(yl)
    print(y1l)
    print(y2l)
    plt.plot(xl, yl, linestyle="--")
    plt.plot(xl, y1l, linestyle="--")
    plt.plot(xl, y2l, linestyle="--")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    plt.show()


def main():
    #graph1()

    x = symbols("x")
    f = -4 * x ** 2 + 60
    graph2(x,f)
    graph1()
    print("\n*** end of graph1 ***")


if __name__ == "__main__":
    main()
