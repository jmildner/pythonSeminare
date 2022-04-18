from sympy.abc import x
from tools import mytools
from seminar5_math.v_graphen.kurvendiskussion import curve_discussion


def kd1():
    f = (3 * x ** 2 - 7) / (2 * x - 4)
    curve_discussion(f, [-10, 10], [-10, 40], [2])


def main():
    mytools.h1("curve_discussion_4.main()")
    kd1()
    print("\n*** end of curve_discussion_4 ***")


if __name__ == "__main__":
    main()
