  
class Person:
    def __init__(self,age):
        self.set_age(age) 

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if(age>=0 and age<=120):
            self.__age=age  # property with "__" prefix is a private property


p1=Person(14)
print(p1.get_age())     #--> 14
p1.set_age(400)
print(p1.get_age())     #--> 14
p1.set_age(-400)
print(p1.get_age())     #--> 14
p1.set_age(50)
print(p1.get_age())     #--> 50
p1.set_age(p1.get_age()+1)
print(p1.get_age())     #--> 51