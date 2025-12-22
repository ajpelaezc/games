import random

random_number = random.randint(1, 100)
attemps = 0
while True:
    try:
        number_guess_by_user = int(input("Enter a number (1-100): "))
        if 1 <= number_guess_by_user <= 100:
            print(f"Valid input: {number_guess_by_user}")
        else:
            print("Number must be between 1 and 100!")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    attemps += 1
    if number_guess_by_user < random_number:
        print("Too low! Try again...")
    else :
        print("Too high! Try again...")

    if number_guess_by_user == random_number:
        print(f"Correct! You guesed in {attemps} attemps!")   
        break 
