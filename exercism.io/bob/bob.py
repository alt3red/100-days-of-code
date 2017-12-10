def hey(phrase):
    if '' == phrase.strip():
        return 'Fine. Be that way!'
    elif phrase.strip().isupper():
        return 'Whoa, chill out!'
    elif phrase.strip()[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'
    
