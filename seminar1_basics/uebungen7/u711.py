import queue
from tools import mytools as mt


def main():
    mt.h1("Übung 7.11 - PriorityQueue")

    q = queue.PriorityQueue()
    q.put((5, "Hallo"))
    q.put((1, "Welt"))

    while not q.empty():
        print(q.get())

    mt.h2("die häufigsten Vorkommen")
    text = "a a a b b c c c c c d d e e f f f g g g g g h i j"
    d = {}
    for word in text.split(" "):
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    print(d)

    pq = queue.PriorityQueue()
    for word, number in d.items():
        pq.put((-number, word))

    while not pq.empty():
        print(pq.get())

    mt.end(__name__)


if __name__ == "__main__":
    main()
