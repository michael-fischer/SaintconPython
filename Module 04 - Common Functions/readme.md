
# Welcome

# Iterate, Iterator and Iterables
Some terms that will help with this section.  

1. Iterate is defined in the dictionary as 'perform repeatedly.' 
2. An iterable is anything that can be looped over.
3. An iterator is an object with state that remembers where it is in during an iteration.

# Zip
`zip()` - Method that can combine multiple iterables into one structure.  This structure is an iterable of tuples.

```python
# zip() demo
names = ['Bob', 'Alice', 'Jane']
quiz1 = [80, 90, 74]
quiz2 = [92, 60, 96]

grades = zip(names, quiz1, quiz2)
print(grades)           # Will print [('Bob', 80, 92), ('Alice', 90, 60), ('Jane', 74, 96)]

# You can unzip items as well
students, tests, exams = zip(*grades)
print (students, tests, exams)         # prints (('Bob', 'Alice', 'Jane'), (80, 90, 74), (92, 60, 96))
```

If you pass in a single iterable you will get a list of one element tuples. 

```python
# zip() demo
names = ['Bob', 'Alice', 'Jane']
results = zip(names)
print(results)          # prints [('Bob',), ('Alice',), ('Jane',)]
```

One thing to note is that the returned iterator will stop when the shortest iterables passed into it is reached.

```python
# zip demo
names = ['Bob', 'Alice', 'Jane']
quiz1 = [80, 90]
quiz2 = [92, 60]

grades = zip(names, quiz1, quiz2)
print(list(grades))                           
# prints [('Bob', 80, 92), ('Alice', 90, 60)]
# Poor Jane was dropped from the class.

# Python 3.10.0 adds a new optional value that will throw a ValueError
# if the items do not match

grades = zip(names, quiz1, quiz2, strict=True)
# The preceding code will rasise an error and output
#     ValueError: zip() argument 2 is shorter than argument 1
```


# Map
`map()` - Method that will call a specified function with each element in an iterable.  The results returned from the map() function is a list containing the results the function on each item of the iterable.

```python
# map demo
def uppercase(text):
    return text.upper()

names = ['Bob', 'Alice', 'Jane']
results = map(uppercase, names)
print(results)                      # ['BOB', 'ALICE', 'JANE']
```

Working with multiple arguments is possible but tedious.  Here is an example without any special considerations.  We will learn a better way later.

```python
# map demo 2
def add(x, y):
    return x + y

range1 = [5, 7, 8]
range2 = [8, 4, 3]

results = map(add, range1, range2)
print(results)                      # [13, 11, 11]
```


# Filter
`filter()` - Method that will extract values that meet criteria from an iterable.  Similar to the map() function, filter() will take an function to take an iterable and apply it to the iterable.  The difference is that this function should return either True or False.  The resulting list returned from this will return an iterator that contains the values that returned true.  Here is a demo using the is_even method that we defined earlier.

``` python
# filter example
def is_even(num):
    return num % 2 == 0

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = filter(is_even, values)
print(results)              # [2, 4, 6, 8, 10] 
```

# Reduce
`reduce()` - Method that will perform cumulative tasks on an iterable.  This function may allow you to do some things that you thought were possible with map().  Where map() applies individually to each item passed into the iterable, reduce() will:

1. During the first step it will take the first two elements and apply it to the function.
2. For the second iteration it will take the results of the first call and the third item in the iterable and call the function.
3. The process continues until there are no more items and the final result is returned.

Using the add() function defined above we can see an example.

``` python
# reduce example
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(add, values)
print(result)                   # will print 55 
```