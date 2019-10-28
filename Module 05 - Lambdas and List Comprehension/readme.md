There is one very important aspect to Python that must be understood to successfully be productive.  That is the Lambda.  Lambdas are small anonymous functions.  These a anonymous functions are defined by the *variables* they require and the *expression* that represents the function.  A simple lambda looks as follows

```python
l = lambda n : n * 2
# will print 4
print(l(2))   
```          

When the code above executes l represents a lambda that will double values that it is called with.  It is simple to add more variables to the lambda as demonstrated in the following snippet.

```python
l = lambda a, b, c: a + b + c
print(l(2, 3, 4))       # will print 9
```

You will invariably see lambdas in code that you use and may be tempted to use them in your own.  Some things to keep in mind is that lambdas have a strange and difficult syntax that require that you think in a different manner and provide a really descriptive 'lambda' instead of a function name in any Traceback.  Unless you are writing a framework or working with a framework method that requires them.  

A lot of the time you will find that list comprehensions will replace a lambda fairly well.

# List Comprehensions
A list comprehension is Python syntax to creates a new list from other iterables.  Let's recall the square function that was used earlier to see how list comprehensions can clean up our code

```python
def square(n):
    return n ** 2


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# procedural code
squares = []
for n in numbers:
    squares.append(square(n))

# using map
squares = list(map(lambda x: square(x), numbers))

# list comprehension
squares = [square(n) for n in numbers]
squares = [n**2 for n in numbers]
```

You can also return a list based on the subset of the original list

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [square(n) for n in numbers if n % 2 == 0]
# while print [4, 16, 36, 64, 100]
print(even_squares) 
```    

As can be seen the syntax for list comprehensions my be a little difficult to get a handle on.


|portion|purpose|
|-|-|
|even_squares | the variable that will hold the results of the list comprehension|
|[| marks the beginning of the list comprehension|
|square(n)|the expression to perform on the list |
|for n in numbers| for variable in originating list |
|if n % 2 == 0 | An optional predicate to sort the list|
| ] | marks the end of the list comprehension|

