obj={
  "userId": 1,
  "name": "Bob",
  "completed": False,
  "hobbies":["Music","Sport"],
  "adderss":{
      "city":"Ariel",
      "country":"Israel"
  }
}


print(obj)

# access specific property in obj
print(obj["name"])


# edit specific property in obj
obj["name"]="Alice"

print(obj)

# delete specific property in obj
del obj["name"]

print(obj)


# get an array that each element in the array conatain the key and the value
print(obj.items())

print("-------------for in---------------")
for x,y in obj.items():
    print("key:",x," | value:",y)



print("-------------Check if in---------------")
# check if obj contains a key "age"
if "age" in obj:
    print("age",obj["age"])
    
# check if obj contains a key "userId"
elif "userId" in obj:
    print("userId",obj["userId"])


# add a new property
obj["age"]=12

print("-------------After adding a property---------------")
print(obj)


"""
OUTPUT:
__________________________
{'userId': 1, 'name': 'Bob', 'completed': False, 'hobbies': ['Music', 'Sport'],
'adderss': {'city': 'Ariel', 'country': 'Israel'}}
Bob
{'userId': 1, 'name': 'Alice', 'completed': False, 'hobbies': ['Music', 'Sport'], 'adderss': {'city': 'Ariel', 'country': 'Israel'}}
{'userId': 1, 'completed': False, 'hobbies': ['Music', 'Sport'], 'adderss': {'city': 'Ariel', 'country': 'Israel'}}
dict_items([('userId', 1), ('completed', False), ('hobbies', ['Music', 'Sport']), ('adderss', {'city': 'Ariel', 'country': 'Israel'})])
-------------for in---------------
key: userId  | value: 1
key: completed  | value: False
key: hobbies  | value: ['Music', 'Sport']
key: adderss  | value: {'city': 'Ariel', 'country': 'Israel'}
-------------Check if in---------------
userId 1
-------------After adding a property---------------
{'userId': 1, 'completed': False, 'hobbies': ['Music', 'Sport'], 'adderss': {'city': 'Ariel', 'country': 'Israel'}, 'age': 12}
"""