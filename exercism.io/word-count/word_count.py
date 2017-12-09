def word_count(phrase):
    phrase = "".join(c for c in phrase if c not in ('!','.',':','&','@','$','%','^'))
    for char in phrase:
        if char in (',','\n','\t','_'):
            phrase = phrase.replace(char,' ')
    words = [word.strip("'") for word in phrase.lower().split()]
    result = {}
    for word in words:
        if word.count("'") > 1:
            word = word.replace("'","")
        if word not in result:
            result[word.lower()] = words.count(word)
    return result
