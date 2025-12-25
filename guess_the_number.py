import random

# Control variable for replaying the game
play_again = 1

# Outer loop: handles replaying the game
while play_again == 1:

    # Game setup
    random_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    # Inner loop: guessing phase
    while max_attempts > 0:
        try:
            # Get user input
            guess = int(
                input(f"Enter a number (1–100) — {max_attempts} attempts remaining: ")
            )

            # Validate range
            if not 1 <= guess <= 100:
                print("Number must be between 1 and 100!")
                continue

        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        # Valid guess consumes an attempt
        attempts += 1
        max_attempts -= 1

        # Compare guess with the target number
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts!")
            answer = input("Want to try again?: ")
            if answer != "yes":
                play_again = 0
            break

        # Check for loss condition
        if max_attempts == 0:
            print("You lost!")
            answer = input("Want to try again?: ")
            if answer != "yes":
                play_again = 0
