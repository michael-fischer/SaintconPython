import functools

def add(x, y):
    return x + y

fib = [1, 1, 2, 3, 5]

sum = functools.reduce(add, fib)
print(sum)
