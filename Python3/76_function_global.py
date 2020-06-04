x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


print('x before', x)
func()
print('x after', x)


"""
OUTPUT:
____________________________________
x before 50
x is 50
Changed global x to 2
x after 2
"""