import queue
from tools import mytools as mt


def main():
    mt.h1("Übung 7.10 - Queue")

    q = queue.Queue()
    q.put("Hallo")
    q.put("Welt")

    while not q.empty():
        print(q.get())

   
    mt.end(__name__)



if __name__ == "__main__":
    main()
