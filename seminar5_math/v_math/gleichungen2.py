import sympy
from matplotlib import pyplot as plt
from sympy import *  # enables trig functions, among other things
from sympy import symbols  # enables symbol function
from sympy.solvers import solve
from sympy import Function
from sympy.abc import t, x, y, v
from tools import mytools as mt


def gleichungen2():
    mt.h2("gleichungen2")
    erg = (solve(x ** 2 - 2 * x - 35, x))
    for e in erg:
        e = complex(e)
        print(type(e), e)
    erg = (solve(x ** 2 - 2 * x + 35, x))
    for e in erg:
        e = complex(e)
        print(type(e), e)
    a = 8 + 5j
    print(a)
    print('Real Part = ', a.real)
    print('Imaginary Part = ', a.imag)
    print('Conjugate = ', a.conjugate())


def gleichungen1():
    mt.h2("gleichungen1")
    print(solve(x - 3, x))
    print(solve(x ** 2 - 144, x))
    print(solve(x ** 2 + 144, x))
    print(solve(x ** 2 - 1, x))
    print(solve(x ** 2 + 1, x))
    print(solve(x ** 3 - 1, x))
    print(solve(x ** 3 + 1, x))
    print(solve(x ** 4 - 1, x))
    print(solve(x ** 4 + 1, x))


def main():
    mt.h1("gleichungen")
    gleichungen1()
    gleichungen2()
    print("\n*** end of gleichungen ***")


if __name__ == "__main__":
    main()
