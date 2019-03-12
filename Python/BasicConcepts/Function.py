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

'''Default Argument values'''


def ask_ok(prompt, retries=4, reminder='Please try again!!!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user Response')
        print(reminder)


ask_ok('Do you really want to quit?')

'''Lambda Expressions'''


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(10))

'''Documentation String'''


def documentation():
    """Do nothing, but document it.

    No really it does not do nothing
    """
    pass


print(documentation.__doc__)
