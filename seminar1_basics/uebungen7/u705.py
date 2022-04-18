from tools import mytools as mt


def delete(any_list, start, end, verbose=True, ):
    """
    Delete Element from List
    :param any_list:    list to be deleted from
    :param start:       start index             or None
    :param end:         end index (exclusive)   or None
    :param verbose:     show the progress
    :return: None
    """
    if verbose:
        print()
        print(f'start index: {start} : end index: {end}')
        print(f'list before delete: {any_list}')

    del any_list[start:end]

    if verbose:
        print(f'list after  delete: {any_list}')


def main():
    mt.h1("Übung 7.5 - remove List Elements del (Slice)")
    lg = 21
    delete(list(range(lg)), 0, None)
    delete(list(range(lg)), -1, None)
    delete(list(range(lg)), None, 0)
    delete(list(range(lg)), None, 1)
    delete(list(range(lg)), 5, 10)
    delete(list(range(lg)), -10, None)
    delete(list(range(lg)), -10, -5)
    delete(list(range(lg)), 12, 17)

    mt.end(__name__)


if __name__ == "__main__":
    main()
