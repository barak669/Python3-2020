'''
def func(*a):
    sum=0
    for x in range(0, len(a)):
        sum+=x
    print(f"avg of {a}: is {sum/len(a)}")
    

arr=[1,2,3,4,5,6]

arr=[12,3,22,]

arr=[14,2,4,6]

func(*arr)
'''



def max2(*nums):
    sum=0
    max1=nums[0]
    max2=nums[0]
    for x in nums:
        if x>max1:
            max2=max1
            max1=x
        elif x>max2:
            max2=x
    print(max1, max2)


    
max2(22,100,99,552,50)

max2(2,9,5,7,1)


