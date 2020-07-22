def print_max(a,b):
    if a>b:
        return "a="+str(a)
    elif b>a:
        return "b="+str(b)
    return "equal"


res=print_max(2,4)
print("res for (2,4):",res)

res=print_max(4,2)
print("res for (4,2):",res)

res=print_max(4,4)
print("res for (4,4):",res)



"""
OUTPUT:
___________________
res for (2,4): a=4
res for (4,2): b=4
res for (4,4): equal
"""