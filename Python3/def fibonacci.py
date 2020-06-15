def fibonacci(amount):
    first=0
    second=1
    print(first,second,end=" ")

    for x in range(2,amount):
        temp = second
        second += first
        first = temp
        print(second,end=" ")

fibonacci(4)
print()
fibonacci(9)
print()