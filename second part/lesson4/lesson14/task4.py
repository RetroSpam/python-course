def fibonacci_price_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b
        
fib_gen = fibonacci_price_generator()
for _ in range(10):
    print(next(fib_gen))