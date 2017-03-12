def namelist(names):
    a = []
    if len(names) == 1:
        return names[0]['name']
    elif len(names) > 1:
        for i in range(len(names)):
            a.append(names[i]['name'])
        a.insert(-1,'&')
        b = str(a[-3]) + ' ' + str(a[-2]) + ' ' + str(a[-1])
        for i in range(3):
            a.remove(a[-1])
        a.append(b)
        return ', '.join(a)
    else:
        return ''
    
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))    
        
        
