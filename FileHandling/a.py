def do_something(filename, sub):
    f = open(filename, 'r')
    # Ignore the header
    f.readline()	
    # we are now at the beginning of the second line of the file
    val, count = 0, 0
    
    for line in f:
        sno, name, gender, ct, python, pdsa = line.strip().split(',')
        sno, ct, python, pdsa = int(sno), int(ct), int(python), int(pdsa)
        if sub == 'CT':
            val = val + ct
        elif sub == 'Python':
            val = val + python
        elif sub == 'PDSA':
            val = val + pdsa
        count = count + 1
        
    f.close()
    return val / count

# Hint: int(1.5) is 1
print(int(do_something('scores.csv', 'Python')))