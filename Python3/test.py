ID = (input("Enter your ID: "))
w = [1,2,1,2,1,2,1,2,1]
counter=0
sum1=0

print(ID)
print(w)


while counter<len(ID):
    sum = int(ID[counter]) * (w[counter])
    print(sum, end = ' ')
    
    counter+=1
   

       
print()
counter=0
while counter<len(ID):
    sum = int(ID[counter]) * (w[counter])
    counter+=1

    if sum>9:
       sum = (sum%10) + (sum//10)
       print(sum, end = ' ')

