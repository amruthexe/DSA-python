def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
    
    
print(fact(5))



def fact(n):
    res=1
    if n==0 or n==1:
        return 1
    else:
        for i in range(2,n+1):
            res*=i
        return res
    
    
print(fact(5))