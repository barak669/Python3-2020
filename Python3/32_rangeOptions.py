# range with two parameters returns an object that produces a sequence of integers 
# from the first parameter(inclusive) to the second parameter (exclusive)
# When step increment by 1
for x in range(5,7):
    print("first for loop:",x )

print("-------------------")

# range with one parameter returns an object that produces a sequence of integers 
# from 0 to the parameter (exclusive)
# When step increment by 1
for x in range(3):
    print("second for loop:",x )

print("-------------------")

# range with three parameters returns an object that produces a sequence of integers 
# from the first paramter(inclusive) to the second parameter (exclusive)
# When step increment by the third parameter
for x in range(5,10,2):
    print("third for loop:",x )

print("-------------------")

# range with three parameters returns an object that produces a sequence of integers 
# from the first paramter(inclusive) to the second parameter (exclusive)
# When step decrement by the third parameter
for x in range(10,5,-2):
    print("four for loop:",x )

"""
OUTPUT:
_____________________________
first for loop: 5
first for loop: 6
-------------------
second for loop: 0
second for loop: 1
second for loop: 2
-------------------
third for loop: 5
third for loop: 7
third for loop: 9
-------------------
four for loop: 10
four for loop: 8
four for loop: 6
"""