def AskForLetter():
    ''' This function will repeatly as the user for a single letter
    until the user types 'quit' to exit the program
    or they have entered a vowel. '''
    while True:
        letter = raw_input("Enter a single letter; or type 'quit' to exit ")
        if letter == 'quit':
            break
        elif len(letter) == 1:
            is_vowel = IsVowel(letter)
            if is_vowel is True:
                print letter, "is a vowel"
            else:
                print letter, "is not a vowel"
        else:
            print "It is not a single letter. Please enter a single letter."

def IsVowel(letter):
    ''' This function will take as input a variable called letter
    and will determine if this letter is a vowel or not. '''
    lower_case = IsLowerCaseVowel(letter)
    upper_case = IsUpperCaseVowel(letter)
    if lower_case is True or upper_case is True:
        return True
    else:
        return False

def IsLowerCaseVowel(letter):
    ''' This function will take a single variable as input called letter
    and will return True if the letter is an lowercase vowel. '''
    if letter == 'a':
        return True
    elif letter == 'e':
        return True
    elif letter == 'i':
        return True
    elif letter == 'o':
        return True
    elif letter == 'u':
        return True
    else:
        return False

def IsUpperCaseVowel(letter):
    ''' This function will take a single variable as input called letter
    and will return True if the letter is an uppercase vowel. '''
    if letter == 'A':
        return True
    elif letter == 'E':
        return True
    elif letter == 'I':
        return True
    elif letter == 'O':
        return True
    elif letter == 'U':
        return True
    else:
        return False

AskForLetter()
