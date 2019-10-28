 
# Welcome

# A Bunch of Useful Terms 
| Term | Definition |
| - | - |
| variable | A variable is just a named memory location that points to an object |
| function | A set of statements that are grouped to gather to enable reusability |
| object | An object is an instance of a class.  Simply put it is a reference to the  |
| class | A class is a template for an object.  It defines the functions and properties that describe an objects behavior.  |
| module | A python file that contains one or more function which as intended for reuse. |
| package | A directory that contains Python module(s). The directory should contain an __init__.py which can have any or no implementation.
| library | Sometimes used to describe a package but for the purposes of this tutorial it will mean the Python standard library. |
| Iterator | An object that enables a programmer to traverse a container, particularly lists. |

# Comments
Not very useful in the interactive shell but in code a useful in scripts to convey the developers intention.  A comment is started by typing the \# character.

  *Many online sources will tell you that you can create a multiline comment by using either ''' or """ to mark the beginning and end of the line.  This is just **wrong**. What this really does is create a multiline string.  Since the string is not used it kind of works - but it is loaded into memory.  Indeed some magic happens to create Docstrings (more omn that later) through the use of multiline comments*   If it is the first line of a module, function, class, or method it becomes the __doc__ for the object.

# Basic Data Types
| Type | Description | Notes |
|-----| ----| ----|
| str | Represents a string of literal characters | msg = 'hello world' |
| bool | used to represent True (1)  or False (0) | done = True or done = bool(1) |
| int | A whole number | x = 5 |
| float | A fractional number | pi = 3.14159265359 |
| tuple | A sequence of immutable Python objects. Similar to lists but cannot be changed. | Top10 = ('Injection', 'Broken Authentication','Sensitive Data Exposure', ...) |
| list | A sequence of mutable Python objects. | Top10 = ['Injection', 'Broken Authentication','Sensitive Data Exposure', ...] |
| range | An immutable sequence based on the values passed during initialization. | range(1,10) |
| set | A sequence of unique Python objects. | Top10 = set(['Injection', 'Broken Authentication','Sensitive Data Exposure', ...]) |
| dictionary | A collection of key:value pairs | dict = ['Key':'Value', 'Name': 'Bob'] |
| file | An object that represents a file | file = open('filename', 'r') |

# Python naming conventions
*straight from the [Python documentation](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)*

 1. General

    * Avoid using names that are too general or too wordy. Strike a good balance between the two.
    * Bad: data_structure, my_list, info_map, dictionary_for_the_purpose_of_storing_data_representing_word_definitions
    * Good: user_profile, menu_options, word_definitions
    * Don’t be a jackass and name things “O”, “l”, or “I”
    * When using CamelCase names, capitalize all letters of an abbreviation (e.g. HTTPServer)

1. Packages
   * Package names should be all lower case 
   * When multiple words are needed, an underscore should separate them
   * It is usually preferable to stick to 1 word names

2. Modules
   * Module names should be all lower case
   * When multiple words are needed, an underscore should separate them
   * It is usually preferable to stick to 1 word names

3. Classes
   * Class names should follow the UpperCaseCamelCase convention
   * Python’s built-in classes, however are typically lowercase words
   * Exception classes should end in “Error”

4. Global (module-level) Variables
   * Global variables should be all lowercase
   * Words in a global variable name should be separated by an underscore

5. Instance Variables
   * Instance variable names should be all lower case
   * Words in an instance variable name should be separated by an underscore
   * Non-public instance variables should begin with a single underscore
   * If an instance name needs to be mangled, two underscores may begin its name

6. Methods
   * Method names should be all lower case
   * Words in an method name should be separated by an underscore
   * Non-public method should begin with a single underscore
   * If a method name needs to be mangled, two underscores may begin its name

7. Method Arguments
    * Instance methods should have their first argument named ‘self’.
    * Class methods should have their first argument named ‘cls’

8. Functions
    * Function names should be all lower case
    * Words in a function name should be separated by an underscore

9.  Constants
    * Constant names must be fully capitalized
    * Words in a constant name should be separated by an underscore

# Creating objects
Creating objects is simple in Python.  You create a variable and assign it the value.  Some examples you have already seen.

```python
# Creates a variable called x and stores the integer 5 in it.
x = 5                   

# Creates a variable named pi and stores the decimal value 3.14 in it.
pi = 3.14        

# Create a variable named pi and stored the string value 'hello world' in it.
msg = 'hello world'
```

# learning about objects
One of the neat things about Python and it being an interpreted language is the ability for introspection of objects.  This is particularly useful if you are in the interactive shell.  Some useful functions for introspection include *help()*, *dir()* and *type()*.

**help()** - given a object will describe the object by displaying the Docstrings associated with the object and the methods contained within.

***Example***
    >>> help(str)

    Help on class str in module builtins:

    class str(object)
    |  str(object='') -> str
    |  str(bytes_or_buffer[, encoding[, errors]]) -> str
    |  
    |  Create a new string object from the given object. If encoding or
    |  errors is specified, then the object must expose a data buffer
    |  that will be decoded using the given encoding and error handler.
    |  Otherwise, returns the result of object.__str__() (if defined)
    |  or repr(object).
    |  encoding defaults to sys.getdefaultencoding().
    |  errors defaults to 'strict'.
    |  
    |  Methods defined here:
    |  
    |  __add__(self, value, /)
    |      Return self+value.
    |  
    |  __contains__(self, key, /)
    |      Return key in self.
    |  
    |  __eq__(self, value, /)
    |      Return self==value.
    :

help() can also be called on the methods of an object as well to retrieve the Docstring about that method.

    help(str.isalpha)
    Help on method_descriptor:

    isalpha(self, /)
        Return True if the string is an alphabetic string, False otherwise.
    
        A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

**type()** - given an object, it will return the type of the object as represented by the \_\_name\_\_ attribute on the object

***Example***

    >>> type('hello class')
    <class 'str'>
    >>>

**dir()** - given an object, it will return the methods and attributes of the object.

***Example***

    >>> dir(str)
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    >>> 

Note: we will learn more about **magic methods** as the day progresses.   For now the only important thing to know is that the start and end with double underscores.  You may also hear them referred to a **dunder** methods.  This is not a reference to the Dunder Mifflin Paper company but double underscore.  It is usually used when communicating a magic methods by name as "dunder" rolls of the tongue easier.

# Getting data from users
To read information from them keyboard we want to use the `input()` function. If you type `input()` at the interactive command prompt you will notice that the cursor will move to the next line and simply wait.  It is waiting for characters to be entered from the keyboard and the enter key to be pressed.  Once the enter key is pressed it will be echoed back to you in quotes.

    >>> input()
    hello
    'hello'
    >>>

You can customize a hint for the input command.

    >>> input('what is your name? ')
    What is your name? Bob
    'Bob'
    >>> 

Those that are pay attention to detail will have noticed a couple of things.

1. There is an space added after the ? mark.  The whole purpose of this is simply to make the input line a little prettier.
2. When the output is echoed back it is in quotes.  When `input()` returns it will return a string.  We will learn how to convert this shortly.

To store the results for later use you would want to store the value in a variable.

    >>> name = input('what is your name? ')
    What is your name? bob
    >>>

You can check the value of the variable.

    >>>name
    'Bob'
    >>>type(name)
    <class 'str'>



