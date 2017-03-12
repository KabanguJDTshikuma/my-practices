#word = ''

def capitals(word):
    a = []
    for i in word:
        if i.isalpha() and i.isupper():
            word.index(i)
            a.append(word.index(i))
    return a

print(capitals('cHris MuLumba'))
        
    

            
            
