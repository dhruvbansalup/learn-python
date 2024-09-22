
def initalize_matrix(n):
    m=[]
    for i in range (n):
        m.append([])
    for i in range(n):
        for j in range(n):
            m[i].append(0)
    return m

def dot_product(a,b):
    val=0
    if len(a)==len(b):
        for i,j in zip(a,b):
            val+=i*j
    return val
    

def row(M,i):
    return(M[i])

def column(M,j):
    l=[]
    for r in M:
        l.append(r[j])
    return l

def matrix_multiplication(a,b):
    if len(a)!=len(b):
        return("Not Possible")

    dim=len(a)
    ans=initalize_matrix(dim)

    for i in range(dim):
        for j in range(dim):
            ans[i][j]=dot_product(row(a,i),column(b,j))

    return ans


A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[2,3,4],[3,5,7],[2,7,8]]

print(matrix_multiplication(A,B))
    
import numpy
A=numpy.mat(A)
B=numpy.mat(B)
C=A*B

print(C)

