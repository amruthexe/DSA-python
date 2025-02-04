def is_armstrong(number):
    # Convert the number to a string to get each digit
    digits = [int(d) for d in str(number)]
    power = len(digits)  # The number of digits determines the power
    armstrong_sum = sum([digit ** power for digit in digits])  # Sum of digits raised to the power
    return armstrong_sum == number  # Check if the sum equals the number

# Input: Get a number from the user
num = int(input("Enter a number: "))