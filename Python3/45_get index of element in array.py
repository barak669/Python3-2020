  
arr=["a","b","c","a","d","e","a","h","a","a"]

print(arr)              # -> ['a', 'b', 'c', 'a', 'd', 'e', 'a', 'h']

print(arr.count("a"))   # -> 3
print(arr.count("t"))   # -> 0


print("a is in indexes:")
temp=arr[0:]
removed_items=0
while (temp.count("a")) > 0:
    firstIndex=temp.index("a")
    print(removed_items+firstIndex)
    removed_items+=firstIndex+1
    temp=temp[firstIndex+1:]