import functools
import time
import tracemalloc


def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        wrapper.counter += 1
        wrapper.total_time += end - start
        wrapper.total_mem += peak

        return result

    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0

    return wrapper
