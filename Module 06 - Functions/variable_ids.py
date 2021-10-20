
def lcoal_var():
    print('local_var()')
    # print(test)  -- This is not defined yet so would raise a UnboundLocalError
    test = "inside local_var"
    print("2 ==> {0}".format(id(test)))

def global_var():
    print('global_var()')
    global test
    print("3 ==> {0}".format(id(test)))
    print(test)
    test = 'inside global_var()'
    print("4 ==> {0}".format(id(test)))
    

test = "global"
print("1 ==> {0}".format(id(test)))
print(test)
print("=" * 10)
lcoal_var()
print("=" * 10)
global_var()
print(test)
print("5 ==> {0}".format(id(test)))