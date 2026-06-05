import asyncio
from functools import wraps

def awaitme(fn):
    """A decorator that turns any function into a coroutine."""
    
    if asyncio.iscoroutinefunction(fn):
        return fn

    @wraps(fn)
    async def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
      
        if asyncio.iscoroutine(result):
            return await result
            
        return result

    return wrapper
