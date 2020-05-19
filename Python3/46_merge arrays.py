  
arr1=["a","b","c"]
arr2=[7,8,9]

print(arr1)     # -> ['a', 'b', 'c']
print(arr2)     # -> [7, 8, 9]

arr1.extend(arr2)
print(arr1)     # -> ['a', 'b', 'c', 7, 8, 9]
print(arr2)     # -> [7, 8, 9]


arr3 = arr1 + arr2
print(arr1)     # -> ['a', 'b', 'c', 7, 8, 9]
print(arr2)     # -> [7, 8, 9]
print(arr3)     # -> ['a', 'b', 'c', 7, 8, 9, 7, 8, 9]