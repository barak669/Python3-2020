chars=["a","b","c","d","e","f"]

print(chars)        # -> ['a', 'b', 'c', 'd', 'e', 'f']
chars.pop()
print(chars)        # -> ['a', 'b', 'c', 'd', 'e']
chars.pop(1)
print(chars)        # -> ['a', 'c', 'd', 'e']


if("f" in chars):
    chars.remove("f")
    print(chars)   
else:
    print("f does not exist in the array")  # -> f does not exist in the array    


if("d" in chars):
    chars.remove("d")
    print(chars)                            # -> ['a', 'c', 'e']  
else:
    print("d does not exist in the array")    


chars.clear()
print(chars)    # -> []