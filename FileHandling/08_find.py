f=open("data1.txt",'r')
s='0'
flag=0
while(s!=''):
    n=int(s)
    s=f.readline()
    if (n==9084313525):
        print("The number was found")
        flag=1
        break

if (flag==0):
    print("Not Found")