def stockList(listOfArt, listOfCat):
    if listOfArt == '':
        return ""
    a = []
    addition = 0
    for y in listOfCat:
        for i in range(len(listOfArt)):
            if listOfArt[i].startswith(y):
                (listOfArt[i].split())[1]
                addition += int((b[i].split())[1])
        e = '({} : {})'.format(y, str(addition))
        a.append(e)
        addition = 0
    return ' - '.join(a)

b = ["CBART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
c = ["A", "B", "C", "W"]
print(stockList(b, c))
    
    

        

    

        

    
        
    
    
            
        
    




        
