class Person:
    def __init__(self,age):
        self.age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if(age>=0 and age<=120):
            self.__age=age  # property with "__" prefix is a private property


p1=Person(14)
print(p1.age)     #--> 14
p1.age=400
print(p1.age)     #--> 14
p1.age=-400
print(p1.age)     #--> 14
p1.age=50
print(p1.age)     #--> 50
p1.age+=1
print(p1.age)     #--> 51