custom_power = lambda x=0, /, e=1: pow(x, e)


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the equation (x**a + y**b) / c.
    """

    args = (x, y, a, b, c)

    for value in args:
        if not isinstance(value, int):
            raise TypeError("All arguments must be integers.")

    result = (pow(x, a) + pow(y, b)) / c

    return float(result)


_call_count = 0


def fn_w_counter() -> (int, dict[str, int]):
    global _call_count

    _call_count = _call_count + 1

    counter_info = {__name__: _call_count}

    return _call_count, counter_info
