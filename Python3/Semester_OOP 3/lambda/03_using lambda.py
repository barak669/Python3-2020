class Person:
    def __init__(self,age, name, hello_action):
        self.age=age
        self.name=name
        self.hello_action=hello_action
    
    def say_hello(self):
        print(f"name: {self.name}, age: {self.age}, hello_action: {self.hello_action('test')}")


p1=Person(12,"Bob",lambda x: f"Hello i am p1 and got {x}")

p2=Person(16,"Tom",lambda y: f"Hello i am p2 and got {y}")

p1.say_hello()  # --> name: Bob, age: 12, hello_action: Hello i am p1 and got test
p2.say_hello()  # --> name: Tom, age: 16, hello_action: Hello i am p2 and got test