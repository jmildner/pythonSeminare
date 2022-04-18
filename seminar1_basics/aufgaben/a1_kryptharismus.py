from seminar1_basics.uebungen6.u63_ggt import ggt
from tools import mytools


def main():
    mytools.h1("Kryptharismus")

    for e in range(1, 10):
        for v in range(0, 10):
            for d in range(1, 10):
                for i in range(0, 10):
                    eve = e * 100 + v * 10 + e * 1
                    did = d * 100 + i * 10 + d * 1
                    if eve < did:
                        talk = eve / did
                        talk = int(talk * 10000000000000)
                        talk = str(talk)
                        t1 = talk[0:4]
                        t2 = talk[4:8]
                        t3 = talk[8:12]
                        if t1 == t2 and t2 == t3:
                            digit_set = {e, v, d, i,
                                         int(t1[0:1]),
                                         int(t1[1:2]),
                                         int(t1[2:3]),
                                         int(t1[3:4])}
                            if len(digit_set) == 8:
                                if ggt(eve, did) == 1:
                                    print(
                                        f"solution: {eve} / {did} = 0.{talk[0:4]}'{talk[4:8]}'{talk[8:12]}...")


if __name__ == "__main__":
    main()
