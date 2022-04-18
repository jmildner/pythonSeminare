from tools import mytools as mt


def delete(any_list, idx, verbose=True, ):
    """
    Delete Element from List
    :param any_list: list to be deleted from
    :param idx: index of the element to be deleted
    :param verbose: show the progress
    :return: None
    """
    if verbose:
        print()
        print(f'index to delete: {idx}')
        print(f'list before delete: {any_list}')

    del any_list[idx]

    if verbose:
        print(f'list after  delete: {any_list}')


def main():
    mt.h1("Übung 7.4 - remove List Elements del")
    lg = 21
    delete(list(range(lg)), 0)
    delete(list(range(lg)), 5)
    delete(list(range(lg)), -1)
    delete(list(range(lg)), -2)
    delete(list(range(lg)), -3)
    delete(list(range(lg)), 15)
    delete(list(range(lg)), 12)
    delete(list(range(lg)), -5)
    delete(list(range(lg)), lg - 5)

    
    mt.end(__name__)



if __name__ == "__main__":
    main()
