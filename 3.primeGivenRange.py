prime=lambda str,stp : [n for n in range(str,stp+1) if n>1 and all( n%i !=0 for i in range(2,int(n**0.5)+1))]

print(prime(2,30))






def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage:
print(primes_in_range(10, 50))  # Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
