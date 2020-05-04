
  
# initializing list 
n = [1,2,1,2,1,2,1,2,1]
  
# printing original list 
print("The n : " + str(n)) 
  
# using naive method 
# Separating odd and even index elements 
odd_i = [] 
even_i = [] 
for i in range(0, len(ID)): 
    if i % 2: 
        even_i.append(n[i]) 
    else : 
        odd_i.append(n[i]) 
  
res = odd_i + even_i 
  
# print result 
print("Seprated odd and even index list: " + str(res))