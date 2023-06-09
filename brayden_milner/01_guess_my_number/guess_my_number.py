import random

print("Welcome to Guess My Number")

secret_number = random.randint(0, 100)
# print(secret_number)

counter = 0

while True:
    guess = int(input("Guess a number: "))
    counter = counter + 1
    if guess > secret_number:
        print("Too High!")
    if guess < secret_number:
        print("Too Low!")
    if guess == secret_number:
        break

if counter == 1:
    print(f"You are correct! You took {counter} guess!")
elif counter > 1:
    print(f"You are correct! You took {counter} guesses!")