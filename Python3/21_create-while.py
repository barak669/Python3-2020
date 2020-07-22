## first way
num=input("enter number:")

count=1
flag=True

while count<=(len(num)//2):
    flag=flag and (num[count-1] == num[len(num)-count])
    count+=1

print(flag)

## second way
num=int(input("enter number:"))

copy_num=num
temp=0

while num!=0:
    temp=(temp*10)+(num%10)
    num//=10

print(copy_num==temp)