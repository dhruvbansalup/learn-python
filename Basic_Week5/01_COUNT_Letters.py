import string
def upper(sentence):
    upper=0
    for c in sentence:
        if(c.isupper()):
            upper+=1
    return upper

def lower(sentence):
    lower=0
    for c in sentence:
        if(c.islower()):
            lower+=1
    return lower

def words(sentence):
    sentence=sentence.split()
    words=0
    for w in sentence:
        words+=1
    return words

sentence=input("Enter Sentence: ")

print("\nUpper: ",upper(sentence),"\nLower: ",lower(sentence),"\nChar: ",len(sentence),"\n Words: ",words(sentence))


