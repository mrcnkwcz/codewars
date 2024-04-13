from functools import cache


@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

def perimeter(n):
    return 4 * sum(fib(i) for i in range(n+1))
