import inspect

custom_power = lambda x=0, /, e=1: float(x ** e)

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates a custom equation: (x**a + y**b) / c.

    :param x: The first base (positional-only).
    :param y: The second base (positional-only).
    :param a: The first exponent (positional-or-keyword).
    :param b: The second exponent (positional-or-keyword).
    :param c: The divisor (keyword-only).
    :return: The result of the equation as a float.
    """
    return float((x ** a + y ** b) / c)

def fn_w_counter() -> tuple[int, dict]:
    if not hasattr(fn_w_counter, 'total_calls'):
        fn_w_counter.total_calls = 0
        fn_w_counter.callers_dict = {}
    
    fn_w_counter.total_calls += 1
    
    frame = inspect.currentframe().f_back
    caller_name = frame.f_globals.get('__name__', 'unknown')
    
    fn_w_counter.callers_dict[caller_name] = fn_w_counter.callers_dict.get(caller_name, 0) + 1
    
    return fn_w_counter.total_calls, fn_w_counter.callers_dict
