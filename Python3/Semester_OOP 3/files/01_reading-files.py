try:
	# opens an exsiting file in read mode
	# Note: if No such file or directory we get: FileNotFoundError
	my_opened_file = open("myfile.txt", "r")


	#is file readable (return boolean value)
	print("readable:", my_opened_file.readable())

	# get all the data from the file using read()
	print("read:", my_opened_file.readlines())

	#close the opened file
	my_opened_file.close()

except FileNotFoundError as ex:
	print(ex)


print("End of app")





"""
s=open('text.txt', 'r')
line = s.readline()
while line != '':
	lcnt += 1
	for ch in line:
		print(ch, end='')
		ccnt += 1
	line = s.readline()
lines = s.readlines(20)
The iteration protocol defined for the file object is very simple - its __next__ method just returns the next line read in from the file.
Moreover, you can expect that the object automatically invokes close() when any of the file reads reaches the end of the file.
from os import strerror
try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'r'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))
"""