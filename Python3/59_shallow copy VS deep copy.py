obj={
  "userId": 1,
  "hobbies":["Music","Sport"]
}

obj_copy=obj

obj_shallow_copy={
  "userId": obj["userId"],
  "hobbies": obj["hobbies"]
}

obj_deep_copy={
  "userId": obj["userId"],
  "hobbies": [ obj["hobbies"][0], obj["hobbies"][1] ]
}


print(obj)                  # {'userId': 1, 'hobbies': ['Music', 'Sport']}
print(obj_copy)             # {'userId': 1, 'hobbies': ['Music', 'Sport']}
print(obj_shallow_copy)     # {'userId': 1, 'hobbies': ['Music', 'Sport']}
print(obj_deep_copy)        # {'userId': 1, 'hobbies': ['Music', 'Sport']}


obj["userId"]=99

print(obj)                  # {'userId': 99, 'hobbies': ['Music', 'Sport']}
print(obj_copy)             # {'userId': 99, 'hobbies': ['Music', 'Sport']}
print(obj_shallow_copy)     # {'userId': 1, 'hobbies': ['Music', 'Sport']}
print(obj_deep_copy)        # {'userId': 1, 'hobbies': ['Music', 'Sport']}


obj["hobbies"][0]="Cyber"


print(obj)                  # {'userId': 99, 'hobbies': ['Cyber', 'Sport']}
print(obj_copy)             # {'userId': 99, 'hobbies': ['Cyber', 'Sport']}
print(obj_shallow_copy)     # {'userId': 1, 'hobbies': ['Cyber', 'Sport']}
print(obj_deep_copy)        # {'userId': 1, 'hobbies': ['Music', 'Sport']}