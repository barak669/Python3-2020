# Datetime Module
from datetime import datetime



try:
	read_file = open("last_date.txt", "r")
	print("read:", read_file.read())
	read_file.close()

except FileNotFoundError:
	print("First time of excecution")



write_file = open("last_date.txt", "w")
now = datetime.now()

write_file.write(f"{now.date()} {now.time()}")
write_file.close() 