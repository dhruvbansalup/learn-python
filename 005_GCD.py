# Calculate GCD for 2 numbers
def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            cf.append(i)
    return cf[-1]

def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            mrcf=i
    return mrcf


#Method -2
def gcd(m,n):
    a,b=max(m,n),min(m,n)
    if a%b==0:
        return(b)
    else:
        return(gcd(b,a-b))
    

#Faster method - Euclid's Algorithm
def gcd(m,n):
    a,b=max(m,n),min(m,n)
    if a%b==0:
        return b
    else:
        return(gcd(b,a%b))