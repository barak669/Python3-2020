class SchoolMember:

    def __init__(self, name):
        self.name = name

    def tell(self):
        print('hello SchoolMember',self.name)


m1 = SchoolMember("Bob")

m1.tell()
SchoolMember.tell(m1)


m2 = SchoolMember("Alice")

m2.tell()
SchoolMember.tell(m2)

"""
OUTPUT:
____________________________________
hello SchoolMember Bob
hello SchoolMember Bob
hello SchoolMember Alice
hello SchoolMember Alice
<<<<<<< HEAD
"""
=======
"""
>>>>>>> 57dacf9a1dc4f6034bafa0c69e86bd026554bc5b
