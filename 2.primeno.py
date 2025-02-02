def prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**(0.5))+1):
            if n%i==0:
                return False
        return True
print(prime(8))



"""
    The check if i % n == 0 should be if n % i == 0, because you want to check if n is divisible by i, not the other way around.
    "A prime number is a number greater than 1 that has no divisors other than 1 and itself. So, to check if a number is prime:
"""


def prime (n):
    return n>1 and all(n%i !=0 for i in range(2,int(n**0.5)+1))

print(prime(3))


# without for loop


def prime (n,i=2):
    if n<=1:
        return False
    if i*i >n:
        return True
    if n%i==0:
        return False
    return prime(3,i+1)

print(prime(50))