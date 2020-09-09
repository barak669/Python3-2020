  
def is_equal(f1,f2):
    try:
        read_file1=open(f1,"r")
        read_file2=open(f2,"r")

        return 0 if (read_file1.read()!=read_file2.read()) else 1

    except FileNotFoundError:
        return -1


file_path_1=input("Enter your first file path: ")
file_path_2=input("Enter your second file path: ")
print(is_equal(file_path_1,file_path_2))