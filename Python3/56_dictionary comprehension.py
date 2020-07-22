
# Dictionary comprehension is a method for transforming one dictionary into another dictionary. During this transformation, 
# items within the original dictionary can be conditionally included in the new dictionary and each item can be transformed as needed.


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)


# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}
print(dict1_cond)

# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
print(dict1_tripleCond)