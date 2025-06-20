import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = None
attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.\n")

# Game loop
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
    except ValueError:
        print("❌ Please enter a valid number.\n")
