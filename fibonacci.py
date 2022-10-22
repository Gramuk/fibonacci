fib_dict = {}

def fib(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return fib(n-1) + fib (n-2)

def fastfib(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n-1] = fastfib(n-1)
        fib_dict[n-2] = fastfib(n-2)
        return fib_dict[n-1] + fib_dict[n-2]
    