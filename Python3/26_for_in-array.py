arr=["a","b","c","d"]

counter=0
while counter<len(arr):
    print("while",arr[counter])
    counter+=1

for x in arr:
    print("for-in",x)


"""
OUTPUT:
________________
while a
while b
while c
while d
for-in a
for-in b
for-in c
for-in d
"""