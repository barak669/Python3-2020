class Student:

    # constractor
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def say_hello(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")



s1=Student("Bob", 12)
s1.say_hello()

s2=Student("Alice", 120)
s2.say_hello()