def fibonacci(n):
    fib_sequence = [0,1]
    for i in range(2,n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2] )
    return fib_sequence
def sum_fibonacci_squares(n):
    fib_sequence = fibonacci(n)
    sum_sequence = sum(x**2 for x in fib_sequence)
    return sum_sequence
n = 50
sum_of_square = sum_fibonacci_squares(n)
print("The sum of 50 square of fibonacci is :",sum_of_square)