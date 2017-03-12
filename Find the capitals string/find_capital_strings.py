def capitals(word):
    a=[]
    for cap in word:
        if cap == ' ' and word.index(cap) not in a:
            a.append(word.index(cap))
        elif cap.isdecimal() and word.index(cap) not in a:
            a.append(word.index(cap))
        elif cap.isupper() and word.index(cap) not in a:
            a.append(word.index(cap))
            
    return a
    
print(capitals('CodE Wa2RsW'))
