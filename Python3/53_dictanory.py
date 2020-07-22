obj={
  "userId": 1,
  "name": "Bob",
  "completed": False,
  "hobbies":["Music","Sport"]
}


print(list(obj.items()))          #-> dict_items([('userId', 1), ('name', 'Bob'), ('completed', False), ('hobbies', ['Music', 'Sport'])])

print(list(obj.keys()))           #-> dict_keys(['userId', 'name', 'completed', 'hobbies'])

print(list(obj.values()))         #-> dict_values([1, 'Bob', False, ['Music', 'Sport']])

first_pair=list(obj.items())[0]
print(first_pair)                 #-> ('userId', 1)

first_key, first_val=first_pair
print("first_key=",first_key,", first_val=",first_val) #-> first_key= userId , first_val= 1