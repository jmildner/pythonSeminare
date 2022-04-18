from matplotlib import pyplot as plt
from sympy.abc import x

from tools import mytools


def plot_the_graph(g0, g1, g2, g3, xa, ya, kl):
    mytools.h2("Plot the Graph")
    x0l = []
    x1l = []
    x2l = []
    x3l = []
    y0l = []
    y1l = []
    y2l = []
    y3l = []
    for r in range(-1000, 1001):
        i = r / 100
        if i in kl:
            pass
        else:
            x0l.append(i)
            y0l.append(float(g0.subs(x, i)))
            if g1 is not None:
                x1l.append(i)
                y1l.append(float(g1.subs(x, i)))
            if g2 is not None:
                x2l.append(i)
                y2l.append(float(g2.subs(x, i)))
            if g3 is not None:
                x3l.append(i)
                y3l.append(float(g3.subs(x, i)))
    print(x0l)
    print(y0l)
    print(y1l)
    print(y2l)
    print(y3l)
    plot_it(f"f(x)=({g0})", x0l, y0l, x1l, y1l, x2l, y2l, x3l, y3l, xa, ya)


def plot_it(title, x0l, y0l, x1l, y1l, x2l,y2l, x3l,y3l, xa, ya, ):
    plt.suptitle(title)
    if len(xa) > 0:
        plt.xlim(xa[0], xa[1])
    if len(ya) > 0:
        plt.ylim(ya[0], ya[1])
    if len(y0l) > 0: plt.plot(x0l, y0l, linestyle="solid")
    if len(y1l) > 0: plt.plot(x1l, y1l, linestyle="--")
    if len(y2l) > 0: plt.plot(x2l, y2l, linestyle="dotted")
    if len(y3l) > 0: plt.plot(x3l, y3l, linestyle="dotted")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    plt.show()
