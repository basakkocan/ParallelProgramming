custom_power = lambda x=0, /, exp=1: x ** exp


def custom_equation(x: int = 0, y: int = 0, /,
                    a: int = 1, b: int = 1, *,
                    c: int = 1) -> float:
    """
    Calculates (x^a + y^b) / c

    :param x: positional only, default 0
    :param y: positional only, default 0
    :param a: positional or keyword, default 1
    :param b: positional or keyword, default 1
    :param c: keyword only, default 1
    :return: float result
    """
    return (x ** a + y ** b) / c


def fn_w_counter() -> tuple[int, dict[str, int]]:
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = 0

    fn_w_counter.counter += 1
    return fn_w_counter.counter, {__name__: fn_w_counter.counter}
