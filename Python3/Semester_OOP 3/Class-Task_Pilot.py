class Person:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_info(self):
        print(f"{self.first_name} , {self.last_name}", end=" ")


class Pilot(Person):
    def __init__(self, first_name, last_name, lic_num, ex_years):
        Person.__init__(self,first_name, last_name)
        self.lic_num = lic_num
        self.ex_years = ex_years

    def print_info(self):
        Person.print_info(self)
        print(f"{self.lic_num} , {self.ex_years}")

class Passanger(Person):
    def __init__(self, first_name, last_name, id):
        Person.__init__(self, first_name, last_name)
        self.id = id

    def print_info(self):
        Person.print_info(self)
        print(f"{self.id}")

pilot=Pilot("Bob", "AB" , "1234", 7)
passanger=Passanger("Alice", "CD", "012")

pilot.print_info()
passanger.print_info()
