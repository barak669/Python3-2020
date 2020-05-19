
"""
List Comprehension - Basic way
"""
arr1=[]
for j in range(0,4):
    arr1.append(j)

print(arr1)     # -> [0, 1, 2, 3]


arr2=[i for i in range(0,4)] 
print(arr2)     # -> [0, 1, 2, 3]


"""
List Comprehension - Conditional Logic way
"""
arr3=[]
for j in range(0,5):
    if j%2 ==0:
        arr3.append(j)

print(arr3)     # -> [0, 2, 4]


arr4=[i for i in range(0,5) if i%2==0] 
print(arr4)     # -> [0, 2, 4]


"""
List Comprehension - Conditional Triple Logic way
"""
arr5=[]
for j in range(3,7):
    if j%2==0:
        arr5.append("even"+str(j))
    else:
        arr5.append("odd"+str(j))

print(arr5)     # -> ['odd3', 'even4', 'odd5', 'even6']


arr6=["even"+str(i) if i%2==0 else "odd"+str(i) for i in range(3,7)] 
print(arr6)     # -> ['odd3', 'even4', 'odd5', 'even6']

