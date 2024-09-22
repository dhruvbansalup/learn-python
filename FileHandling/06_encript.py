# Encription of file by caeser cipher (letter shifted by 3 letters)
import string

def creat_caesar_dictonary():
    l=string.ascii_lowercase
    l=list(l)
    d={}
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26]
    return d

def encript(file,encripted):
    f=open(file,'r')
    g=open(encripted,'w')
    d=creat_caesar_dictonary()

    c=f.read(1)
    while (c!=''):
        g.write(d[c])
        c=f.read(1)
        
    f.close()
    g.close()    



encript('story.txt','encripted_story.txt')