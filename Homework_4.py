""" Write a program that will ask the user to input the names of cities they would like to visit. 
This means that the program should ask the user first how many cites they want to input (function - AskForNumberCities).
Then the program should allow the user to input this and only this number of cities (function - AskForCityName).
If they input the same city name you should not count that as one of the cities.
You only need to consider cities spelled EXACTLY the same way (e.g. Haifa and Haifa).
Do not worry about upper and lowercase characters in city names. """


def AskForNumberCities():
    """ ask the user first how many cites they want to input """

    while True:
        number = raw_input('How many cites you would like to visit? ')
        try:
            number_cities = int(number)
            return number_cities
        except ValueError:
            print 'The input value is invalid. Please input a valid number.'
            continue


def AskForCityName(number):
    """ allow the user to input this and only this number of cities
    also the city must be unique, that means the list cannot contain the same city name """

    name_cities = []
    for i in range(number):
        city = raw_input('Please input the names of cities you would like to visit: ')
        if city not in name_cities:
            name_cities.append(city)

    return name_cities


def PrintFirstCitySentence(city_list):
    """ print a sentence that looks exactly like the following:
     'You would like to visit Tel Aviv as city 1 and Haifa as city 2 and Negev as city 3 on your trip.' """

    short_sentence = []

    for i in range(len(city_list)):
        short_sentence.append(city_list[i] + ' as city ' + str(i+1))

    combine_sentence = " and ".join(short_sentence)

    whole_sentence = 'You would like to visit ' + combine_sentence + ' on your trip.'

    print whole_sentence

    return whole_sentence


def PrintAddOneCityNumSentence(sentence):
    """ take the sentence string and add 1 to each city number and then output the string with the changes:
    'You would like to visit Tel Aviv as city 2 and Haifa as city 3 and Negev as city 4 on your trip.' """

    split_sentence = sentence.split()

    for i in range(len(split_sentence)):
        if split_sentence[i].isdigit():
            index = int(split_sentence[i]) + 1
            split_sentence[i] = str(index)

    print " ".join(split_sentence)


def Run():
    number = AskForNumberCities()
    cities = AskForCityName(number)
    sentence = PrintFirstCitySentence(cities)
    PrintAddOneCityNumSentence(sentence)


Run()
