from tools import mytools


def get_heads():
    return mytools.geti_r("enter number of animals", 0, 10_000)


def get_legs(heads):
    while True:
        minimum_legs = heads * 2
        maximum_legs = heads * 4
        legs = mytools.geti_r(
            f"enter number of legs {minimum_legs}-{maximum_legs}", minimum_legs, maximum_legs)
        if legs % 2 == 0:
            return legs
        else:
            print("number of legs must be even ... ")


def main():
    mytools.h1("Farm")

    heads = get_heads()
    legs = get_legs(heads)

    pigs = 0
    hens = heads

    while pigs * 4 + hens * 2 != legs:
        pigs += 1
        hens -= 1

    print(f"there are {pigs} pigs and {hens} hens")


if __name__ == "__main__":
    main()
