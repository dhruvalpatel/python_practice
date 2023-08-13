def fibonacci_series_generator(n):
    x, y = 0, 1
    while True:
        yield x
        x, y = y, y + x
        if x >= n:
            break


fib_obj = fibonacci_series_generator(3)
print(next(fib_obj))
print(next(fib_obj))
print(next(fib_obj))
print(next(fib_obj))


def fibonacci_series_using_recursion(n):
    """This function is used to return the current value at nth place. e.g n=5, value=5(0 1 1 2 3 5)"""
    if n <= 1:
        return n
    else:
        return fibonacci_series_using_recursion(n - 1) + fibonacci_series_using_recursion(n - 2)


print(fibonacci_series_using_recursion(5))


# Optimized version of a Fibonacci version:

def fibonacci(n):
    a = 0
    b = 1

    if n == 0:
        return 0

    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(4))
