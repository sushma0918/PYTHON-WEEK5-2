def fibonacci_iterative(n):
    a, b = 0, 1
    print("Fibonacci Series (Iteration):")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
# Fibonacci using recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input("Enter the number of terms: "))
fibonacci_iterative(n)
print("Fibonacci Series (Recursion):")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")


