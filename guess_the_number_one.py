import random
"""
a guess game:
try to figure out, which number we are looking for.
"""

def my_number():
    " a helper function to enter the number"
    while True:
        try:
            my_guess = int(input("Guess the number: "))
            return my_guess
        except ValueError:
            print("It's not a number, last chance fancy pants, try again:")

def guess_the_number():
    "the maingame"
    guess_pc = random.randint(1, 100)
    given_number = my_number()
    while given_number > 100 or given_number < 0:
        print("the number is higher than 100 or negative.")
        given_number = my_number()
    while given_number is not guess_pc:
        if given_number < guess_pc:
            differenze_small = guess_pc - given_number
            print(f"Too small!, your number is {differenze_small} higher ")
            given_number = my_number()
        else:
            differenze_high = given_number - guess_pc
            print(f"Too big! your number is {differenze_high} smaller")
            given_number = my_number()
    return print("You Win!")

guess_the_number()