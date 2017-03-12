def unique_in_order(iterable):
    table = []
    for letter in iterable:
        if len(table) == 0: table.append(letter)
        elif letter != table[(len(table)-1)]: table.append(letter)
        elif letter == table[(len(table)-1)]: continue
    return table
print(unique_in_order('AAAABBBCCDAABBB'))
 
