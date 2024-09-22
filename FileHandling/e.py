def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    
    f=open(filename,'r')
    Dict={}
    
    for word in f.read().splitlines():
        if word not in Dict.keys():
            Dict[word]=1
        else:
            Dict[word]=Dict[word]+1
            
    return Dict

print(get_freq('words.txt'))