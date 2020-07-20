class Student:
    sum_score = 0
    sum_age = 0
    sum_student = 0 

    # constractor
    def __init__(self, age, score):
        self.score=score
        self.age=age
        Student.sum_student += 1
        Student.sum_age += age
        Student.sum_score += score

    @classmethod
    def score_average(cls):
        return cls.sum_score/cls.sum_student
        

    @classmethod
    def age_average(cls):
        return cls.sum_age/cls.sum_student

    @classmethod
    def print_info(self):
        print(f"age: {self.age}, score: {self.score}")



student=[
    Student(10,60),
    Student(15,70),
    Student(20,60),
    Student(25,70),
]

for student in student:
    student.print_info()

print("score average: ",Student.sum_score())
print("age average: ",Student.sum_age())