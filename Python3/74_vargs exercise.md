vargs exercise
Q1
create a function that gets numbers, and print the average of them

result 1
def avg(*nums):
    sum=0
    for x in nums:
        sum+=x
    print(f"avg of: {nums}: {sum/len(nums)}")




avg(22,5)           #-> avg of: (22, 5): 13.5

avg(30,90,3)        #-> avg of: (30, 90, 3): 41.0

avg(4)              #-> avg of: (4,): 4.0
Q2
create a function that gets numbers, and prints the two max values

result 2
def max2(*nums):
    max1=0
    max2=0
    for x in nums:
        if x>max1:
            max2=max1
            max1=x
        elif x>max2:
            max2=x
    print(max1,max2)



max2(22,100,99,5,50)           #-> 100 99

max2(2,9,5,7,1)                #-> 9 7