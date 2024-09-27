# A number is prime product if it can be written as p*q where p & q are both primes

def isprime(n):
    for i in range(2,n):
        if (n%i==0):
            return False
    return True
    
def prime_factors(n):
    fl=[]
    for i in range(2,n+1):
        if (n%i==0 and isprime(i)):
            fl.append(i)
    return fl

def prime_product(n):
    if (len(prime_factors(n))==2)and(prime_factors(n)[0]*prime_factors(n)[1]==n):
        return True
    return False


n = int(input())
print(prime_product(n))