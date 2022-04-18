from sympy.abc import x
from tools import mytools
from seminar5_math.v_graphen.kurvendiskussion import curve_discussion


def kd1():
    f = -2 * x ** 4 + 4 * x ** 3 - x ** 2 + 1000
    curve_discussion(f, [], [995, 1050], [])
    curve_discussion(f, [], [], [])


def kd2():
    f = 1 * x ** 4 - 2 * x ** 2
    curve_discussion(f, [-3, 6], [-2, 5], [])


def main():
    mytools.h1("curve_discussion_3.main()")
    kd1()
    kd2()
    print("\n*** end of curve_discussion_3 ***")


if __name__ == "__main__":
    main()
