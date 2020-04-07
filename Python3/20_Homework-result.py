  
num = int(input("Enter your number: "))
arr=["zero","one","two","three","four","five","six","seven","eight","nine"]

if num<10:
    print("One Digit",arr[num])
elif num<100:
    print("Two digits", ((num//10)+(num%10)))
elif num<1000:
    print("Three digits", ((num//100)*(num%100//10)*(num%10)))
else:
    print("number has more than 3 digits")