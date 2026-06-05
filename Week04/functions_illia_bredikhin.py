custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(
    x: int = 0,
    y: int = 0,
    /,
    a: int = 1,
    b: int = 1,
    *,
    c: int = 1
) -> float:
    """
    Custom equation.

    :param x: first integer
    :param y: second integer
    :param a: power of x
    :param b: power of y
    :param c: divisor
    :return: calculated result
    """
    for value in (x, y, a, b, c):
        if not isinstance(value, int):
            raise TypeError("All values must be integers")

    return (x ** a + y ** b) / c


_counter = 0


def fn_w_counter() -> (int, dict[str, int]):
    global _counter

    _counter += 1
    return _counter, {__name__: _counter}
