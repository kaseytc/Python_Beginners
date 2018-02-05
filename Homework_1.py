'''
HW1.py:

Write a program that asks the user for their dream job title. Then ask them for the hourly wage they want to earn.
This number should account for dollars and cents. Calculate the annual wage they will earn over a year.
Assume they work 48 weeks a year (4 weeks vacation) but are paid over 52 weeks.
Then ask them how much money they feel they will need at retirement time.
Determine the number of years they will have to work to save up their retirement dollar value
assuming their only source of income was their paycheck?
Finally, determine if the number of years they need to save is an even or odd number.
For this part, use the modulus operator to determine if the number you calculated is odd or even.
Once you have calculated it, use print to print out the value.
You should also print out something like this.
"If the value is --- then the number is odd, however, if the value is ----- then the number is even."
'''

# ask user's the dream job title
job_input = raw_input('What is your dream job? ')

# ask the hourly wage user want to earn
wage_input = raw_input('What is the hourly wage you want to earn? ')
try:
    wage = float(wage_input)
except ValueError:
    print 'The number input', wage_input, 'is not a valid number'
else:
    print 'The number input', wage_input, 'is a valid number'
    print 'Your desire hourly wage is:', wage

    # calculate annual wage. assume working 8 hours per day, 5 days per week, and get paid 52 weeks per year
    annual_wage = wage * 8 * 5 * 52
    print 'Your desire annual wage is:', annual_wage

    # ask user's desire retirement money
    retire_input = raw_input('How much money you feel you will need at retirement time? ')
    try:
        retire = float(retire_input)
    except ValueError:
        print 'The number input', retire_input, 'is not a valid number'
    else:
        print 'The number input', retire_input, 'is a valid number'
        print 'Your desire retirement money is:', retire

        # calculate the estimated number of years the user should work for their retirement life
        number_of_year = int(round(retire / annual_wage))
        print 'The estimated working year is:', number_of_year

        # determine if the number of working year is odd or even
        odd_or_even = number_of_year % 2
        print 'Working year value is odd or even number:', odd_or_even
        print 'If the value is 1 then the number is odd, however, if the value is 0 then the number is even.'




