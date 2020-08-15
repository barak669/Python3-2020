num = int(input("Enter your number: "))


if num<=9:
    print("output:" ,num)

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
