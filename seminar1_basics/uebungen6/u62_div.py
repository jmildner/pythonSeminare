from tools import mytools


def div(p1, p2):
    if p1 == 0: return 0
    if p2 == 0: return 0

    vz = 0
    if p1 < 0:
        vz += 1
    if p2 < 0:
        vz += 1
    a = abs(p1)
    b = abs(p2)

    erg = 0
    while a >= b:
        a -= b
        erg += 1

    if vz == 1:
        erg = -erg

    return erg


def main():
    mytools.h1("Übung 6.2 - div")

    show_div(150, 12)
    show_div(-150, 12)
    show_div(150, -12)
    show_div(-150, -12)
    show_div(6000, 12)
    show_div(12, 6000)
    show_div(1, 1)
    show_div(0, -1)
    show_div(-10, 0)

    mytools.end(__name__)

def show_div(a, b):
    print(f'{a} / {b} = {div(a, b)}')


if __name__ == "__main__":
    main()
