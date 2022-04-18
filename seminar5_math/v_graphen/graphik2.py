import matplotlib.pyplot as plt

from tools import mytools as mt


def graph7():
    mt.h1("downward open parable - (-4x2 + 60)")
    xl = []
    yl = []
    y1l = []
    y2l = []
    for i in range(-60, 61):
        x = i / 10
        xl.append(x)
        yl.append(-4 * x ** 2 + 60)
        y1l.append(-8 * x)
        y2l.append(-8)
    print(xl)
    print(yl)
    print(y1l)
    print(y2l)
    plt.plot(xl, yl, linestyle="dotted")
    plt.plot(xl, y1l, linestyle="dotted")
    plt.plot(xl, y2l, linestyle="dotted")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    plt.show()


def graph8():
    mt.h1("downward open parable - (-4x2 + 60)")
    xl = []
    yl = []
    y1l = []
    y2l = []
    for i in range(-60, 61):
        x = i / 10
        xl.append(x)
        yl.append(-4 * x ** 2 + 60)
        y1l.append(-8 * x)
        y2l.append(-8)
    print(xl)
    print(yl)
    print(y1l)
    print(y2l)
    plt.plot(xl, yl, linestyle="dotted")
    plt.plot(xl, y1l, linestyle="dotted")
    plt.plot(xl, y2l, linestyle="dotted")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    plt.show()


def f1(x):
    y = (x ** 3 + 10 * x ** 2 + 10 * x + 10)


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


def f5(x):
    global xl, yl, y1l, y2l
    # (x2 + 2x + 1) / (x + 3)
    xl.append(x)
    if x != -3:
        y = ((x ** 2 + 2 * x + 1) / (x + 3))
        yl.append(y)
    else:
        yl.append(None)


def f6(x):
    global xl, yl, y1l, y2l
    # (x2 + 2x + 1)
    xl.append(x)
    yl.append((x ** 2 + 2 * x + 1))
    y1l.append(2 * x + 2)
    y2l.append(2)


def main():
    graph7()
    graph8()
    print("\n*** end of program ***")


if __name__ == "__main__":
    main()
