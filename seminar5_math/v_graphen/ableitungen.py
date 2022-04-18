from tools import mytools
from sympy import *

x = symbols('x')


def ableitungen(f0, note):
    print(f"\n---------- {note} --------")

    null_stellen = solve(f0, x)
    for ns in null_stellen:
        try:
            print("Nullstellen:", float(ns))
        except:
            pass

    f1 = f0.diff(x)
    f2 = f1.diff(x)
    f3 = f2.diff(x)

    print(f"f0: {str(f0):30}")
    print(f"f1: {str(f1):30}")
    print(f"f2: {str(f2):30}")
    print(f"f3: {str(f3):30}")


def konstanten():
    mytools.h2("Konstanten")
    fx1 = 5 + 0 * x  # Konstante 5
    fx2 = 2 ** (1 / 2) + 0 * x  # 2. wurzel aus 2
    fx3 = 5 ** (5 / 3) + 0 * x  # 3. Wurzel aus 5 hoch 3
    ableitungen(fx1, "Konstante 5")
    ableitungen(fx2, "Wurzel aus 2")
    ableitungen(fx3, "3.Wurzel aus 5 hoch 3")


def potenzen():
    mytools.h2("Potenzen")
    fx1 = x ** 3  # x hoch 3
    fx2 = x ** -7  # x hoch -7
    ableitungen(fx1, "x hoch 3")
    ableitungen(fx2, "x hoch -7")


def faktoren():
    mytools.h2("Faktoren")
    fx1 = 3 * x ** 5  # 3 * x hoch 5
    fx2 = 2 ** (1 / 2) * x ** 4  # wurzel 2 * x hoch 4
    ableitungen(fx1, "3 mal x hoch 5")
    ableitungen(fx2, "wurzel 2 mal x hoch 4")


def summen():
    mytools.h2("summen")
    fx1 = x ** 2 - 5 * x ** 3 - 7
    ableitungen(fx1, "")


def produkte():
    mytools.h2("produkte")
    fx1 = (x ** 2 - 5) * (5 * x ** 3)
    fx2 = (x ** 2 - 5) * (x)
    ableitungen(fx1, "(x2 - 5) * (5x3)")
    ableitungen(fx2, "(x2 - 5) * (x)")


def quotienten():
    mytools.h2("quotienten")
    fx1 = (x ** 2 - 5) / (5 * x ** 3)
    fx2 = (x ** 2 - 5) / (x)
    ableitungen(fx1, "(x2 - 5) / (5x3)")
    ableitungen(fx2, "(x2 - 5) /"
                     " (x)")


def main():
    mytools.h1("Ableitungen")
    konstanten()
    potenzen()
    faktoren()
    summen()
    produkte()
    quotienten()

    print("\n*** end of ableitungen ***")


if __name__ == "__main__":
    main()
