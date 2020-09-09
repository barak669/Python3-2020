  
def x0():
    return 2

x1=x0

print(x1())   # --> 2

# lambda = is a way to define a function that may get params and return 1 value
x3 = lambda :2

print(x3())   # --> 2


x4 = lambda y:y*2

print(x4(3))  # --> 6


sub = lambda z,w:z-w
div = lambda z,w:z/w
mul = lambda z,w:z*w
mod = lambda z,w:z%w

print(sub(9,4))  # --> 5
print(div(9,4))  # --> 2.25
print(mul(9,4))  # --> 36
print(mod(9,4))  # --> 1