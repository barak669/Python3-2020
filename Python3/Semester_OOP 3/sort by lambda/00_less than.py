  
class Person:
    pass


print(2<4)                    #-->  True
print("c"<"B")                #-->  False
print( ("a",200) < ("b",1))   #-->  True
print( Person() < Person())   #--> TypeError: '<' not supported between instances of 'Person' and 'Person'
print( {"a":1} < {"b":1})     #--> TypeError: '<' not supported between instances of 'dict' and 'dict'