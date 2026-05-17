import inspect

# 1. custom_power
# A lambda function returning a float[cite: 807, 808].
# It takes positional-only parameter x (default 0) and positional-or-keyword parameter e (default 1)[cite: 809, 810, 812, 813, 814].
custom_power = lambda x=0, /, e=1: float(x**e)


# 2. custom_equation
# A function returning a float with 5 integer parameters[cite: 808, 811].
# x and y are positional-only (default 0)[cite: 811, 812].
# a and b are positional-or-keyword (default 1), c is keyword-only (default 1)[cite: 816].
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates a custom equation based on the provided parameters.

    :param x: First positional-only parameter.
    :type x: int
    :param y: Second positional-only parameter.
    :type y: int
    :param a: First positional-or-keyword parameter.
    :type a: int
    :param b: Second positional-or-keyword parameter.
    :type b: int
    :param c: Keyword-only parameter.
    :type c: int
    :return: The result of the equation (x**a + y**b) / c.
    :rtype: float
    """
    return float((x**a + y**b) / c)


# 3. fn_w_counter
# Returns a tuple of an int (total calls) and a dictionary (caller tracking)[cite: 819, 820].
def fn_w_counter() -> tuple[int, dict[str, int]]:
    # Initialize function attributes if they don't exist yet
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.caller_counts = {}

    fn_w_counter.total_calls += 1

    # Inspect the stack to find the caller's __name__
    frame = inspect.currentframe().f_back
    caller_name = frame.f_globals.get("__name__", "unknown")

    # Update the caller dictionary [cite: 821]
    if caller_name not in fn_w_counter.caller_counts:
        fn_w_counter.caller_counts[caller_name] = 0
    fn_w_counter.caller_counts[caller_name] += 1

    return fn_w_counter.total_calls, fn_w_counter.caller_counts
