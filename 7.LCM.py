# Function to find HCF using Euclid's algorithm
def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find LCM of two numbers
def find_lcm(a, b):
    hcf = find_hcf(a, b)  # First, find the HCF
    return abs(a * b) // hcf  # LCM formula

# Example usage
num1 = 36
num2 = 60
lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
