# Sequência de Fibonacci 
# F(n) = F(n - 1) + F(n - 2)

def fibonacci(n: int) -> list[int]:
    fib: list[int] = []
    for i in range(0, n + 1):
        if i < 2:
            fib.append(i)
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib

# Fibonacci recursivo
def recursive_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


# Fibonacci: 0 1 1 2 3 5 8 13 ...      

n = int(input("Número para a sequência de Fibonacci: "))
print(fibonacci(n))
