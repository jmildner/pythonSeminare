from sympy.abc import x
from tools import mytools
from seminar5_math.v_graphen.kurvendiskussion import curve_discussion


def kd1():
    # pow(x,2) + 4x
    f = -1 * x ** 2 + 4 * x
    curve_discussion(f, [], [], [])


def kd2():
    # pow(x,3) + 4pow(x,2) - 12x -100
    f = x ** 3 + 4 * x ** 2 - 12 * x - 100
    curve_discussion(f, [], [], [])


def kd3():
    # pow(x,4) + pow(x,3) -1
    f = x ** 4 + 1 * x ** 3 - 1
    curve_discussion(f, [-1.5, 1], [-1.2, 0.5], [])
    curve_discussion(f, [], [], [])


def kd4():
    f = (x + 2) ** 2
    curve_discussion(f, [-10, 10], [-10, 10], [])


def kd5():
    # pow(x,2) + 2x + 1
    f = x ** 2 + 2 * x + 1
    curve_discussion(f, [-10, 10], [-10, 10], [])


def kd6():
    # pow(x,2) - 60
    f = 1 * x ** 2 - 60
    curve_discussion(f, [], [], [])


def kd7():
    # pow(x,2) + 60
    f = -1 * x ** 2 + 60
    curve_discussion(f, [], [], [])


def kd8():
    # pow(x,3)
    f = x ** 3
    curve_discussion(f, [], [], [])


def main():
    mytools.h1("curve_discussion_1.main()")
    kd8()
    kd7()
    kd6()
    kd1()
    kd2()
    kd3()
    kd4()
    kd5()
    print("\n*** end of curve_discussion_1 ***")


if __name__ == "__main__":
    main()
