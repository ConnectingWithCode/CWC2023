print("")

import random

secret_number = random.randint(0, 100)
#print(secret_number)

counter = 0

while True:
    guess = int(input("Guess a Number:  "))
    counter = counter + 1
    if guess > secret_number:
        print("Lower.")
    if guess < secret_number:
        print("Higher")
    if guess == secret_number:
        break

if counter == 1:
    print(f"You are correct. You took {counter} guess.")
else:
    print(f"You are correct. You took {counter} guesses.")