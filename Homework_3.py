""" Write a program that takes a 3 word phrase
and then converts the words to Pig Latin. """

VOWELS = ['a', 'e', 'i', 'o', 'u']


def AskUserForSentence():
    """ Ask user for sentence and convert to Pig Latin"""
    while True:
        sentence = raw_input('Input a 3 words sentence. Type "QUIT" to end: ')
        if sentence == 'QUIT' or sentence == 'quit':
            break
        else:
            lower_version = LowercaseSentence(sentence)
            split_sentence = SplitSentenceIntoList(lower_version)
            if len(split_sentence) != 3:
                print ('It it not a 3 words sentence. '
                       'Please input a 3 words sentence '
                       'or type "QUIT" to end: ')
                continue
            else:
                pig_latin = ConvertWordToPigLatin(split_sentence)
                PrintThreeWordPhrase(pig_latin)


def LowercaseSentence(sentence):
    """ converts a sentence string to all lowercase letters """
    lower_version = sentence.lower()
    return lower_version


def SplitSentenceIntoList(sentence):
    """ splits a string into a list """
    split_sentence = sentence.split()
    return split_sentence


def ConvertWordToPigLatin(sentence):
    """ convert word to Pig Latin """
    consonants_end = 'ay'
    vowels_end = 'hay'

    first_word = sentence[0]
    second_word = sentence[1]
    third_word = sentence[2]

    pig_latin_list = []

    if first_word[0] in VOWELS:
        pig_latin_list.append(first_word + vowels_end)
    else:
        pig_latin_list.append(first_word[1:] + first_word[0] + consonants_end)
    if second_word[0] in VOWELS:
        pig_latin_list.append(second_word + vowels_end)
    else:
        pig_latin_list.append(second_word[1:] + second_word[0] + consonants_end)
    if third_word[0] in VOWELS:
        pig_latin_list.append(third_word + vowels_end)
    else:
        pig_latin_list.append(third_word[1:] + third_word[0] + consonants_end)

    return pig_latin_list


def PrintThreeWordPhrase(sentence):
    """ print three word phrase """
    join_sentence = " ".join(sentence)
    print('Translate to Pig Latin: ' + join_sentence)


AskUserForSentence()
