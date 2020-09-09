#open file 
# r - read mode (file must exist)
# w - write mode
# a - append mode (append to the end of the file)
# r+ - read and write
# w+ - write and update


# create a new file (if file does not exist) in append mode
my_opened_file = open("myfile.txt", "a")
# add a new line in the file
my_opened_file.write("\nhello line 1")
my_opened_file.write("\nhello line 2") 
my_opened_file.write("\nhello line 3")  
my_opened_file.write("\nhello line 4") 
my_opened_file.close()


# create a new file (if file does not exist) in write mode
my_new_file = open("my_new_file", "w")
# add contents to new file, if file exists it will overwrite its contents
my_new_file.write("Bob")
my_new_file.close()