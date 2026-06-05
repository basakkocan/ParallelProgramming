def awaitme(func):
    """A decorator that allows the decorated function to be called with 'await' syntax, enabling asynchronous behavior."""
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    return wrapper