def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number <= limit:
            fibonacci_sequence.append(next_number)
        else:
            break
    return fibonacci_sequence
    
limit = int(input("Enter the limit for Fibonacci numbers: "))
fibonacci_numbers = generate_fibonacci(limit)
print("Fibonacci sequence up to {}:".format(limit))
print(fibonacci_numbers)                
