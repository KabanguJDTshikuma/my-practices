def duplicate_count(text):
    newText = ''
    add = 0
    for letter in list(text.lower()):
        if (list(text.lower())).count(letter) > 1 and letter not in newText:
            add += 1
            newText += letter
        else:
            add += 0
    return add

print(duplicate_count("aabcdeB"))

