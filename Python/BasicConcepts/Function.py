'''Print fibonacci series up to n
using function 'fib' '''


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a + b
    print()


''' Now call the function fib
and print the results'''

# fib(200)

if round(.1 + .1 + .1, 10) == round(.3, 10):
    print("pass")
