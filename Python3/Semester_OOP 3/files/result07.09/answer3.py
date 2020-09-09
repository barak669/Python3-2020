  
file_path=input("Enter your file path: ")


try:
    read_file=open(file_path,"r")
    write_file=open("copy.txt","w")

    for line in read_file.readlines():
        if(len(line)>6):
            write_file.write(line)

    write_file.close()
    read_file.close()


except FileNotFoundError:
	print("No such file")