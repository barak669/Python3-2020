# must inherit from BaseException "Exception" to be able to raise this class as Exception 
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    pass

try:
    text = input('Enter something: ')
    if len(text) < 3:
        raise ShortInputException()

except ShortInputException:
    print('ShortInputException - because input is less than 3 chars')
    
else:
    print('No exception was raised.')


print("End of app")

"""
OUTPUT 1:
_________________________________________
Enter something: t
ShortInputException - because input is less than 3 chars
End of app
OUTPUT 2:
_________________________________________
Enter something: te
ShortInputException - because input is less than 3 chars
End of app
OUTPUT 3:
_________________________________________
Enter something: test
No exception was raised.
End of app
"""