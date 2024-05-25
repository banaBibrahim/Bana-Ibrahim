def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        if digit != '0' and digit != '1':
            return "Invalid input. Please enter a valid binary number."
        decimal = decimal * 2 + int(digit)
    return decimal

binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)

print(f"The decimal equivalent of {binary_number} is: {decimal_number}")





