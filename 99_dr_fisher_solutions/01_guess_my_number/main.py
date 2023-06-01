
# David Fisher
# This computer belongs to David Fisher

import random

# This is a comment.  The line below is code.
print("Welcome to Guess My Number")

# Pick a secret number
secret_number = random.randint(1, 100)
# print(secret_number)

# Create a variable, called guess_counter set to 0
guess_counter = 0

# Start a loop
while True:
    #   Ask the user to guess a number (1-100)
    guess = int(input("Guess a number: "))

    #   increment guess_counter by 1
    guess_counter = guess_counter + 1

    #   if the guess was too high, say "Too high"
    if guess > secret_number:
        print("Too High!")
    #   if the guess was too low, say "Too low"
    if guess < secret_number:
        print("Too Low!")
    #   if the guess was correct, exit the loop
    if guess == secret_number:
        break


# Tell the user, "Correct" and guess_counter (how many tries they took)
print(f"You are correct!  You took {guess_counter} guesses!")

