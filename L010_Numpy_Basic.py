import numpy as np

zeromatrix = np.zeros((3, 3))
print("zeromatrix",zeromatrix)

newarray = np.array([[1, 2],[ 4, 5]])
print("newarray",newarray)

row2=np.arange(5)
print("row2",row2)


A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
C=3*A + B
print("3A+B",C)
C=np.matmul(A,B) # Matrix Multiplication
print("AB",C)