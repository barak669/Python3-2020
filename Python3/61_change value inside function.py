
def change_arr_element(arr):
    arr[0]+=1


def change_arr(arr):
    arr=[1,2,3]



def change_num(num):
    num+=1


ages=[12,16,18]
print("before function",ages)       # -> before function [12, 16, 18]

change_arr_element(ages)
print("after function",ages)        # -> after function [13, 16, 18]

change_arr(ages)
print("after function",ages)        # -> after function [13, 16, 18]


age=20
print("before function",age)        # -> before function 20

change_num(age)