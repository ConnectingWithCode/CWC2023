import random

#  print("Hello David Fisher!")

# for k in range(10):
#     print(k, "Hello")

print("Guess My Number")

# Select a random number 1 to 100
secret_number = random.randint(1, 1000)
# print(f"The secret number is... {secret_number}")

# Made a guess counter set to 0
guess_counter = 0

# Forever Loop:
#   Ask my user to guess a number
#   Incremented a guess counter
#   If the guess was Too High, I said "Too High"
#   If the guess was Too Low, I said "Too Low"
#   If the guess was correct, exit the loop

while True:
    guess = int(input("Guess a number: "))
    guess_counter = guess_counter + 1
    if guess > secret_number:
        print("Too High")
    if guess < secret_number:
        print("Too Low")
    if guess == secret_number:
        print("Correct!")
        break

# Tell my user "Good job you took XXXX guesses"
print(f"Good job you took {guess_counter} guesses")
