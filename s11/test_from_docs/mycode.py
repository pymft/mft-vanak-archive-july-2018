def mysum(x, y):
    """
    >>> mysum(1, 2)
    3
    >>> mysum(10, 1.01)
    11.011
    """
    return x + y

if __name__ == "__main__":
    import doctest
    doctest.testmod()