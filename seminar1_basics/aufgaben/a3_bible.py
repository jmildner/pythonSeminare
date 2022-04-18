import queue
from tools import mytools as mt


def main():
    mt.h1("Word analysis")
    with open("bibel.txt", 'r', encoding='utf-8') as file:
        buffer = file.read()

        records = buffer.split("\n")
        d = {}
        for rec in records:
            for char in rec:
                if char in "»«-'\"()?,.!/;:":
                    rec = rec.replace(char, '')
            if rec.endswith(" "):
                rec = rec[:-1]

            words = rec.split(" ")

            for word in words:
                word = word.lower()
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
        counter = 0
        pq = queue.PriorityQueue()
        for word, number in d.items():
            pq.put((-number, word))
            counter += number

        while not pq.empty():
            print(pq.get())

        print("Number of words:", counter)
        print("Number of different words:", len(d))

    print()


if __name__ == "__main__":
    main()
