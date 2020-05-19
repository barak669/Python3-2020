t=("zero","one","two","three")

print(t[0])  # -> zero
print(t) #-> ('zero', 'one', 'two', 'three')

"""
t[0]="ZERO"     #-> TypeError: 'tuple' object does not support item assignment
del t[0]        #-> TypeError: 'tuple' object doesn't support item deletion
t=t+("four")    #-> TypeError: can only concatenate tuple (not "str") to tuple
"""


#  create a copy of existing tuple and then add new element to it using `+` operator
t=t+("four",)



print(t) #-> ('zero', 'one', 'two', 'three', 'four')


# Sliced copy containing elements from 3 to end
print(t[3:]) #-> ('three', 'four')


# Sliced copy containing elements from 0 to 3
print(t[:3]) #-> ('zero', 'one', 'two')


t=t[:2]+("TWO",)+t[3:]
print(t) #-> ('zero', 'one', 'TWO', 'three', 'four')

t=t[:2]+t[3:]
print(t) #-> ('zero', 'one','three', 'four')

print(len(t))  #-> 4