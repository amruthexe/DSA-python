def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Add the last digit
        n //= 10  # Remove the last digit
    return total

# Example usage:
print(sum_of_digits(12345))  # Output: 15



def sum_of_digits(n):
    total = 0
    for digit in str(n):  # Loop through each character of the number (as a string)
        total += int(digit)  # Convert each character back to an integer and add to total
    return total

# Example usage:
print(sum_of_digits(12345))  # Output: 15
