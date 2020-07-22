def print_params(msg, *numbers, **pairs):
    print("msg:",msg,", numbers:",numbers,", pairs:",pairs)


print_params("hello",1,2,3,4,"TEST",name="bob",age=13)           #-> msg: hello , numbers: (1, 2, 3, 4, 'TEST') , pairs: {'name': 'bob', 'age': 13}
print_params("bye")                                              #-> msg: bye , numbers: () , pairs: {}
print_params("hi",day="Mon")                                     #-> msg: hi , numbers: () , pairs: {'day': 'Mon'}
print_params("see-you","Bob","Alice")                            #-> msg: see-you , numbers: ('Bob', 'Alice') , pairs: {}