num=int(input("Insert a number: "))
mul=1

while num!=0:
    mul*=num%10
    num//=10

print(mul)


3