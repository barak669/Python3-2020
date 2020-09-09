def say_hello():
    return "hello"


f1=say_hello()
print(f1)    # --> hello


f2=say_hello
print(f2)    #  -->  <function say_hello at 0x7fd0f89cfe50>


print(f2())  # --> hello