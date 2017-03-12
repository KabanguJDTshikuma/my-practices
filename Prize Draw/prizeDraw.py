def rank(st, we, n):
    import string
    alphabet = string.ascii_lowercase
    table = st.split(',')
    long = 0
    for i in table:
        f = i.lower()
        for letter in f:
            d = alphabet.index(letter)
            drow = len(i) + d
        winner = drow * n
        if winner > long:
            long = drow
        drow = 0
    return i, winner
y =rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)
print(y)
            
     
        
    
