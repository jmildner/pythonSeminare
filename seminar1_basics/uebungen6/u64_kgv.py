from tools import mytools

def kgv(a, b):
    a = abs(a)
    b = abs(b)
    if a == b:
        return a

    if a < b:
        (a, b) = (b, a)

    m = a
    while a % b != 0:
        a += m

    return a


def main():
    mytools.h1("Übung 6.4 - kgv")

    show_kgv(3, 5)
    show_kgv(3, 6)
    show_kgv(20, 30)
    show_kgv(20, 60)
    show_kgv(15, 12)
    show_kgv(1001, 7)
    show_kgv(1002, 7)


    mytools.end(__name__)



def show_kgv(a, b):
    print(f'kgv({a},{b}) = {kgv(a, b)}')


if __name__ == "__main__":
    main()
