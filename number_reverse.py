import random

def my_number():
    " a helper function to enter the number"
    try:
        my_guess = int(input("put a number between 1 and 1000: "))
    except ValueError:
        print("It's not a number, last chance fancy pants:")
        my_guess = int(input("Guess the number: "))
    while my_guess > 1000 or my_guess < 1:
        print("the number is higher then 1000 or negativ")
        my_guess = int(input("put a number between 1 and 1000: "))
    return my_guess

def guess_the_number():
    counter = 10
    my_guessed_number = my_number()
    print(my_guessed_number)
    too_small = 'Too small'
    too_big = 'Too big'
    you_won = 'You won'
    for i in range(counter):
        print(f"your guess is {my_guessed_number}")
        pc_guessed_try = random.randint(1,1000)
        print(f"the computer guesses the number: {pc_guessed_try}\nis that guess correct?")
        answer = input("write 'Too small', 'Too big' or 'You win'")
        answer = str(answer)
        while answer != too_small or answer != too_big or answer != you_won:
            answer = input("try again! write 'Too small', 'Too big' or 'You win'")
        if answer == too_small:
            difference_small = my_guessed_number - pc_guessed_try
            print(f"ok, the computers guess is too small about {difference_small}")
        elif answer == too_big:
            difference_big = pc_guessed_try - my_guessed_number
            print(f"nah, the computers guess is too big about {difference_big}")
        elif answer == you_won:
            return print("nice, the computer figured out")
    return print("Game over, the player won!")

        
guess_the_number()




