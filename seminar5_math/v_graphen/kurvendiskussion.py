from sympy import *
from sympy.abc import x

from tools import mytools
from seminar5_math.v_graphen.plot_the_graph import plot_the_graph


def show_range_of_values(f):
    mytools.h2(f"Range of values for x from  -10 to +10")
    for i in range(-10, 10):
        erg = f.subs(x, i)
        try:
            print(f"{i:3} {float(erg):25} \t\t {type(erg)}")
        except TypeError:
            print(f"{i:3} {' ':25} \t\t {type(erg)}")


def show_function_and_differentials(f, a1, a2, a3):
    mytools.h2("function and differentials")
    print(f"f  : {str(f):30} ")
    print(f"a1 : {str(a1):30} ")
    print(f"a2 : {str(a2):30} ")
    print(f"a3 : {str(a3):30} ")


def show_null_points(f):
    mytools.h2(f"null points")
    null_points = solve(f, x)
    if len(null_points) == 0:
        print("no null points")
        return

    for m in null_points:
        try:
            print(float(m))
        except TypeError:
            pass


def show_extreme_points(a1, a2, a3):
    mytools.h2("high, low, saddle points")

    nulls1 = solve(a1, x)

    if len(nulls1) == 0:
        print("no extreme points")
        return

    for ix, m in enumerate(nulls1):
        print(f"{ix + 1}. extreme point")
        print(f"   x = ({m}) = {float(m)}  ", end=" --- ")
        w = a2.subs(x, m)
        if w < 0:
            print("high point")
        elif w > 0:
            print("low point")
        else:  # w==0
            w2 = a3.subs(x, m)
            if w2 != 0:
                print("saddle point")


def show_turning_points(a1, a2, a3):
    mytools.h2("turning points")

    nulls2 = solve(a2, x)
    wp_printed = False
    for ix, m in enumerate(nulls2):
        w = a3.subs(x, m)
        if w != 0:
            w2 = a1.subs(x, m)
            if w2 != 0:
                print(f"  {float(m)}: turning point")
                wp_printed = True
    if wp_printed:
        pass
    else:
        print("no turning points")


def curve_discussion(funct, x_axis, y_axis, no_solutions):
    mytools.h1(f"Curve Discussion of the Function [{funct}]")
    show_range_of_values(funct)
    print(no_solutions, type(no_solutions))
    diff1 = funct.diff(x)
    diff2 = diff1.diff(x)
    diff3 = diff2.diff(x)
    show_function_and_differentials(funct, diff1, diff2, diff3)
    show_null_points(funct)
    show_extreme_points(diff1, diff2, diff3)  # high, low, saddle
    show_turning_points(diff1, diff2, diff3)
    plot_the_graph(funct, diff1, diff2, diff3, x_axis, y_axis, no_solutions)


def main():
    f3 = (x ** 3 - 4)
    curve_discussion(f3, [-3, 3], [-10, 10], [0])
    f1 = (x ** 2 - 4) / ((x - 2) * x)
    curve_discussion(f1, [-3, 3], [-10, 10], [0])
    f2 = (x ** 2 - 12)
    curve_discussion(f2, [], [], [])
    curve_discussion(f2, [-5, 10], [], [])
    curve_discussion(f2, [], [-13, 8], [])
    print("\n*** end of curve_discussion ***")


if __name__ == "__main__":
    main()
