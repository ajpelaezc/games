import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Count how many attempts the user makes
attempts = 0

# Main game loop
while True:
    try:
        # Ask the user for a guess
        number_guess_by_user = int(input("Enter a number (1–100): "))

        # Check if the number is within the valid range
        if 1 <= number_guess_by_user <= 100:
            print(f"Valid input: {number_guess_by_user}")
        else:
            print("Number must be between 1 and 100!")
            continue  # Skip the rest and ask again

    except ValueError:
        # Runs if the input is not an integer
        print("Invalid input! Please enter a valid integer.")
        continue

    # Count this attempt
    attempts += 1

    # Compare the guess to the random number
    if number_guess_by_user < random_number:
        print("Too low! Try again...")
    elif number_guess_by_user > random_number:
        print("Too high! Try again...")
    else:
        # Correct guess
        print(f"Correct! You guessed it in {attempts} attempts!")
        break
