class Student:
    sum_score = 0
    sum_age = 0
    sum_student = 0

    # constractor
    def __init__(self, score, age):
        self.score=score
        self.age=age
        Student.sum_age += age/4
        Student.sum_score += score/4

    @classmethod
    def score_average(class_level):
        print(f"The average of the score is {class_level.sum_score}")

    @classmethod
    def age_average(class_level):
        print(f"The average of the age is {class_level.sum_age}")






s1=Student(90, 20)
s1.score_average()
s1.age_average()

s2=Student(88, 40)
s2.score_average()
s2.age_average()

s3=Student(79, 33)
s3.score_average()
s3.age_average()

s4=Student(95, 25)
s4.score_average()
s4.age_average()