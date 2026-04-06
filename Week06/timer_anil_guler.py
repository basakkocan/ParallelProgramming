import time
from functools import wraps

class Timer:
    def __init__(self, name="Kod Bloğu"):
        self.name = name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.perf_counter()
        execution_time = end_time - self.start_time
        
        print(f"--- {self.name} ---")
        print(f"Süre: {execution_time:.6f} seconds.")
        print("-" * (len(self.name) + 8))

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with Timer(name=func.__name__):
                return func(*args, **kwargs)
        return wrapper
