def is_isogram(string):
    for char in string:
        if char == ' ' or char == '-':
            continue
        if string.lower().count(char.lower()) > 1:
            return False
    return True
