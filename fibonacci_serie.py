"""Fibonacci series using generator and recursion ."""


def fibonacci_series_using_generator():
    """Create a Fibonacci series using generator"""
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


def fibonacci_series_using_recursion(n):
    """Create a Fibonacci series using recursion"""
    if n <= 1:
        return n
    else:
        return fibonacci_series_using_recursion(n - 1) + fibonacci_series_using_recursion(n - 2)


def main():
    # Generator
    fibo_obj = fibonacci_series_using_generator()  # create object
    for i in range(5):
        print(next(fibo_obj))  # iterate object

    # Recursion
    for i in range(5):
        print(fibonacci_series_using_recursion(i))


if __name__ == '__main__':
    main()
