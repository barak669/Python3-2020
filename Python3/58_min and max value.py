import sys
print(sys.maxsize) #  9223372036854775807

a=sys.maxsize + 1
print(type(a),a)


import sys
print(sys.float_info.max)

b=sys.float_info.max + 1
print(type(b),b)


import sys
print(sys.float_info)

c=sys.float_info + 1
print(type(c),c)