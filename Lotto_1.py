import random
drawn_numbers = []
your_numbers = []
result = []
for rounds in range(6):
    random_number = random.randint(1,10)
    while random_number not in drawn_numbers:
        drawn_numbers.append(random_number)
    drawn_numbers.sort()
for rounds in range(6):
    guess_number = int(input("put an number between 1 and 49 in: "))
    while guess_number not in your_numbers:
        your_numbers.append(guess_number)
    your_numbers.sort()
print(f"your numbers are:{your_numbers}\nthe drawn numbers are: {drawn_numbers}")
for number in drawn_numbers:
    if number in your_numbers:
        result.append(number)
    if len(result) > 2:
        print(f"hit, {number}")
    else:
        print("nothing won")
        print(f"the reslut is {result} ")

