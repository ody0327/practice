n = int(input("> "))

def factorial(n):
    for i in range(1, n):
        n *= i
    return n

print(factorial(n))