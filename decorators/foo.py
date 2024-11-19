def deco(func): 
    def inner(): 
        print('Running inner()')     # run when execute the inner function

    return inner    # return function object 

@deco 
def target(): 
    print('Running target()')

target()           # print 'Running inner()'
print(target)
print('=' * 50)


# ------------ Registration --------------------------------
# This example shows that decorator run right after the decorated function is defined 
# This is understandable, because @decorator def(f) ~ f = decorator(f), namely, we are calling the `decorator` function.
registry = []

def register(func): 
    print(f'Running register({func})')    # print logging that notify the execution of register function 
    registry.append(func)
    return func 

@register                               
def f1():                               # add function reference f1 to the list registry right now 
    print('running f1()')    

@register
def f2():                               # add function reference f2 to the list registry right now
    print('running f2()')               

def f3():                               # f3 is not a decorated function 
    print('running f3()')               

def main():
    print('running main()')
    print('registry ->', registry)      # registry now has two entries of function references: f1 and f2
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()