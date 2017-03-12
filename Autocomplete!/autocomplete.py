def autocomplete(input_, dictionary):
    auto = list()
    names = ''
    symbol = "~`!@#$%^&*()_+={}[]:>;',</?*-+"
    if len(dictionary) == 0:
        return ['Nopesville']
    for name in dictionary:
        for letter in name:
            if letter.isalpha() or letter == '-':
                names += letter
            elif letter in symbol:
                names += ''
                del letter
        if names.upper().startswith(input_.upper()):
            auto.append(names)
        names =''
        if len(auto)== 5:
                break
    return auto
    
dictionary=['abnormal',
              'arm-wrestling',
              'abso2lute',
              'airplane',
              'airport',
              'amazing',
              'apple',
              'ball']
print (autocomplete('air', dictionary))
            
