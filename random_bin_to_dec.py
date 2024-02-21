import random
def generate_binary():
    binary_numbers = ""
    for _ in range(4):
        binary_numbers += str(random.randint(0,1))
    print(binary_numbers)
    return binary_numbers
def bin_to_decimal(binary_numbers):
    decimal_numbers = int(binary_numbers,2)
    return decimal_numbers
    
random_binary = generate_binary()
print("The binary number generated is:",random_binary)

decimal_number = bin_to_decimal(random_binary)
print("The decimal of the generated binary is:",decimal_number)