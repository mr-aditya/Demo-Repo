def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

# Get input from the user
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# Display the Fibonacci sequence
result = fibonacci(n)
print(f"Fibonacci Sequence up to {n}-th term: {result}")
