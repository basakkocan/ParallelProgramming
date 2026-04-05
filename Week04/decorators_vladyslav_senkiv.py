from functools import wraps
from time import perf_counter
import tracemalloc



def performance(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1

        tracemalloc.start()
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            wrapper.total_time += elapsed
            wrapper.total_mem += peak

    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0
    return wrapper
