custom_power = lambda x=0, /, e=1: x**e


def custom_equation(
    x: int = 0,
    y: int = 0,
    /,
    a: int = 1,
    b: int = 1,
    *,
    c: int = 1,
) -> float:
    """
    Calculate a custom equation.

    :param x: First base value.
    :param y: Second base value.
    :param a: Exponent for x.
    :param b: Exponent for y.
    :param c: Divisor value.
    :returns: The result of (x**a + y**b) / c.
    """
    return float((x**a + y**b) / c)


def fn_w_counter() -> tuple[int, dict[str, int]]:
    """Count total calls and calls grouped by this module name."""
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.caller_counts = {}

    module_name = __name__

    fn_w_counter.total_calls += 1
    fn_w_counter.caller_counts[module_name] = (
        fn_w_counter.caller_counts.get(module_name, 0) + 1
    )

    return fn_w_counter.total_calls, dict(fn_w_counter.caller_counts)
