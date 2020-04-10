ID = (input("Enter your ID: "))

n = [1,2,1,2,1,2,1,2,1]
  
  
odd_i = [] 
even_i = [] 
for i in range(0, len(ID)): 
    if i % 2: 
        even_i.append(n) 
    else : 
        odd_i.append(n) 
  
res = odd_i + even_i 

print(ID)
print(res)