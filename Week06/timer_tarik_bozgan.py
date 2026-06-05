import time as t

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = t.time()
        return self

    def __exit__(self, *args):
        self.end_time = t.time()