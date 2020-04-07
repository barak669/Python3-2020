non_corona_countries=None
countries=["China","Isreal","Italy","Germany"]
death_counter=[1500,1,5000,40]

print(countries)                #--> ['China', 'Isreal', 'Italy', 'Germany']
print(death_counter)            #--> [1500, 1, 5000, 40]


print(countries[1])             #--> 'Isreal'
print(death_counter[0])         #--> 1500

print(non_corona_countries)     #--> None

death_counter[0]=1890
print(death_counter)            #--> [1890, 1, 5000, 40]