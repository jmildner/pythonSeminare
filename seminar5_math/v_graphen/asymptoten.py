from sympy import *
from sympy.abc import x

from tools import mytools
from seminar5_math.v_graphen.plot_the_graph import plot_the_graph


def vertical_asymptote(numerator, denominator):
    # get nulls of denominator

    null_points = solve(denominator, x)
    if len(null_points) == 0:
        print("no vertical asymptotes")
        return

    for m in null_points:
        w = numerator.subs(x, m)
        if w != 0:
            try:
                print(f"vertical asymptote at x={float(m)}")
            except TypeError:
                pass
        else:
            print("fraction can be shortened")


def asymptotes(z_funct, n_funct, x_axis, y_axis, no_solutions):
    funct = z_funct / n_funct
    print(z_funct, n_funct)
    mytools.h1(f"Asymptotes of the Function [{funct}]")
    print(f"no solutions at {no_solutions}")
    vertical_asymptote(z_funct, n_funct)

    diff1 = None
    diff2 = None
    diff3 = None

    plot_the_graph(funct, diff1, diff2, diff3, x_axis, y_axis, no_solutions)


def asymptotes1():
    z = (3 * x ** 2 - 7)
    n = (2 * x - 4)
    asymptotes(z, n, [-8, 8], [-60, 60], [2])


def asymptotes2():
    z = x * (x - 2)
    n = (2 * x - 4)
    asymptotes(z, n, [-8, 8], [-60, 60], [2])


def asymptotes3():
    mytools.h2("3 horizontal y=0")
    z = x ** 2 - 3
    n = (4 * x ** 3 - 2)
    asymptotes(z, n, [-8, 8], [-60, 60], [1/x**(1/3)])


def asymptotes4():
    mytools.h1("4 horizontal y=0.5")
    z = 2 * x ** 2 - 5 * x
    n = (4 * x ** 3 + 2 * x ** 2)
    asymptotes(z, n, [-10, 10], [-1, 1], [-2, -0.5, 0])


def main():
    asymptotes4()
    asymptotes3()
    asymptotes1()
    asymptotes2()
    print("\n*** end of asymptotes ***")


if __name__ == "__main__":
    main()
