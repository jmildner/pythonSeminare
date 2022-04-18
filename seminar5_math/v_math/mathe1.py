from math import sqrt
import matplotlib.pyplot as plt
from sympy import symbols, solve
from tools import mytools as mt

x = symbols("x")
y = symbols("y")


def graph2(x, f):
    mt.h2("graph2: downward open parable - (-4x2 + 60)")
    print(f"x: {x}, functiom: {f}")
    xl = []
    yl = []
    y1l = []
    y2l = []

    for i in range(-60, 61):
        w = i / 10
        xl.append(w)
        erg = f.subs(x, w)
        abl1 = f.diff(x)
        print("xxx", erg, type(erg))
        print("ab1", f.subs(abl1, w), type(erg))
        yl.append(erg)
        y1l.append(-8 * x)
        y2l.append(-8)
    print(xl)
    print(yl)
    print(y1l)
    print(y2l)
    plt.plot(xl, yl, linestyle="dotted")
    # plt.plot(xl, y1l, linestyle="dotted")
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


def do_function_subs(function, x_value) -> None:
    print(f"\ndo_function_subs: [{str(function)}]  ({x_value})")
    erg = function.subs(x, x_value)
    try:
        print("\t",float(erg))
    except TypeError:
        print("\t",complex(erg))


def do_solve(function) -> None:
    print(type(function))
    print(f"\ndo_solve: [{str(function)}]")
    erg = solve(function, x)
    print(erg,type(erg))
    for e in erg:
        try:
            print("\t", float(e))
        except TypeError:
            print("\t",complex(e))
    mt.pause()


def main():
    function = 4 * x ** 2 + 60
    do_function_subs(function, 10)
    do_function_subs(x * 7, 2)
    do_function_subs(x ** 30, 2)
    do_function_subs(x ** 3, -1)
    do_function_subs(x ** (1 / 3), -1)
    do_solve(x ** 3 + 1)
    do_function_subs(x ** 3, -1)
    do_solve(3*x**5 - x**3 + x -100)
    do_solve(x / (5))

    print("\n*** end of mathe1 ***")


if __name__ == "__main__":
    main()
