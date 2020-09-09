class Person:
    def __init__(self, name,age,eye_color):
        self.name = name
        self.eye_color = eye_color
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, eye_color: {self.eye_color}"
    
    
def get_name(p):
    return p.name



arr=[
    Person("Bob",12,"brown"),
    Person("Alice",19,"green"),
    Person("Tom",17,"black")
]

print("------------------no sort--------------------------")
[print(p) for p in arr]


print("------------------age sort--------------------------")
arr=sorted(arr, key=lambda p:p.age)
[print(p) for p in arr]

print("------------------eye_color sort--------------------------")
arr=sorted(arr, key=lambda p:p.eye_color)
[print(p) for p in arr]

print("------------------name sort--------------------------")
arr=sorted(arr, key=get_name, reverse=True)
[print(p) for p in arr]