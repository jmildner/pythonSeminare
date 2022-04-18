from sympy.abc import x
from tools import mytools
from seminar5_math.v_graphen.kurvendiskussion import curve_discussion


def kd1():
    f = 1 / (x - 2)
    curve_discussion(f, [-10, 10], [-10, 10], [2])


def kd2():
    f = 1 / (x ** 2)
    curve_discussion(f, [-10, 10], [-10, 10], [0])


def kd3():
    f = (x - 3) / (x ** 2 - 9)
    curve_discussion(f, [-15, 15], [-15, 15], [3, -3])


def kd4():
    f = (x ** 2 - 4) / ((x - 2) * x)
    curve_discussion(f, [-3, 3], [-10, 10], [0])


def main():
    mytools.h1("curve_discussion_2.main()")
    kd1()
    kd2()
    kd3()
    kd4()
    print("\n*** end of curve_discussion_2 ***")


if __name__ == "__main__":
    main()
