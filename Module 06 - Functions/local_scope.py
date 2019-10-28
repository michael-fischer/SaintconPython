
def first():
    print('Start of First')
    # print(test)  -- This is not defined yet so would raise a UnboundLocalError
    test = "first"
    print(test)
    second()
    print('End of First')

def second():
    print('Start of Second')
    test = "second"
    print(test)
    print('End of Second')

def third():
    print('Start of Third')
    global test
    print(test)
    test = 'third'
    print(test)
    print('End of Third')

test = "global"
print(test)
print("=" * 10)
first()
print(test)
print("*" * 10)
third()
print(test)