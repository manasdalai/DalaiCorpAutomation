''' While loop '''
a = 0
while a < 10:
    print(a)
    a = a + 1

'''Fibonacci Series'''
a, b = 0, 1
while a < 10:
    # print(a)
    print(a, end=',')
    a, b = b, a + b

'''print multiple lines'''
print(""" \n This is 
multilayer print
statement """)

'''if condition'''
a = 12
if a < 10:
    print(a)
elif a > 10:
    print(a)
else:
    print(a)
