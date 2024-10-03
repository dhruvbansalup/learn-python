
# Check prime no
def factors(n):
    fl=[]
    for i in range(1,n+1):
        if (n%i)==0:
            fl.append(i)
    return fl
def prime(n):
    return(factors(n)==[1,n])

# Second Method check prime
def prime(m):
    result=True
    for i in range(2,m):
        if(m%i)==0:
            result=False
            break
    return result
# Faster algorithm
import math
def prime(n):
    result,i=True,2
    while(result and (i<math.sqrt(n))):
        if n%i ==0:
            result=False
        i=i+1
    return result




# Prime no upto a number
def primeupto(m):
    pl=[]
    for i in range(1,m+1):
        if prime(i):
            pl.append(i)
    return pl

# First n Prime no
def firstprimes(m):
    count,i,pl=0,1,[]
    while count<m:
        if prime(i):
            count,pl=count+1,pl+[i]
        i=i+1
    return pl



#Check Distribution of prime numbers
# Defference b/w each primes
def primediffs(n):
    lastprime=2
    pd={}#Dictonary for prime differences
    for i in range(3,n+1):
        if prime(i):
            d=i-lastprime
            lastprime=i
            if d in pd.keys():
                pd[d]=pd[d]+1
            else:
                pd[d]=1
    return (pd)




