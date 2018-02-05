# Python_Beginners
### Homework 1 - Python
####
Write a program that asks the user for their dream job title. Then ask them for the hourly wage they want to earn. This number should account for dollars and cents. Calculate the annual wage they will earn over a year. Assume they work 48 weeks a year (4 weeks vacation) but are paid over 52 weeks. Then ask them how much money they feel they will need at retirement time. Determine the number of years they will have to work to save up their retirement dollar value assuming their only source of income was their paycheck? Finally, determine if the number of years they need to save is an even or odd number. 
### Homework 2 - Python
####
Write a program that asks the user for a letter. The program should then determine if the letter is a vowel or not.
In this homework you will, of course, be writing functions to perform the individual components of the program.

### Homework 3 - Python
####
Write a program that takes a 3 word phrase and then converts the words to Pig Latin.
To review, Pig Latin takes the first letter of a word, puts it at the end, and appends “ay”. The only exception is if the first letter is a vowel, in which case we keep it as it is and append “hay” to the end.
E.g. “boot” → “ootbay”, and “image” → “imagehay”.

### Homework 4 - Python
####
Write a program that will ask the user to input the names of cities they would like to visit. This means that the program should ask the user first how many cites they want to input (function – AskForNumberCities). Then the program should allow the user to input this and only this number of cities (function - AskForCityName). If they input the same city name you should not count that as one of the cities. You only need to consider cities spelled EXACTLY the same way (e.g. Haifa and Haifa). Do not worry about upper and lowercase characters in city names.
After all the cities have been collected the program should then print a sentence that looks exactly like the following (function - PrintFirstCitySentence):
“You would like to visit Tel Aviv as city 1 and Haifa as city 2 and Negev as city 3 on your trip.”
Next the program will take this sentence string and add 1 to each city number and then output the string with the changes (function – PrintAddOneCityNumSentence). For example,
“You would like to visit Tel Aviv as city 2 and Haifa as city 3 and Negev as city 4 on your trip.”

### Homework 5 - Python
####
##### Part 1:
Write a module that has the following functions. Make sure you read carefully the requirements for these functions and follow them EXACTLY. Name this homework_5_solution_module.py.
1. Function called AskForFileName( ) that will ask the user for the name of the input file(1JKB.pdb). Make sure you put all files in the same directory/folder as this python program.
2. Function called ReadFileContents(file_name ) that will open the file and read all the lines in the file into memory. Name this variable all_file_contents.
3. Function called BuildHeadList(all_file_contents ). This function will loop over the variable populated in ReadFileContents and append to another list called head_list the header information from the file. These are the lines from the top of the file to the lines that start with the word ATOM.
4. Function called BuildAtomList(all_file_contents ). This function will loop over the variable populated in ReadFileContents and append to another list called atom_list all the lines that begin with ATOM and ONLY these lines.
5. Function called BuildTailList(all_file_contents ). This function will loop over the variable populated in ReadFileContents and append to another list called tail_list all the lines that are below those that begin with ATOM (the lines left over).
6. Function called WriteNewFile( ). This function will take the three lists created above (head_list, atom_list, tail_list) as arguments and will write these lists to an output file called output.txt that should look exactly like 1JKB.pdb when finished writing.
##### Part 2:
Write another program that will import the module you created above so that it can be used by this new program. Name this new program homework_5_solution_program.py. This program must have the following functions.
1. A function called Run( ) that will call AskForFileName( ) in the module you imported. Run( ) will then call the rest of the functions defined above in the same order they are defined above. Run( ) will finally call DifferenceTwoFiles( file_1, file_2).
2. Function called DifferenceTwoFiles( file_1, file_2) that will take in the name of two files as parameters. The order passed does not matter. Make sure the files are saved in the same directory as this python program. This function will open both files reading in all lines into two separate variables and compare the two to determine if the files are different. This function will accomplish this by looping over the elements of the first variable and checking if the second variable contains the same line in the same order. If there is a difference, then the element that is different should be appended to a list call diff_list. This list should then be counted for the number of differences and that number output.
