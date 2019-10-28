import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    # soource: very similar to https://realpython.com/primer-on-python-decorators/
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()    
        result = func(*args, **kwargs)
        end_time = time.perf_counter()      
        elapsed = end_time - start_time    
        print(f"{func.__name__!r}: {elapsed:.4f} secs")
        return result
    return wrapper

def debug(func):
    """Print the function signature and return value"""
    # source: https://realpython.com/primer-on-python-decorators/
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
        signature = ", ".join(args_repr + kwargs_repr)           
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           
        return value
    return wrapper_debug

def slow_down(func):
    """Sleep 1 second before calling the function"""
    # source: https://realpython.com/primer-on-python-decorators/
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down