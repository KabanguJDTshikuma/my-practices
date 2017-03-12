def alphabet_position(text):
    text = text.lower()
    import string
    alpha = string.ascii_lowercase
    b = []
    for i in text:
        if i in alpha:
            b.append(str((1 + alpha.index(i))))
       
    return (' '.join(b))

a = alphabet_position("The sunset sets at twelve o' clock.")
print(a)


    
       
            


            
