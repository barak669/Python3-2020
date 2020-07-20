def sum(x1,x2,x3):
    print(f"{x1} + {x2} + {x3} = {x1+x2+x3}")


arr=[4,5,6]


################# first way: (send each element by index) ######################
sum(arr[0],arr[1],arr[2])       #-> 4 + 5 + 6 = 15

################# second way: (send with vargs) ################################
sum(*arr)                       #-> 4 + 5 + 6 = 15