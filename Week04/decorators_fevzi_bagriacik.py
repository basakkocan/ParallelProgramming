import time
import tracemalloc
from functools import wraps

class performance:
    def __init__(self, func):
        self.func = func
        self.counter = 0
        self.total_time = 0.0
        self.total_mem = 0
        
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()

        result = self.func(*args, **kwargs)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.counter += 1
        self.total_time += (end_time - start_time)
        self.total_mem += peak

        return result
