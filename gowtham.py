def fibonacci(n):
    fib_series = []
    a, b = 0, 1  # First two Fibonacci numbers

    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
    
    return fib_series

# Example: Generate the first 10 Fibonacci numbers
n = 10
result = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {result}")
