import sys

# 1. Lambda function with positional-only and positional-or-keyword arguments
custom_power = lambda x=0, /, e=1: x ** e

# 2. Function with strict argument rules, type hints, and a reST docstring
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates a custom equation based on the provided parameters.

    :param x: First base (positional-only)
    :param y: Second base (positional-only)
    :param a: First exponent (positional-or-keyword)
    :param b: Second exponent (positional-or-keyword)
    :param c: Divisor (keyword-only)
    :return: The result of the calculation as a float
    """
    return float((x ** a + y ** b) / c)

# 3. Function that tracks its own calls and callers using function attributes
def fn_w_counter() -> tuple:
    # Get the name of the file/module that called this function
    caller = sys._getframe(1).f_globals.get('__name__', '__main__')
    
    # Initialize attributes if they don't exist yet
    if not hasattr(fn_w_counter, 'total_calls'):
        fn_w_counter.total_calls = 0
        fn_w_counter.callers = {}
        
    # Update the counters
    fn_w_counter.total_calls += 1
    fn_w_counter.callers[caller] = fn_w_counter.callers.get(caller, 0) + 1
    
    return fn_w_counter.total_calls, fn_w_counter.callers
