ID = (input("Enter your ID: "))
w = [1,2,1,2,1,2,1,2,1]
counter=0



while counter<len(ID):
    sum = int(ID[1]) * (w[counter])
    print(sum)
    counter+=1

