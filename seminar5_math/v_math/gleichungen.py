import sympy
from matplotlib import pyplot as plt
from sympy import *  # enables trig functions, among other things
from sympy import symbols  # enables symbol function
from sympy.solvers import solve
from sympy import Function
from sympy.abc import t, x, y, v
from tools import mytools as mt

mt.h2("assert")
assert (solve(x - 3, x) == [3])
print(solve(x ** 2 - 1, x))
mt.h2("erg")
erg = solve(x ** 7 - x ** 2 + x - 100, x)
for e in erg:
    print(complex(e))
print()
erg2 = solve(5 * x ** 3 - 1 * x - 22, x)
for e in erg2:
    print(complex(e))
print()
xlist = []
ylist = []
for e in erg:
    x = complex(e)
    xlist.append(x.real)
    ylist.append(x.imag)
    print(f"real: {x.real}, imag: {x.imag}")

plt.plot(xlist, ylist, "ob")
plt.show()


def main():
    mt.h1("gleichungen")
    al, al_prime1 = symbols("al"), symbols("al_prime1")
    p1, p2, q1, q2 = symbols("p1"), symbols("p2"), symbols("q1"), symbols("q2"),
    v_prime1 = symbols("v_prime1")
    print(p1)
    print("\n*** end of gleichungen ***")


if __name__ == "__main__":
    main()
