  
import random

class OutOfRangeAge(Exception):
    pass

class OutOfRangeName(Exception):
    pass

class NotValidColor(Exception):
    pass

class Person:
    def set_age(self,age):
        if(age<0 or age>120):
            raise OutOfRangeAge()
        self.__age=age

    def set_name(self,name):
        if(len(name)<3 or len(name)>9):
            raise OutOfRangeName()
        self.__name=name

    def set_eye_color(self,color):
        if(not color in ["green","brown","blue"]):
            raise NotValidColor()
        self.__eye_color=color

    def __str__(self):
        return f"name: {self.__name}, age: {self.__age}, eye_color: {self.__eye_color}"


def init_person(p):
    colors=["green","brown","blue","red","yellow"]
    names=["Tom","ArielAriel","Bob","Alice"]

    while True:
        try:
            p.set_name(names[random.randint(0,len(names))])
            break
        except Exception:
            pass
    
    while True:
        try:
            p.set_eye_color(colors[random.randint(0,len(colors))])
            break
        except Exception:
            pass

    while True:
        try:
            p.set_age(random.randint(50,200))
            break
        except Exception:
            pass


people=[Person() for i in range(5)]

for p in people:
    init_person(p)

for p in people:
    print(p)