# 14 lines: Doctest-based testing


import doctest


def median(pool):
    """Statistical median to demonstrate doctest.

    >>> median([2, 9, 9, 7, 7, 2, 5, 4, 8])
    6 change to 7 in order to pass the test
    """

    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2


if __name__ == '__main__':
    doctest.testmod()
