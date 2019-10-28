

def fibonacci(n): 
    a = 1
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n <= 0: 
        return n 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 


def squares(n):
    return n**n


def triangles(n):
    return int((n * (n +1))/2)

