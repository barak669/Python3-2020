current=int(input("Insert a number: "))
counter=0
is_legal=0

while counter<3:
    prev=current
    current=int(input("Insert a number: "))
    if prev<=current:
        is_legal+=1
    counter+=1

if(is_legal==3):
    print("you entered a valid set")
else:
    print("you entered invalid set")  