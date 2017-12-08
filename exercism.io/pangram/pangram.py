def is_pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvxyzw'
    for letter in letters:
        if letter not in sentence.lower():
            return False
    return True 
