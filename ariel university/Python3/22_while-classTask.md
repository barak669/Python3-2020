Q1
Get a number from the user
Print to the user if the number is a Palindromic_number
NOTE: Palindromic_number are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, etc...
Result
First way (get the input as a string):
num=input("Insert a number: ")

count=1
flag=True

while count<=(len(num)//2):
    flag= flag and (num[count-1] == num[len(num)-count])
    count+=1

print(flag)
Second way (get the input as a number):
num=int(input("Insert a number: "))

copy_num=num
temp=0


while num!=0:
    temp=(temp*10)+(num%10)
    num//=10

print(copy_num==temp)
Q2
קלוט מהמשתמש מספר (יש להניח שהמספר שנקלט חיובי) והדפס ללקוח את מכפלת הספרות

Result
num=int(input("Insert a number: "))
mul=1

while num!=0:
    mul*=num%10
    num//=10

print(mul)
Q3
קלוט 10 מספרים ובדוק אם הם ממוינים בסדר עולה (כלומר אם כל נתון הוא גדול או שווה לקודמו). אם כן הדפס "ממוין", אחרת הדפס "לא ממוין"

Result
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
Q4
קלוט 20 מספרים וסכם אותם, כאשר הגעת לנתון השווה לסכום כל קודמיו הדפס אותו, אם בכל האיטרציות לא מצאת הדפס (אחרי היציאה מהלולאה) "לא נמצא"

Result
counter=0
sum=0
flag=False

while counter<3:
    current=int(input("Insert a number: "))

    if current==sum:
        print(current, "is the amount of the prev inputs")
        flag=True

    sum+=current
    counter+=1
    


if not flag:
    print ("no of the inputs was the amount of the prev inputs")
Q5
הדפס את כל המספרים בין 10 ל-99 שספרת האחדות שלהם גדולה מספרת העשרות

Result
counter=10
while counter<=99:
    if counter%10>counter//10:
        print(counter)
    counter+=1
Q6
הדפס את כל המספרים הדו-ספרתיים המתחלקים לספרת האחדות שלהם, לספרת העשרות שלהם, ולסכום הספרות שלהם.

Result
counter=10
while counter<=99:
    left_digit=counter//10
    right_digit=counter%10

    divided_by_right_digit= right_digit!= 0 and counter%right_digit==0
    divided_by_left_digit= counter%left_digit==0 
    divided_by_sum_of_digit=counter%(right_digit+left_digit)==0

    if right_digit !=0:
        if  divided_by_right_digit and divided_by_left_digit and divided_by_sum_of_digit:
            print(counter)
    counter+=1
Q7
קלוט משמשתמש מספר והדפס האם הוא מספר ראשוני או לא (מספר ראשוני הוא מספר שלם וחיובי, שמתחלק רק בעצמו וב-1 ללא שארית)

Result
first way (without break)
num=int(input("Insert a number: "))
counter=2
flag=True

while counter<num and flag:
    if num%counter==0:
        flag=False
    counter+=1


if flag:
    print("prime number")
else:
    print("not a prime number")
second way (with break):
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