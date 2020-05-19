# When we apply ** to a dictionary, then it expands the contents in dictionary as a collection of key value pairs.


dict1 = {'Ritika': 5, 'Sam': 7, 'John' : 10 }
dict2 = {'Aadi': 8,'Sam': 20,'Mark' : 11 }
dict3 = {'Mark': 18,'Rose': 22,'Wong' : 22 }


# Merge contents of dict3, dict2 and dict1 to dict4
dict4 = {**dict1, **dict2, **dict3}
 
print('Dictionary 4 :')
print(dict4)