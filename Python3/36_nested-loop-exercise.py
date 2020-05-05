Create a script that gets from the user a number and print an empty rectangle

Given the following shape.py script:

num=int(input("Enter a number: "))

for outer in range(0,num):
    row=""
    for inner in range(0,num):
        if inner==0 or inner==num-1 or outer==0 or outer==num-1:
            row+="*"
        else:
            row+=" "
    print(row)
test this script:

anna@HP-Printer:~$ python3 shape.py 
Enter a number: 4
****
*  *
*  *
****


anna@HP-Printer:~$ python3 shape.py 
Enter a number: 6
******
*    *
*    *
*    *
*    *
******