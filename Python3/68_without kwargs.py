def func(a):
    print(a)

func(name="Bob",age=12,hobbies=["Cyber","Math","Programming"])


"""
OUTPUT:
______________________________
Traceback (most recent call last):
    func(name="Bob",age=12,hobbies=["Cyber","Math","Programming"])
TypeError: func() got an unexpected keyword argument 'name'
"""