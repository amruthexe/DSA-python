def reverse_number(num):
    reversed_num = 0
    for digit in str(num):
        reversed_num = reversed_num * 10 + int(digit)
    return reversed_num

print(reverse_number(12345))  # Output: 54321


def reverse_number(num):
    return int(str(num)[::-1])

# Example
print(reverse_number(12345))  # Output: 54321
