from tools import mytools


def mult(p1, p2):
    vz = 0
    if p1 < 0:
        vz += 1
    if p2 < 0:
        vz += 1
    a = abs(p1)
    b = abs(p2)

    if a > b:
        (a, b) = (b, a)

    erg = 0
    while a > 0:
        a -= 1
        erg += b

    if vz == 1:
        erg = -erg

    return erg


def main():
    mytools.h1("Übung 6.1 - mult")

    show_mult(12, 12)
    show_mult(-12, 12)
    show_mult(12, -12)
    show_mult(-12, -12)
    show_mult(12, 1_000_000_000_000)
    show_mult(1_000_000_000_000, 12)

    mytools.end(__name__)


def show_mult(a, b):
    print(f'{a} * {b} = {mult(a, b)}')


if __name__ == "__main__":
    main()
