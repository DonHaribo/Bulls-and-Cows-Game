"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
import random
#writing out the welcoming sequence
sep = '-' * 25
print('hi there')
print(sep)
print(
    "I've have generated a random"
    " 4 digit number for you."
    "\nLet's play a bulls and cows game."
)
print(sep)

# bening the while loop
# defining user input
bulls_count = []
cows_count = []
RNG_numbers = []
number_of_guesses = []
RNG = random.randint(1, 9)
# generating the first non 0 digit
if RNG not in RNG_numbers:
    RNG_numbers.append(RNG)
# generating the last three digits so that there are
# no duplicates
while len(RNG_numbers) != 4:
    RNG = random.randint(0, 9)
    if RNG not in RNG_numbers:
        RNG_numbers.append(RNG)
print(RNG_numbers)

# user inputs his first guess

# Establishing the correctness of the given input
# notifing the user of the errors
user_numbers = []

def error_message():
    print(
        'You need to input 4 numeric characters.'
        ' please try again'
    )
while len(bulls_count) < 4:
    if len(number_of_guesses) == 0:
        guess = input('Enter a number:')
    else:
        guess = input('>>>>>> ')
    print(guess)
    print(sep)

    if not guess.isnumeric():
        error_message()
    elif len(guess) != 4:
        error_message()
    elif guess[0] == '0':
        error_message()
    else:
        pass

    # creating a list with the correct input
    for number in guess:

        if number not in user_numbers:
            user_numbers.append(int(number))

        else:
            error_message()
            user_numbers.clear()
    # checking for the cows and bulls



    # bulls count
    for number, digit in zip(user_numbers, RNG_numbers):
        if number == digit:
            bulls_count.append(1)

    for number in user_numbers:
        if number in RNG_numbers:
            cows_count.append(1)
    teh_real_cows = sum(cows_count)-sum(bulls_count)
    print(f'{len(bulls_count)} bulls, {teh_real_cows} cows')
    # cows count

    number_of_guesses.append(1)
    user_numbers.clear()
print(sep)
print(
    "Correct, you've guessed the right"
    f" number in  {len(number_of_guesses)} guesses!"

)
print(sep)
if len(number_of_guesses)  < 3:
    print('!!amazing job!!')
elif len(number_of_guesses) < 4 and len(number_of_guesses)  > 8:
    print('You okay man!')
else:
    print('you suck!')



