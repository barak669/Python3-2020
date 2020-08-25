  
class AgeExeption(Exception):
    '''A user-defined exception class.'''
    def __init__(self,age):
        Exception.__init__(self)
        self.age=age

class UnderAgeExeption(AgeExeption):
    '''A user-defined exception class.'''
    pass


class OverAgeExeption(AgeExeption):
    '''A user-defined exception class.'''
    pass

try:
    age = int(input('Enter age: '))
    if age < 0:
        raise UnderAgeExeption(age)
    if age > 120:
        raise OverAgeExeption(age)


except AgeExeption as my_ex:  
    print(f"non valid age: {my_ex.age}, {type(my_ex).__name__}")


else:
    print('valid age')


print("End of app")


"""
OUTPUT 1:
_________________________________________
Enter age: 130
non valid age: 130
End of app
OUTPUT 2:
_________________________________________
Enter age: -5
non valid age: -5
End of app
OUTPUT 3:
_________________________________________
Enter age: 5
valid age
End of app
"""