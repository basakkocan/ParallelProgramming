import time
import tracemalloc

def performance(func):
    """
    A decorator that measures and tracks the performance of decorated functions.
    
    Attributes:
        counter (int): The number of times the decorated function has been called.
        total_time (float): The cumulative execution time (in seconds) of all calls.
        total_mem (int): The cumulative memory usage (in bytes) of all calls.
    Args:
        func (callable): The function to be decorated.
    Returns:
        callable: A wrapper function that executes the original function while tracking performance metrics
    """
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        performance.counter += 1
        performance.total_time += (end_time - start_time)
        performance.total_mem += current

        return result

    # Initialize attributes here, inside the decorator, not globally
    if not hasattr(performance, 'counter'):
        performance.counter = 0
        performance.total_time = 0.0
        performance.total_mem = 0

    return wrapper
