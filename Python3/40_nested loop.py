counter=3

while counter<6:
    print("counter",counter, "-------------")
    inner_counter=1

    while inner_counter<=counter:
        print(inner_counter)
        inner_counter+=1

    counter+= 1


"""
OUTPUT:
_________________________
counter 3 -------------
1
2
3
counter 4 -------------
1
2
3
4
counter 5 -------------
1
2
3
4
5
"""