#factorial and fibonacci by recursion

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
