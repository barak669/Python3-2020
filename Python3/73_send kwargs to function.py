def sum(x0=0,x1=1,x2=2,x3=3):
    print(f"{x0} + {x1} + {x2} + {x3} = {x1+x2+x3}")


obj={
    "x1":4,
    "x2":5,
    "x3":6
}


################# first way: (send named paramter by dict key) ################
sum(x1=obj["x1"],x2=obj["x2"],x3=obj["x3"])       #-> 0 + 4 + 5 + 6 = 15

################# second way: (send named paramter by with kwargs) ############
sum(**obj)                                         #-> 0 + 4 + 5 + 6 = 15