num = int(input("Enter number: "))

for outer in range(0, num):
    row=''
    for inner in range(0, num):
        if (inner==0 or inner==num-1 or outer==0 or outer==num-1):
            row+='*'
        else:
            row+=' '

    print(row)