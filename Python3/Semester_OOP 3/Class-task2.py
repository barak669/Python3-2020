<<<<<<< HEAD
class Student:
    student_cnt=0
    grades_sum=0
    ages_sum=0

    def __init__(self, age, grade):
        self.age=age
        self.grade=grade

        Student.student_cnt+=1
        Student.grades_sum+=grade
        Student.ages_sum+=age

    @classmethod
    def grades_avg(cls):
        return cls.grades_sum/cls.student_cnt

    @classmethod
    def ages_avg(cls):
        return cls.ages_sum/cls.student_cnt
    
    def print_info(self):
        print(f"age: {self.age}, grade: {self.grade}")


students=[
    Student(10,60),
    Student(15,70),
    Student(20,60),
    Student(25,70),
]

for student in students:
    student.print_info()
    

print("grades_avg:",Student.grades_avg())
print("ages_avg:",Student.ages_avg())


"""
OUTPUT:
____________________________________
age: 10, grade: 60
age: 15, grade: 70
age: 20, grade: 60
age: 25, grade: 70
grades_avg: 65.0
ages_avg: 17.5
"""
=======
class Cinema:

    def __init__(self, name,num_of_chairs,open_hour,close_hour):
        self.name=name
        self.num_of_chairs=num_of_chairs
        self.open_hour=open_hour
        self.close_hour=close_hour

    def amount_of_open_hours(self):
        return self.close_hour-self.open_hour

    def print_info(self):
        return f*"name:{self.name}, open_hour: {self.open_hour}, close_hour: {self.close_hour}, num_of_chairs: {self.num_of_chairs}"

    @property
    def num_of_chairs(self):
        return self.__num_of_chairs


    @num_of_chairs.setter
    def num_of_chairs(self, num):
        self.__num_of_chairs = num if num>0 else 0

    @property
    def open_hour(self):
        return self.__open_hour


    @open_hour.setter
    def open_hour(self, hour):
        self.__open_hour = hour if hour>6 and hour<12 else 6

    @property
    def close_hour(self):
        return self.__close_hour


    @close_hour.setter
    def close_hour(self, hour):
        self.__close_hour = hour if hour>18 and hour<23 else 6


arr= [
    Cinema("Yes", 38,7,22),
    Cinema("Hen", -9,5,12)
]


>>>>>>> 57dacf9a1dc4f6034bafa0c69e86bd026554bc5b
