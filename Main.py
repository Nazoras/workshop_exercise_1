import random
"""
a guess game:
try to figure out, which number we are looking for
"""
def ratespiel():
    counter = 10
    original_counter = counter
    guess_number = random.randint(1,100)
    guess = int(input("enter a number between 1 and 20: "))
    positive = guess - guess_number
    negative = guess_number - guess
    while guess > 20 or guess < 1:
        print("the number is higher than 20 or negative.")
        guess = int(input("please enter a number between 1 and 20 again: "))
    while counter > 0:
        while guess != guess_number:
            if counter == 1:
                return print("  !!!!! GAME OVER !!!!!","\n",f"The seeked number was {guess_number}!" )
            elif guess < guess_number:
                negative = guess_number - guess
                print(f"The guess number is higher than your guess  about {negative}")
                counter = counter -1
                print(f"you have left {counter} out of {original_counter} tries")
                guess = int(input("please enter a number between 1 and 20 again: "))
                while guess > 20 or guess < 1:
                    print("the number is higher than 20 or negative.")
                    guess = int(input("please enter a number between 1 and 20 again: "))
            elif guess > guess_number:
                positive = guess - guess_number
                print(f"The guess number is lower than your guess about {positive}")
                counter = counter - 1
                print(f"you have left {counter} out of {original_counter} tries")
                guess = int(input("please enter a number between 1 and 20 again: "))
                while guess > 20 or guess < 1:
                    print("the number is higher than 20 or negative.")
                    guess = int(input("please enter a number between 1 and 20 again: "))
        if guess_number == guess:
            return print(f"Congratulation, won the game in {counter} rounds.Your guess was {guess} and the guess number was {guess_number}")
ratespiel()
