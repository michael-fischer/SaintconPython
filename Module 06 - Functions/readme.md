# Welcome

Now it is time to start thing about making our scripts more reusable.  In this module we will look at Functions, Classes, Modules, and Libraries.  Before we started on those we will want to look into Scope and how it affects variables.  

# Scope
Scope is also referred to as namespace.  Scope is simply a container for mapping names to objects whether they are variables, functions, or classes.  There are four scopes within a Python program.  These are local, enclosing, global, and built-in.  

Scope is defined in a hierarchy search order where if a variable cannot be found in the local scope, the enclosing scope will be searched.  Next, the the global namespace will be searched and finally the built-in scope.  If a variable name was not found any an scope a NameError exception will be raised.

Modules also provide another level of scope, but more on that later.

## local
Variables that are defined within a function or a class method are local in scope.  Local variables can only be accessed within the function that they are defined in.  If you try to access a local variable outside the scope that it is defined the script will raise a NameError.  ex: NameError: name 'x' is not defined.

## enclosing
Enclosed can be the enclosing function. For instance if a function was defined within another function.

## global
Variables that are defined outside of a class or function are said to be in the global scope.  They are global to the level of the executing script.

These variables can be access from anywhere.  While this sounds powerful but it is a double edged sword.  If the variable is mutable it can also be changed by anywhere as well.  Global variables should be used with caution or not at all any anything beyond trivial scripts. 

## Built-in Scope
These are variables that are predefined in Python.

## Putting it all together
Let's take a quick look at how this works by running `python3 local_scope.py` in the terminal and examining the results.

![Local Scope Results](local_scope_results.png)

See how the `global` keyword allowed us to change the value in third() and the value

# Functions
Functions simply allow you to create small reusable sections of code.  They are customizable through the use of parameters and have the ability to return results if desired.

Functions are defined by the _def_ keyword, followed by the name of the function and some parameters and a colon.  In the most basic form you have:

```python
def my_function():
    pass        # the pass keyword is a dummy place holder that can be used if
                # the syntax of a construct requires a statement but no action is desired
```
                    

## Parameters
You can do a lot with functions without taking user input.  However, by adding parameters it becomes possible to make functions dynamic.  Without parameters, functions can only do the exact same thing over and over.

```python
def say_hello(name):
    print(f'Hello {name}!  How are you?')

say_hello('Bob')
```

In other languages parameters are either passed by reference or passed by value.  Python takes another approach and parameters are passed by assignment.  Everything in Python is an object.  Objects can either be mutable or immutable.  Immutable types include bool, int, float, tuple, and string.  Mutable types ae list, set, and dict.    

```python
# Demonstration of immutability in Python
def func(num):
    num = 7
    print(id(num))          # This will print the same identifier 140405731523368
    print(num)              # This prints 7 since num was assigned 7 previously

x = 5
print(id(x))                # This will print some identifier such as 140405731523368
func(x)
print(x)                     # This is still 5 after the function returns 
```    

### Advanced usage of function parameters
There is a special syntax that allows you to pass in a variable number of parameters into a python method.  One option is _*args_ and the other is _**kwargs_.  _*args_ allows a variable number of arguments into a method.

```python
def dynamic_args(*args):
    for arg in args:
        print(arg, end = " ")

dynamic_args("Welcome", "To", "Python")
# This will print "Welcome To Python"
```

The other syntax, _**kwargs_ allows for a variable length of key and value pairs which will be passed into the function as a dictionary.

```python
def dynamic_kwargs(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print ("%s == %s" % (key, value))

dynamic_kwargs(first ='Welcome', mid ='To', last='Python')

# This will print
# 
# first == Welcome
# mid == To
# last == Python
```

But wait!  There is more.  if you buy now you can use this format for input as well.  Consider the following code.

```python
def standard_function(arg1, arg2, arg3):
    print(f'arg1: {arg1}\targ2: {arg2}\targ3: {arg3}')

tuple_args = ('Welcome', 'To', 'Python')
dictionary_args = {"arg1": 'Welcome', "arg2": 'To', "arg3": 'Python'}

standard_function(*tuple_args)              # Will print "arg1: Welcome	arg2: To	arg3: Python"
standard_function(**dictionary_args)        # Will print "arg1: Welcome	arg2: To	arg3: Python"
```

The caveat is that in either case it is important that the parameters match.  In the first case, you need to have the exact number of parameters in the iterable that the function expects or you will receive a *TypeError*.  You will also receive a *TypeError* in the keyword variation if the collection contains an unexpected key value or is missing one. Although, interesting things can happen if you use this convention both to call the function and as the parameters.

For the most basic data types this can be problematic if you need to make changes to the values that have come in.  One of the favorite tricks that I learned back in my undergraduate tricks is something similar to the following.

```python
x = 5 
y = 6

x = x ^ y
y = x ^ y
x = x ^ y

print(x,y)      # This will print 6 5
```

This neat little trick could be modularized, if integer values were not immutable.

```python
# Sadly this will not work the way we want it to since
# integers are immutable in Python
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
x = 5
y = 6

swap(x, y)
print(x,y)      # Rats, x and y are still 5 and 6
```

Since we can't change the input since it is immutable.  Let's take a look at return values and come back to this.   
    
## Return Values
Returning a method is as simple as specifying a value using the return keyword proceeding what should be returned.   

Let's take a look with a simple function to sum values:

```python
def sum(a, b):
    return a + b

x = 5
y = 6

print(sum(x,y))             # prints 11
```

The return value can be any valid Python expression.  In actuality, Python methods without a return statement in them will return a default value of None.  Let's consider this ill formed Python function

```python
# This method does not behave correctly
def is_even(num):
    if num % 2 == 0: 
        return True

print(is_even(4))           # This will return True which we expect
print(is_even(5))           # This will return None which is probably not what we expect
```

How should we fix this?  We need to make sure that all return paths return a value.  There are a couple of ways that we can do this.  First, by completing the original method

```python
def is_even(num):
    if num % 2 == 0: 
        return True
    else: 
        return False
```

or a slightly cleaned up version.

```python
def is_even(num):
    return num % 2 == 0
```

In both cases, this will return 

```python
print(is_even(4))           # This will return True 
print(is_even(5))           # This will return False
```

Now we will revisit our swap method thinking about a return value now.

```python
# Okay this version works but 
# we will see it is rather silly
# in a second.
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b, 5

x = 5
y = 6
x, y = swap(x, y)
print(x,y)   
```   

This is an interesting aspect of Python.  The ability to return multiple results without packaging it in another construct.  It is automatically bound into a tuple and you can unpack it on the receiving end.  This is what would have been returned if only one one variable was defined on the left hand side of the function call.

But what is the better way?

```python
# Better way
def swap(a, b):
    return b, a

x = 5
y = 6
x, y = swap(x, y)
print(x,y)
```


# Classes
A python class is a template for putting together objects within Python.  Object oriented programing is a class all on its own but we will keep well known object oriented principles in mind.  Objects have attributes and functionality associated with it.  Classes are defined by the *class* keyword followed by the name of the class and a colon.  By convention, classnames start with an uppercase name.  

```python
class Point:
    x = 0
    y = 0

# instantiating an object
point = Point()

print(point.x, point.y)

point.x = 5
point.y = 7

print(point.x, point.y)
```
            
Now we have an object with the ability to set the values for the x and y properties we defined. OO aficionados will scream that this breaks encapsulation.  It is important to remember that classes are mutable in Python.  The concept of private member variables is difficult but not impossible to achieve.  However, that is a discussion for a later [topic](http://www.blog.pythonlibrary.org/2014/01/17/how-to-create-immutable-classes-in-python/).

Adding a constructors

```python
def __init__(self, x, y):
    self.x = x
    self.y = y
```

This is a little more object oriented bit the internal x, y are still accessible from an instance of the class.

# Modules
A python module allows you to organize Python code.  However, you already know how to make a Python module.  It is any file that contains Python code, whether it be script, function, class or combination thereof.  A python module is defined by the name of the module.py.  For example, the module Saintcon would be in the file saintcon.py.  To use the module you need to the import statement.  

Let's create a file named sequences.py

```python
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 

def squares(n):
    return n**n


def triangles(n):
    return n(n +1)/2
```

We can test this module with another file.

```python
import sequences

print('Fibonacci\n')
for x in range(10):
    print(x, sequences.fibonacci(x))

print("Squares\n")
for x in range(10):
    print(x, sequences.squares(x))

print("Triangles\n")
for x in range(10):
    print(x, sequences.triangles(x))
```