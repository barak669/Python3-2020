ID = (input("Enter your ID: "))
w = [1,2,1,2,1,2,1,2,1]
counter=0
counter1=0
sum1=0

print(ID)
print(w)


while counter<len(ID):
    sum = int(ID[counter]) * (w[counter])
    counter+=1 
    print(sum, end= ' ')
 
   


while counter1<len(ID):
    sum = int(ID[counter1]) * (w[counter1])
    counter1+=1

    if sum>9:
       sum = (sum%10) + (sum//10)
       print(sum, end = ' ')
       

