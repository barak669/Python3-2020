#################################### int - val type ##############################################

num1=1
num2=num1

print("num1=",num1,"num2=",num2)  # num1= 1 num2= 1

num1=3
print("num1=",num1,"num2=",num2)  # num1= 3 num2= 1




#################################### float - val type #############################################

float1=1.2
float2=float1


print("float1=",float1,"float2=",float2)  # float1= 1.2 float2 = 1.2

float1=3.6
print("float1=",float1,"float2=",float2)  # float1= 3.6 float2 = 1.2


#################################### boolean - val type ############################################

bool1=True
bool2=bool1


print("bool1=",bool1,"bool2=",bool2)  # bool1= True bool2= True

bool1=False
print("bool1=",bool1,"bool2=",bool2)  # bool1= False bool2= True




#################################### list - ref type ############################################

list1=[12,15,17]
list2=list1


print("list1=",list1,"list2=",list2)  # list1= [12, 15, 17] list2= [12, 15, 17]

list1[0]=99
print("list1=",list1,"list2=",list2)  # list1= [99, 15, 17] list2= [99, 15, 17]


list1=[66,33,22]
print("list1=",list1,"list2=",list2)  # list1= [66, 33, 22] list2= [99, 15, 17]



#################################### dict - ref type ############################################
dict1={"age":12}
dict2=dict1


print("dict1=",dict1,"dict2=",dict2)  # dict1= {'age': 12} dict2= {'age': 12}

dict1["age"]=13
print("dict1=",dict1,"dict2=",dict2)  # dict1= {'age': 13} dict2= {'age': 13}

dict1={"age":45}
print("dict1=",dict1,"dict2=",dict2)  # dict1= {'age': 45} dict2= {'age': 13}