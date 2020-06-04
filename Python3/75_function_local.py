x = 50


def func(x):
    ''' In this function the "x" is not the global "x" - it is a local "x" '''
    print('x is', x)
    x = 2
    print('Changed local x to', x)



print('x before', x)
func(x)
print('x after', x)


"""
OUTPUT:
____________________________________
x before 50
x is 50
Changed local x to 2
x after 50
"""