def sort_arr(arr, key=lambda x: x , reverse=False):
    for current in range(0,len(arr)-1):
        index=current

        for i in range(current, len(arr)):
            if not reverse and key(arr[i]) < key(arr[index]):
                index=i
            elif reverse and key(arr[i]) > key(arr[index]):
                index=i

        temp=arr[current]
        arr[current]=arr[index]
        arr[index]=temp



arr1=[0, -10, 15, -2, 1, 12]

sort_arr(arr1)
print(arr1)  #--> [-10, -2, 0, 1, 12, 15]

sort_arr(arr1, reverse=True)
print(arr1)  #-->  [15, 12, 1, 0, -2, -10] 


arr2 = [{"name":"Alice","age": 100},{"name":"Bob","age": 20}]
sort_arr(arr2, key= lambda x: x["age"])
print(arr2)