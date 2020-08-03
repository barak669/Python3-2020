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