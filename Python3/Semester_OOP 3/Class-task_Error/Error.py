class OutOfRangeAge(Exception):
    pass

    class OutOfRangeName(Exception):
    pass

    class NotValidColor(Exception):
    pass

class Person:
    def __init__(self, age, name, eye_color):
        self.age=age
        self.name = name
        self.eye_color=eye_color

    @set_age.setter
    def set_age(self,age):
        raise OutOfRangeAge() if(set_age<0 or set_age>120) else self.__age=age

    @set_name.setter
    def set_name(self,name):
        raise OutOfRangeName() if(len(name)<3 or len(name)>9) else self.__name=name

    @set_eye_color.setter
    def set_eye_color(self,eye_color):
        raise NotValidColor() if(not color in ["green", "brown", "blue"]) else self.__eye_color=eye_color

    def __str__(self):
        return f"name: {self.__name}, age: {self.__age}, eye_color: {self.__eye_color}"