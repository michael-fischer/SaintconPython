import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("We are able to add code before the function.")
        func(*args, **kwargs)
        print("We are able to add code after the function.")

    return wrapper
