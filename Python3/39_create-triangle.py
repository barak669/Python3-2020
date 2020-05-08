num = int(input("Enter number: "))

for i in range(0, num):
    row = ''
    for j in range(0, i+1):
        row+='*'
    for j in range(0, num-i-1):
        row+=''

    print(row)