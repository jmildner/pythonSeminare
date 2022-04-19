from tools import mytools as mt


def main():
    mt.h1("Übung 7.12 - Strings")

    mt.h2("zeichenkette -> list und v.v")
    s1 = "123"
    l = list(s1)

    s2 = ""
    for c in l:
        s2 += c

    print(s1, l, s2)

    mt.h2("Operatoren + und *")
    str1 = "Zeichenkette"
    str2 = str1 + "\n" + 12 * "="
    print(str1)
    print(str2)

    mt.h2("Teilstrings")
    c1 = str1[0]
    c2 = str1[1:7]
    c3 = str1[-5:]
    print(c1, c2, c3)

    mt.h2("Iterieren")
    for s in str1:
        print(s, end=" ")
    print()
    print()
    for ix, elem in enumerate(str1):
        print(ix, elem)
    print()
    for i in range(len(str1)):
        print(i, str1[i])

    mt.h2("Methoden")
    upper_str = "HALLO WELT"
    lower_str = "hallo universe"
    name = "friedrich"
    text = "u01_classes u02_vererbung ccc u01_classes u02_vererbung ccc xxx mmm mmm mmm"
    planeten = "merkur venus erde mars jupiter saturn uranus (neptun)"
    print(upper_str, "len:", len(upper_str))
    print(upper_str, upper_str.lower())
    print(lower_str, lower_str.upper())
    print(name, name.capitalize())
    print(f"{text} beinhaltet {text.count('u01_classes')} u01_classes's")
    print(f"{planeten} - erde2 steht an inde {planeten.find('erde2')} im text")
    print(f"{planeten} - erde steht an inde {planeten.index('erde')} im text")
    dig1 = "111"
    dig2 = "11x"
    num = "111"
    dec = "111"
    print(f"{dig1} isdigit - {dig1.isdigit()}")
    print(f"{dig2} isdigit - {dig2.isdigit()}")
    print(f"{num} isnumeric - {num.isnumeric()}")
    print(f"{dec} isdecimal - {dec.isdecimal()}")
    print(lower_str.replace("hallo", "hello"))
    print(text)
    print(text.replace("u01_classes", "qqq", 1))  # only 1
    print(text.replace("u01_classes", "qqq"))  # all
    print(name.startswith("fried"))
    print(name.endswith("rich"))

    mt.end(__name__)


if __name__ == "__main__":
    main()
