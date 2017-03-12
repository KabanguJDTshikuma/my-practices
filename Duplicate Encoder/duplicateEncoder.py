def duplicate_encode(word):
    c = word.lower()
    encoder = ''
    for i in c:
        #if i.isupper():
            #encoder += ''
        if c.count(i) == 1:
            i = '('
            encoder += i
        else:
            i = ')'
            encoder += i
    return encoder
a = duplicate_encode("Success")
print(a)
