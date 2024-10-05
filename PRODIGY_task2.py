import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the Guessing Game!")
print("I have generated a random number between 1 and 100.")
print("Can you guess what it is?")

# Loop until the user guesses correctly
while True:
    try:
        # Prompt the user to enter their guess
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increment the number of attempts

        # Compare the guess to the generated number
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter an integer value.")