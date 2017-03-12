def to_currency(price):
    a = str(price)
    b = ''
    c= 0
    if len(a)>3:
        for i in a:
            if (c%3 == 0) and(c <(len(a))):
                    b = b + i + ','
            
            else:
                b = b+i
            c = c+1
            
            
            
           
    return b
price1 = 123456
print(to_currency(price1))
    
                
        
