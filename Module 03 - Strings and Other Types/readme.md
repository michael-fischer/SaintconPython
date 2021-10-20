
# Welcome
This section focuses mainly on strings and other sequences in Python in Python.  Like ranges and tuples, the string is represented as an immutable sequence.  Inside the Python documentation this is referred to as the text sequence type.  As such many of the sequence operations that you use will work on strings as well.

# Strings
In Python a string is an immutable sequence of characters.

## Creating strings

```python
# strings can be created using single or double quotes.
msg = 'This is a string'

#  multiline strings
msg = """This is a string
    that spans multiple lines"""
```

## Common operations on strings [and other sequences]

| Operation | Example | Result |
|:-:|:-:|:-:|
| in | x in s| True if x is contained within s |
| not in | x not in s | False if x is contained within s |
| + | s + t | will concatenate s and t |
| * | s * n or n * s| will add s to itself n times |
| len | len(s) | will return the length of s |
| min | min(s) | the minimum value of s.  Might not be too terribly useful on a string |
| max | max(s) | the maximum value of s.  Might not be too terribly useful on a string |
| chr | chr(n) |Converts an integer to a string |
| str | str(0) | returns a string representation of an object |


# Common string methods
Complete documentation of strings can be found at in the [Python Documentation](https://docs.python.org/3.7/library/stdtypes.html#string-methods).

| Operation | Example | Result |
|:-:|:-:|:-:|
| index | s[i] | will return the ith item in s |
| slice | s[i:j] | returns a *slice* of s starting at index i and up to but not including j|
| stride | s[i:j:j] | returns a *slice* of s starting at index i and up to but not including j stepping by k |
| index | s.index[x[, i[, j]]] | index of the first occurrence of x in s (at or after index i and before index j) |
| count | s.count(x) | total number of occurrences of x in s |
| encode | s.encode('utf-8') | returns a UTF-8 formatted version of s.  This will return a bytes array that can be transformed back with the bytes.decode() method |

Since strings are immutable there are some things that you could do in other languages that wont work in Python.  For example:

```python
msg = 'hello world'
char = msg[0]       # this will return 'h'
msg[0] = 'H'        # this will throw TypeError: 'str' object does not support item assignment
```

Instead you have to use *string.replace()* to make changes. This method will create a new string from the existing string while applying the specified changes.

```python
msg = 'Hello world'
```
      
*Note* another option is to turn it into a list of characters, modify the list, and then change it back into a string.

```python
msg = "hello world"
chars = list(msg)
chars[0] = 'H'
msg = "".join(chars)  
```          

## building strings
There are multiple ways to to format strings in Python.  

```python
# The manual way
num = 5
msg = "This song is " + str(num) + " words long"

# a slightly more annoying way
msg = "This song in", num, " words long"

# Can you believe a third, slightly better way
msg = "This song in %s words long" % num

# And even a fourth
msg = "This song is {} words long".format(num)

# Now string interpolation in Python 3.6+
msg = f"this song is {num} words long"
```

sting.format() is was what was vogue when I started to learn Python.  However, you got to admit it is cool to have to deal with f-strings. Okay, so that really stands for Formatted String Literal.

*s.lower()* and *s.upper()& return the lowercase or upper case of a string

```python
msg = 'hELLO wORLD!'
msg = msg.lower()           # 'hello world!'
msg = msg.upper()           # 'HELLO WORLD!'
# Bonus
msg = msg.capitalize()      # 'Hello world!'
```

*s.strip()* - will return a string with whitespace removed from the beginning and end.

```python
msg = "          SAINTCON IS LIVE AGAIN          "

left = msg.lstrip()     
right = msg.rstrip()
full = msg.strip()


print(left)         # "SAINTCON IS LIVE AGAIN          "
print(right)        # "          SAINTCON IS LIVE AGAIN"
print(full)         # "SAINTCON IS LIVE AGAIN"
```

*s.split('delim')* will take a string and convert it to a list based on the specified delimiter.  *s.split()* will split a string based on all whitespace.

```python
msg = '1,2,3,4,5,6,7,8,9,10'
numbers = msg.split(',')     

# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# But note that they are still strings.  We will learn ways to convert but...
```

*s.join(list)* is the opposite of split().  It will take a list and join it together based on the value of the string as a delimiter.  Common values for the string are an empty string 
(""),  a space (" "), and a comma (",") but it would be anything.

```python
words = ["How", "Are", "You", "Today?"]
msg = " ".join(words)       # "How Are You Today?"
```

But it has to be strings.  We will learn how to work with that later.

# List
A list is a mutable collection that is ordered and can be modified. Creation of a list is done with square brackets

```python
# creating an empty list
l = []

# creating a list with values
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

lists are also accessed using square brackets.  This is a 0 based index so [0] will return the first item, [1] will return the second.  Python is different than the majority of other languages as it will also allow you to index via a negative number and start at the back of the list.  This means that [-1] will return the last element in the list.

```python
# accessing a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = l[0]            # sets a to the first element: 1
b = l[4]            # set b to the fifth element in the list: 5
c = l[-1]           # sets c to the last element in the list: 10
d = l[-3]           # sets d to to the third to last element in the list: 8 
```

Finally, it is possible to slice a list as you would a string.

```python
# accessing a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sublist = l[1:4]        #returns a list of [2, 3, 4]
sublist = l[1:9:2]      # returns a list of [2, 4, 6, 8]
sublist = l[::-1]       # returns the list in reverse [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

As mentioned, a list can be modified.  We have seen accessing a list by indexing it on the right hand side of the equal sign.  To modify it you assign a value to the position by indexing it on the left hand side of an equest sign.  Here is an example that will double all the values in a list.

```python
# accessing a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(l)

for x in range(length):
    l[x] = l[x] * 2

print(l)            # prints the updated list: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

It is also possible to add and remove items for the list.  

```python
# accessing a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l.pop()             # removes the last item from the list
l.pop(1)            # removes the second item from the list
print(l)            # prints [1, 3, 4, 5, 6, 7, 8, 9]
```


# Tuple
Tuples are similar to list except where a list can be modified a tuple is read only. Creation of a tuple is done with parentheses.

``` python
# creation of an empty tuple
t = ()

# creation of a tuple with values
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

Tuples behave essentially the same as a list unless you try to modify one of the elements which will result in an error.  The following snippet of code will throw a TypeError.

```python
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
length = len(t)

for x in range(length):
    t[x] = t[x] * 2

# the previous line will result in the following Traceback
# Traceback (most recent call last):
#   File "scratch.py", line 5, in <module>
#       t[x] = t[x] * 2
# TypeError: 'tuple' object does not support item assignment
```

# Range
For all intents you can consider this to be a function that returns a immutable sequence of numbers but under the hood there is a [type](https://docs.python.org/3.8/library/stdtypes.html#range) supporting it.  So much so that...

```python
x = range(5)
print(type(x))          # Will print <type 'list'>
```

The `range()` 'function' works as follows:

*range(stop)*
returns a sequence that starts at zero and increments by 1 until stop is reached.  The stop value is not included in the range.  For example *range(5)* will contain the values 0, 1, 2, 3, 4.

*range(start, stop[, step])*
Need a custom range.  Python has got you covered.  You can specify a start value and stop value and an optional step value.  If the step value is not specific the value defaults to 1.

The parameters to range():
- Must all be integers- May be Positive, Negative or Zero
- By default range is 0 indexed

```python
# generate a range from (0, 9]
x = range(10)

# generate a range from (1, 11)
x = range (1, 11)

# generate a range from (10, 0)
x = range (10, 0, -1)
```

Yes, it is easy to fall prey to off-by-one errors using *range*.

## The for loop revisited
You may ask if it is possible to crete a for loop that executes 10 times without having to manage the expression that breaks out of the loop.  

```python
# range in a for loop
for x in range(10):
    print(x)            # Prints 0 - 9 on a line by itself
```

# Set
A set is an _unordered_ collection of unique elements.

```python
# initialize an empty set
set = set()
print(set)          # will print set([])

# initialize a set with unique values
set = {'banana', 'apple', 'orange'}
print(set)          # will print set(['orange', 'apple', 'banana'])

# initialize a set with duplicate values.
set = {'banana', 'apple', 'orange', 'apple'}
print(set)          # will print set(['orange', 'apple', 'banana'])
```

Adding items to the list is simple with the `add()` method

```python
set = set()
set.add('apple')
```


Removing items from a set can be done with either `remove()` or `discard()`.  I recommend using `discard()` as `remove()` will throw a TypeError if an item that is not in the set is removed.

# Dictionary
A dictionary is an *unordered* collection of key and value pairs that is mutable and indexed. Creation of a dictionary is done with curly brackets. 

```python
# Create an empty dictionary
d = {}

# Create a dictionary wth values
d =  {
    "Title": "Ghostbusters",
    "Year": 1984,
    "Rating": "PG",
    "Genre": ["Action", "Comedy", "Fantasy"]
}
```

Accessing an element is done by indexing into the dictionary with square brackets.

```python
print(d['Title'])           # Will print Ghostbusters
```

To change the values in a dictionary in a similar manner except that it is assigned on the left hand side of an equal sign.

```python
d['Title'] = 'Ghostbusters II"
d['Year'] = 1989
```

When you loop through a dictionary it will loop through the keys

```python
for key in d:
    print(key)

# prints
#   Genre
#   Rating
#   Year
#   Title
```

So you want to access the values you have to index it as demonstrated above.

```python
for key in d:
    print("{}: {}".format(key, d[key]))

# prints
#   Genre: ['Action', 'Comedy', 'Fantasy']
#   Rating: PG
#   Year: 1984
#   Title: Ghostbusters
```

Removing items from a dictionary can be done with either `pop()` or `del`.  `pop()` takes two parameters, the key and an optional default value.  If the key is found then it is removed and returned.  If the key is not found and a default value is provided the value is returned.  If no default was specified and the key is not found a KeyError Exception is raised.  

Let's take a more in depth look at the dictionary object.

```python   
# the hard way
text = 'supercalifragilisticexpialidocious'
count = {}   # Creates an empty dictionary

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

# will print
#     {'s': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'c': 3, 'a': 3, 'l': 3, 'i': 7, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1, 'o': 2}

# now let's explore removing items from this dictionary.
# how would we remove the vowels

vowels = 'aeiou'
for vowel in vowels:
    del count[vowel]
    
print(count)
# will print
#     {'c': 3, 'd': 1, 'g': 1, 'f': 1, 'l': 3, 'p': 2, 's': 3, 'r': 2, 't': 1, 'x': 1}
```

However, if you were paying attention to the comments you noted that this is the hard way to get counts like this.  Let's take a slight segue to show the easy way and introduce some specialized collections.  Python provides two high performance collections that could generate this data easier.:  `defaultdict` and `Counter`.  `defaultdict` allows you to specify a value for when the key does not exist in the collection and `Counter` is optimized for counting hashable objects.  

```python
    text = 'supercalifragilisticexpialidocious'
from collections import defaultdict
count = defaultdict(int)
for char in text:
    count[char] += 1

print(count)
# will print 
#     defaultdict(<type 'int'>, {'a': 3, 'c': 3, 'e': 2, 'd': 1, 'g': 1, 'f': 1, 'i': 7, 'l': 3, 'o': 2, 'p': 2, 's': 3, 'r': 2, 'u': 2, 't': 1, 'x': 1})

from collections import Counter
count = Counter(text)

print(count)
# will print 
#     Counter({'i': 7, 'a': 3, 'c': 3, 'l': 3, 's': 3, 'e': 2, 'o': 2, 'p': 2, 'r': 2, 'u': 2, 'd': 1, 'g': 1, 'f': 1, 't': 1, 'x': 1}) 
```

As you can see the data is very similar.  The only difference is the order that the items are shown.  If the order matters, and some times it does, using `orderdict` can solve this problem.  

One of that additional benefits of the counter collection is that it has numerous methods that can provide some useful data about the collection.  For example, 

```python
print count.most_common(3)
# will print [('i', 7), ('a', 3), ('c', 3)]
```
