import sys

# 1. Lambda function
custom_power = lambda x=0, /, e=1: x ** e

# 2. Function with exact reST docstring requirements
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates a custom equation based on the provided parameters.

    :param x: The first base.
    :type x: int
    :param y: The second base.
    :type y: int
    :param a: The first exponent.
    :type a: int
    :param b: The second exponent.
    :type b: int
    :param c: The divisor.
    :type c: int
    :return: The mathematical result of the equation.
    :rtype: float
    """
    return (x ** a + y ** b) / c

# 3. Function tracking state via attributes with strict type hinting
def fn_w_counter() -> tuple[int, dict[str, int]]:
    """
    Tracks the total number of calls and the modules making those calls.
    
    :return: A tuple containing the total call count and a dictionary of callers.
    :rtype: tuple[int, dict[str, int]]
    """
    # Dynamically identify the module calling this function
    caller = sys._getframe(1).f_globals.get('__name__', '__main__')
    
    # Initialize function attributes on the first call
    if not hasattr(fn_w_counter, 'call_count'):
        fn_w_counter.call_count = 0
        fn_w_counter.callers = {}
        
    # Increment the call counters
    fn_w_counter.call_count += 1
    fn_w_counter.callers[caller] = fn_w_counter.callers.get(caller, 0) + 1
    
    return fn_w_counter.call_count, fn_w_counter.callers
