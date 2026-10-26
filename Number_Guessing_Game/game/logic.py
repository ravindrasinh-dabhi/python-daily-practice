import random
def generate_random_number(start, end):
    """ THIS RETURNS THE RANDOM NUMBER BETWEEN THE STRAT AND END WHERE START AND END ARE INCLUDED"""
    
    return random.randint(start, end)


def check_guess(guess, secret_number):
    """ THIS FUNCTION CHECKS THE GUESS AND RETURNS A STRING BASED ON THE GUESS"""
    
    if guess < secret_number:
        return "Your guess is too low."
    elif guess > secret_number:
        return "Your guess is too high."
    else:
        return "Congratulations! You've guessed the correct number!"