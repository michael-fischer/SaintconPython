
# Welcome

This module will introduce the concepts of decision making and looping constructs.

# Decisions are True/False, Yes/No, 0/1.  

|Operation|Description|
|:-:|-|
|AND |If both are True the result is True |
|OR |If One of the results is True the result is True | 
|NOT|Invert the result.  If operand is True then the result is false and vice versa |
|XOR|If One or the other but not Both then the result is True|

# Hopefully the most math we see today

## Arithmetic Operators
| Operator | Symbol | Description | Example |
|- | - | - | - | 
| Addition | + | Adds the two addends together to provide the sum| sum = addend1 + addend2  | 
| Subtraction | - | Subtracts the subrtahend from the minuend to provide the difference | difference = minuend - subtrahend | 
| Multiplication | * | Multiplies the multiplicand by the multiplier to return the product  |  product = multiplicand * multiplier |
| Division | / | Divides the dividend by the devisor to return the quotient | quotient = dividend / devisor | 
| Modulus | % | represents the remainder of the result of division with the quotient has been determined   | modulus = dividend % devisor  | 
| Exponent | ** | Raises the base by the value specified in the exponent to return the power | power = base ** exponent | 
| Floor Division | // | Similar to division but with the result round down to the next lower integer value | quotient = dividend // divisor | 

## Assignment Operators
| Symbol | Description | Longhand | Shorthand |
| - | - | - | - |
| = | Assigns the value from the right hand side to the left hand side |  x = y | NA |
| += | Adds the right operand to the left operand and stores the result in the left operand | x = x + y | x += y |
| -= | Subtracts the right operand from the left operand and stores the result in the left operand | x = x - y | x -= y |
| *= | Multiples the left operand with the right operand and stores the value in the left operand | x = x * y | x *= y |   
| /= | Divides the left operands with the right operand and stores the result in the left operand | x = x / y | x /= y |   
| %= | Performs the modulo function on the left operand by the right operand and stores the result in the left operand |  x = x % y | x %= y |  
| **= | Raises the left operand to the exponent specified in the right operand and stores the result in the left operand | x = x ** y | x **= y |   
| //= | Divides the left operands with the right operand and stores the result in the left operand | x = x // y | x //= y |   

## Comparison operators
| Operator | Symbol | Description  |
|- | - | - | 
| Equal To| == | Returns True if the two values are equal  |  
| Not Equal | != *OR* <> | Returns True if the two values are  not equal|
| Greater Than | > | Returns True if the first value is greater than the second value |  
| Less Than | < | Returns True if the first value is less than the second value |  
| Greater Than or Equal To | >= | Returns True if the first value is greater than or equal to the second value |  
| Less Than or Equal to | <= | Returns True if the first value is less than or equal to the second value | 


## Bitwise operators
| Operator | Symbol | Description |
| - | - | - | 
| Binary AND  | & | Copies a bit to the result if it is set in bother operands |  
| Binary OR | \| | Copies a bit to the result if it is set in either operand |  |  
| Binary XOR | ^ | Copies the bit if it is set in one operand but not the other |  
| Binary Ones Complement | ~ | A unary operator that 'flips' the bits that are set | 
| Binary Left Shift | << | The left hand operands are moved to the left by the number of bits represented on the right hand side |  
| Binary Right Shift | >> | The left hand operands are moved to the right by the number of bits represented on the right hand side |  

### Bitwise Truth Table
## Truth Table 
|  A  |  B  | A & B | A \| B | A ^ B | 
| :-: | :-: | :-: | :-:| :-: |
| 1 | 1 | 1 | 1 | 0 | 
| 1 | 0 | 0 | 1 | 1 |  
| 0 | 1 | 0 | 1 | 1 |  
| 0 | 0 | 0 | 0 | 0 | 


## Logical operators
For the purpose of logical operators False  is zero and True is Non Zero.

| Operator | Symbol | Description | 
| :-: | :-: | :-: | 
| Logical AND | AND | Returns True if both operands are True | 
| Logical OR | OR | Returns True if either of the operands are True |
| Logical NOT | NOT | Reverses the logical state of the operator |

### Logical Truth Table 
|  A  |  B  | A AND B | A OR B  | NOT A | 
| :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | F |
| T | F | F | T | F | 
| F | T | F | T | T | 
| F | F | F | F | T |

## Seeing the difference between bitwise and logical operators

    # Set two variables with integers and perform both  bitwise and logical operations on them
    x = 5
    y = 7
    bitwise = a & b     # this returns 5
    logical = a and b   # this returns 7

Bitwise operations will make comparisons at the, you guessed it, bit level.  Resulting in:

| variable | integer value | bit 4| bit 3 | bit 2 | bit 1 
|:-:|:-:|:-:|:-:|:-:|:-:|  
| x | 5 | 0 | 1 | 0 | 1 |  
| y | 7 | 0 | 1 | 1 | 1 |
| x & b | 5 | 0 | 1 | 0 | 1 |

Want to convert an integer to a string in another base?  Look at *bin()*, *oct()*, and *hex() to print out numbers in different bases.  To convert one of these strings into an integer you can use the *int()* method.

    x = 254
    bin(x)              # returns the string '0b11111110'
    oct(x)              # returns the string '0o376'
    hex(x)              # returns the string '0xfe'

    int('0xff', 16)     # returns the integer 255

if you specify 0 as the base then the Python runtime will attempt to infer the base from the encoding in the string.  

# Branching logic

## Simply make a decision to do something or not

    if expression:
        statements

## Simply make a decision to do one thing or another

    if expression:
        statements
    else:
        statements

## so many choices

    if expression:
        statements
    elif expression:
        statements
    ...
    else:
        statements

## Nested decisions

    if expression:
        if another expression:
            statements

A note about nested conditionals is that by applying a bit more thought to the problem it is sometimes possible to collapse them into single statements.  For example, consider:

```python
if num >= 0:
    if num == 0:
        print('LIFTOFF')
    else:
        print(num)
else:
    print('Did the engines forget to fire?')
```

can be rewritten without the nesting

```python
if num > 0:
    print(num)
elif num == 0:
    print('LIFTOFF')
else:
    print('Did the engines forget to fire?')
```

Or, another example

```python
if weapon_ready:
    if target_in_range:
        fire()
```

can be simplified as:

```python
if weapon_ready and target_in_range():
    fire()
```

## ternary operator
AKA conditional expression.  This provides a sort of one line if statement to python.  This shorter syntax allows you to combine the conditional with an assignment.  Consider this example:

```python
# Sets result = to 'odd' or 'even' based on checking the modulus value.  
# Assumes that num has been set elsewhere.
if num % 2 == 0:
    result = 'even'
else:
    result = 'odd'
```
    
This could easily be rewriting using the ternary operator as:

```python
result = 'even' if num % 2 == 0 else 'odd'
```

If you are familiar with other programming languages this syntax may be a bit odd to you.

# Do things again, again
Python has simplified looping constructs compared tother languages and it is a little daunting the first time you try to create a for loop.  

There are two types of loops in Python: the *for* loop and the *while* loop. 

## For loop
The *for* loop is chosen when you have an an object that is iterable that you want to iterate through and perform an operation on each item.

```python
fruits = ['Apple', 'Banana', 'Orange']
for fruit in fruits:
    print(fruit)

# prints
# Apple
# Banana
# Orange
```


## While loop
The while loop allows you to continue a loop until a condition is meet.  

    while expression:
        statements

For example:

```python
# print odd numbers less than 10.
num = 0
while num < 10:
    print(num)
    num += 1
```

# Summary

This is a quick in depth look at decision making and looping.  It is good to know but shortly we will see some more pythonic ways to accomplish this.
