from tools import mytools


def ggt(a, b):
    a = abs(a)
    b = abs(b)
    if a == b:
        return a

    while True:
        if a < b:
            (a, b) = (b, a)
        a -= b
        if a == b:
            return a


def main():
    mytools.h1("Übung 6.3 - ggt")

    show_ggt(150, 12)
    show_ggt(25, 15)
    show_ggt(60, 15)
    show_ggt(324, 12)
    show_ggt(325, 7)

    mytools.end(__name__)

def show_ggt(a, b):
    print(f'ggt({a},{b}) = {ggt(a, b)}')


if __name__ == "__main__":
    main()
