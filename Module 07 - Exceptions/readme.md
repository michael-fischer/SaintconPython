# Error and Exceptions
Computer programs may run into problems from both errors and exceptions.  Errors are conditions that occur in programs that should not be recovered from.  The most likely error that you will see in Python is a SyntaxError.  However, a good Integrated Development Environment (IDE) will help identify those for you during the development process.   
 
Exceptions, on the other hand, can be recovered from.  Exception handling in Python is more verbose than you might have seen in other languages with the addition of an optional else clause that is executed if no exception occurred during the *try* block.  The format of the *try* block is fairly simple.

```python 
# example of the python exception handling construct
try:
    # execute some code that could raise an exception
except:
    # this code is executed if an exception occurs
    pass
else:
    # this code is executed if the try block is executed without exception
    pass
finally:
    # this code is executed after the try block, any exception block OR the else block
    pass
```

Rumor has it that the purpose of the else clause is that exception handling is more common in Python than other languages.  It does make the code a little easier as the code in the else would otherwise need to be included in the try block after whatever line could have caused an exception.

It is also possible to *raise* an exception to signify that an exceptional condition has occurred. This allows the developer to control the flow of the program if necessary. Raising Exceptions have changed between Python 2 and 3 so we will only see the syntax for Python 3.  

```python
# demo of raising an exception
raise Exception('This is my exception')

# Will produce the following Traceback - aka StackTrace
# Traceback (most recent call last):
#  File "scratch.py", line 1, in <module>
#    raise Exception('This is my exception')
#Exception: This is my exception
```

One thing that you want to be careful about is hiding important details from an error.  The following will allow you to keep visibility into the original issue.

```python
# demo of raising an exception
try:
    x = 5 / 0
except Exception as e:
    print('something went wrong: \n' + str(e))
finally:
    print('we made it to the end')
```

In addition, starting with Python 3 you can have Exception chaining.

```python
# demo of raising an exception
try:
    x = 5 / 0
except Exception as e:
    raise Exception('Something went wrong') from e
```

The Traceback changes a little when exceptions are chained.

![Exception Chaining](exception_chaining.png)

## Creating your own Exception class to raise.

```python
class CustomError(Exception):
    pass
```
