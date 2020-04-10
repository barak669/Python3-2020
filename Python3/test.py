num=int(input("Insert a number: "))
counter=2


while counter<num:
    if num%counter==0:
        break
    counter+=1


if counter==num:
    print("prime number")
else:
    print("not a prime number")