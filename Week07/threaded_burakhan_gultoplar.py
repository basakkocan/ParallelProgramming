import threading
from functools import wraps

def eszamanli_calistir(thread_sayisi: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            is parçacıkları = [
                threading.Thread(target=func, args=args, kwargs=kwargs)
                for _ in range(thread_sayisi)
            ]
            
            for t in is_parçacıkları:
                t.start()
                
            for t in is_parçacıkları:
                t.join()
                
        return wrapper
    return decorator
