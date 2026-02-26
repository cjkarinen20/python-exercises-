def is_pangram(sentence):
    EACH_LETTER = []
    for index, item in enumerate(sentence):
        if item not in EACH_LETTER:
            EACH_LETTER.append(item)
    if len(EACH_LETTER) == 26:
        return True
    elif len(EACH_LETTER) < 26:
        return False
        
if __name__ == "__main__":
    print('Enter a sentence: ')
    sentence = input()
    if is_pangram(sentence) == True:
        print('That sentence is a pangram.')
    elif is_pangram(sentence) == False:
        print('That sentence is not a pangram.')

