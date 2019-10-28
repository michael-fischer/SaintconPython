# Decorators (move to another section????)
Extended functionality made extremely easy in Python.  Decorators are a special from of functions that can wrap other functions to 'extend' the functionality of the method.   They follow a simple formula as shown below.

```python
# Decorator example
def my_decorator(func):
    def wrapper():
        print("We are able to add code before the function.")
        func()
        print("We are able to add code after the function.")
    
    return wrapper

def my_function():
    print('Hello World!')

my_function = my_decorator(my_function)
my_function()

# The output of executing this is:
# We are able to add code before the function.
# Hello World!
# We are able to add code after the function.
```

But wait, how is this decorating anything.  You caught me. What is happening in the code above is that we are seeing that functions can be passed as parameters in methods.  There is one minor change that needs to be done to our example above that we will see in some demos later. For your convenience it is included in the [Decorator template](decorator_template.py). What makes it a decorator is that Python add some syntactic sugar.  

Let us take a second to think about the code above.  Tbe `my_decorator()` function defines an inner function called `wrapper()` and simply returns it.  So we have the ability to return a function from a function in Python.  The line `my_function = my_decorator(my_function)` shows that we can pass a function as a parameter.  `my_function` is passed into the `my_decorator` function and then used within the inner `wrapper` function.  This is because we have defines a *closure*.  A closure is a way to define a function that remembers the enclosing scopes.  There are 3 criteria that has to be meet to define a closure.

1. A function must be nested within another function
2. The nested function must refer to a value defined in the enclosing function
3. The enclosing function must return the nested function

The following code is the same as the previous but using the decorator syntax instead.

```python
# Decorator example
def my_decorator(func):
    def wrapper():
        print("We are able to add code before the function.")
        func()
        print("We are able to add code after the function.")
    return wrapper

@my_decorator
def my_function():
    print('Hello World!')

my_function()

# The output of executing this is:
# We are able to add code before the function.
# Hello World!
# We are able to add code after the function.
```

Our earlier example was a bit simplified and we have to do a little bit of extra work to decorate functions that take parameters.  The [Decorator template](Decorator_template.py) already includes these additions but we need to add *args and **kwargs to the wrapper function and then pass those along to the original function.

```python
# Decorator example
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("We are able to add code before the function.")
        func(*args, **kwargs)
        print("We are able to add code after the function.")
    return wrapper

@my_decorator
def my_function():
    print('Hello World!')

my_function()
```

Things get really interesting if you want to pass parameters into your decorator.  We have to add another layer in our wrapper functions.  Consider the following decorator that will allow us to specify an arbitrary multiplier for the results of the function.

```python
# Decorator with parameters example
    def outer_wrapper(multiplier):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            return multiplier * func(*args, **kwargs)
        return wrapper

    return my_decorator

@outer_wrapper(multiplier=4)
def add(x, y):
    return x + y

print (add(2,3))        # This will print 20.
```

More decorators can be found on the [internet](https://github.com/lord63/awesome-python-decorator) and the sky is the limit for developing your own. 

# Scripts 
Now that we have a basic understanding of all the components in the Python environment lets look at the most basic concept - a script.   In reality, nothing more than a module.  When a python script is executed from the command line or imported it begins executing code one line at a time.  The script continues to execute until the end of the script is reached and the script exits.  

This is true un less something happens to short circuit the program.  This could be an error being raised and not caught or a call to `sys.exit()` which will cause the program to terminate.



