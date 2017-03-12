def title_case(title, minor_words = ''):
    if title == '': return ''
    morecase = minor_words.lower()
    minor = morecase.split()
    string = title.split()
    titlecase = string[0].title()
    string.remove(string[0])
    for word in string:
        if word.lower() in minor:
            titlecase += ' ' + word.lower()
        else:
            titlecase += ' ' + word.title()
    return titlecase

print(title_case('THE WIND IN THE WILLOWS', 'The In'))
        
        
        
        
    
