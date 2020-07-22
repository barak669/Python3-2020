  
arr=[0,1,2,3,4,5,6,7,8,9]


# list [m : n] means sublist start at index m (included) and end at index n (not included).

print(arr)              # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[-3])          # -> 7
print(arr[:6])          # -> [0, 1, 2, 3, 4, 5]
print(arr[7:])          # -> [7, 8, 9]
print(arr[3:5])         # -> [3, 4]
print(arr[-8:-5])       # -> [2, 3, 4]
print(arr[::-1])        # Get a reversed list by providing step size as -1