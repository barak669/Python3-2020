num = int(input("Enter number: "))

for outer in range(0, num):
    row=''
    for inner in range(0, num):
        if (inner==0 or outer==num-1):
            row+='*'
        if (inner==(num-4+inner)):
            row+=''
        else:
            row+='*'

    print(row)