// # Sequência de Fibonacci 
// # F(n) = F(n - 1) + F(n - 2)

function fibonacci(n: number): number[] {
    let fib: number[] = [];
    // Inicialização; Condição de parada; Incremento
    for (let i = 0; i != (n + 1); i++) {
        if (i < 2) {
            fib.push(i);
        } else {
            fib.push(fib[i-1] + fib[i-2])
        }
    } return fib
}

console.log(fibonacci(10))