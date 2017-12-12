def decode(string):
    result = ''
    num = ''
    for c in string:
        if c.isdigit():
            num = num + c
        elif len(num) > 0:
            result = result + (c * int(num))
            num = ''
        else:
            result = result + c
    return result

def encode(string):
    count = 1
    letter = ''
    result = ''
    if string == '':
        return ''
    for i in range(1, len(string)):
        if string[i-1]==string[i]:
            count += 1
        else:
            if count == 1:
                num = ''
            else:
                num = str(count)
            result += num + string[i-1]
            count = 1
    if count == 1:
        num = ''
    else:
        num = str(count)
    result += num + string[i]
    return result 
