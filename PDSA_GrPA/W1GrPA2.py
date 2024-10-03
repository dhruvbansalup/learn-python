# Goldbach's conjecture
# Every even no greater than 2 is the sum of two prime no

def isprime(m):
    if m==1:
        return False
    result=True
    for i in range(2,m):
        if(m%i)==0:
            result=False
            break
    return result

def prime_list(n):
    """Return list of prime upto n"""
    pl=[]
    for i in range(1,n):
        if isprime(i):
            pl.append(i)
    return pl
        

def Goldbach(n):
    primes=prime_list(n)
    pairs=[]
    for p in primes:
        t=n-p
        if t in primes:
            if tuple([t,p]) not in pairs:
                pairs.append(tuple([p,t]))
    return pairs

n=int(input())
print(sorted(Goldbach(n)))
