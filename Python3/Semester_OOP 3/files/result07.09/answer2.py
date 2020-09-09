age=int(input("Enter your age: "))
amount=input("Enter your amount: ")

write_file=open(f"{'soft' if age<18 else 'alcoholic'}_drinks.txt","a")
write_file.write(amount+"\n")
write_file.close()

try:
    toatal_soft_drinks=0
    read_file=open("soft_drinks.txt","r")

    for line in read_file.readlines():
        toatal_soft_drinks+=int(line.split("\n")[0])

    print(f"soft drinks: {toatal_soft_drinks}")
    read_file.close()


except FileNotFoundError:
	print("soft drinks: 0")



try:
    toatal_alcoholic_drinks=0
    read_file=open("alcoholic_drinks.txt","r")

    for line in read_file.readlines():
        toatal_alcoholic_drinks+=int(line.split("\n")[0])

    print(f"alcoholic drinks: {toatal_alcoholic_drinks}")
    read_file.close()

except FileNotFoundError:
	print("alcholic driks: 0")