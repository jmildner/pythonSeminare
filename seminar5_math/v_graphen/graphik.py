import matplotlib.pyplot as plt


def f1(ylist, x):
    ylist.append(x ** 3 + 10 * x ** 2 + 10*x + 10)


def f2(ylist, x):
    ylist.append((3 * x ** 4 + 2 * x ** 3 + 17 * x ** 2 + x + 25))


def f3(ylist, x):
    # 1 / x2
    if x == 0:
        ylist.append(None)
    else:
        ylist.append(1 / (x ** 2))


def f4(ylist, x):
    ylist.append(4 - x ** 2)


def f5(ylist, x):
    # (x2 + 2x + 1) / (x + 3)
    if x == -3:
        ylist.append(None)
    else:
        ylist.append((x ** 2 + 2 * x + 1) / (x + 3))


def get_y(xlist):
    ylist = []
    for x in xlist:
        f1(ylist, x)

    return ylist


def main():
    x = []
    for i in range(-100, 50):
        x.append(i / 10)
    y = get_y(x)
    print(x)
    print(y)
    plt.plot(x, y)
    plt.show()
    print("\n*** end of program ***")


if __name__ == "__main__":
    main()
