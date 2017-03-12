def likes(names):
    if len(names) == 1:
        return names[0] + ' likes this'
    elif len(names) == 2:
         return  str(names[0]) + ' and ' + str(names[1]) + ' like this'
    elif len(names) == 3:
        return str(names[0]) + ', ' + str(names[1]) + ' and ' + str(names[2]) + ' like this' 
    elif len(names) > 3:
        return  str(names[0]) + ', ' + str(names[1]) + ' and ' + str(len(names) - 2) + ' others like this'
    else:
        return 'no one likes this'

print(likes(['Dadi', 'soso', 'lody', 'damimi']))
    
