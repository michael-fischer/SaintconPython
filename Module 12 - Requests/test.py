

def catch(func, handle=lambda e : e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        pass
        #  return handle(e)


eggs = (1,3,0,3,2)
result = [catch(lambda : 1/egg) for egg in eggs]

print(result)
# [1.0, 0.3333333333333333, None, 0.3333333333333333, 0.5]
# slight problem because of the None...

result = list(filter(None, result))
print(result)
# [1.0, 0.3333333333333333, 0.3333333333333333, 0.5]

# no, without the painful problems - if you know all the input that 
# could cause problems
result = [1/egg for egg in eggs if egg != 0]
print(result)
# [1.0, 0.3333333333333333, 0.3333333333333333, 0.5]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
msg = ",".join([str(num) for num in numbers])
# more pythonic
msg = ",".join(map(str, numbers))
