# Write a fn del_char(s,c) that delete all ocurence of c in s
def del_char(str,char):
    if len(char)!=1:
        return str
    new_str=""
    for c in str:
        if(c==char):
            continue
        new_str+=c
    return (new_str)
s = input()
c = input()
print(del_char(s,c))