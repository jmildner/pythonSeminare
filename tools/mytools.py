# -------------
# get_functions
# -------------


def geti(prompt) -> int:
    return geti_r(prompt, -2000000000, 2000000000)


def geti_r(prompt, a, b) -> int:
    while True:
        s = input(prompt + " > ")
        if not s.isdigit():
            print("not numeric ", end=" ... ")
            continue
        i = int(s)
        if i < a or i > b:
            print("out of range", end=" ... ")
            continue
        return i


def getf(prompt) -> float:
    return float(input(prompt + " > "))


def gets(prompt) -> str:
    return input(prompt + " > ")

# -------------
# headings
# -------------


def h1(txt) -> None:
    stg = len(txt) * "-"
    print()
    print("/-" + stg + "-\\")
    print("! " + txt + " !")
    print("\\-" + stg + "-/")


def h2(txt) -> None:
    stg = len(txt) * "-"
    print()
    print("+-" + stg + "-+")
    print("! " + txt + " !")
    print("+-" + stg + "-+")


def end(name):
    if name == "__main__":
        input("\n*** hit enter to continue *** ")
    else:
        pause("end of " + name)


def pause(msg=None) -> None:
    if msg == None:
        input("\n*** hit enter to continue *** ")
    else:
        input(f"\n*** {msg} - hit enter to continue *** ")
