### program to print sum of digit (for 2 digits number)

num=34
print(num%10+int (num/10))

### program to print sum of digit (for 3 digits number)

num=342
print((num%10)+(int(num%100/10))+(int(num/100)) )

### program to print sum of digit (for 4 digits number)

num=3421
print((num%10)+int((num%100)/10)+int((num%1000)/100)+(int(num/1000)))

### program to print sum of digit (for 5 digits number)

num=53421
print((num%10)+int((num%100)/10)+int((num%1000)/100)+int((num%10000)/1000)+int((num%100000)/10000))