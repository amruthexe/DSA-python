def pali (s):
    return s==s[::-1]

print(pali("abbaa"))






def palindrome(s):
    r=0
    orginal=s
    while s>0:
        last=s%10
        r=r*10+last
        s//=10
        



def palindrome(s):
    r=""
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

print(palindrome("abba"))
    
    
    
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    
    while num > 0:
        last_digit = num % 10  # Get last digit
        reversed_num = reversed_num * 10 + last_digit  # Build the reversed number
        num //= 10  # Remove the last digit
    
    return original_num == reversed_num  # Check if original and reversed are the same

# Test the function
print(is_palindrome(121))  # Output: True
print(is_palindrome(123))  # Output: False



def is_palindrome(num):
    num_str = str(num)  # Convert number to string
    return num_str == num_str[::-1]  # Check if the string is the same forward and backward

# Test the function
print(is_palindrome(121))  # Output: True
print(is_palindrome(123))  # Output: False




def reverse_string(s):
    reversed_str = ""  # Initialize an empty string to store the reversed string
    for char in s:  # Iterate over each character in the original string
        reversed_str = char + reversed_str  # Prepend the character to the reversed string
    return reversed_str  # Return the reversed string
