num=int(input("enter number:"))

if num == 0:
    print ("output:","zero")

if num == 1:
    print ("output:","one")

if num == 2:
    print ("output:","two")

if num == 3:
    print ("output:","three")

if num == 4:
    print ("output:","four")

if num == 5:
    print ("output:","five")

if num == 6:
    print ("output:","six")

if num == 7:
    print ("output:","seven")

if num == 8:
    print ("output:","eight")

if num == 9:
    print ("output:","nine")

elif num>=10 and num<=99:
	sum=(num%10+int (num/10))
	print(num%10+int (num/10))
	print("output:" ,num ,"is 2 digit number sum is",sum)

elif num>=100 and num<=999:
	mul=((num%10)*(int(num%100/10))*(int(num/100)) ) 
	print((num%10)*(int(num%100/10))*(int(num/100)) )
	print("output:" ,num ,"is 3 digit number mul is",mul)

else:
	print("output: number has more than 3 digits")
