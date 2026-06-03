import functools
import time
import tracemalloc

class PerformanceDecorator:
    def __init__(self):
        self.counter = 0
        self.total_time = 0
        self.total_mem = 0
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.counter += 1
            
            # Track time
            start_time = time.time()
            
            # Track memory
            tracemalloc.start()
            result = func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            # Update metrics
            self.total_time += time.time() - start_time
            self.total_mem = max(self.total_mem, peak)
            
            return result
        return wrapper

performance = PerformanceDecorator()
