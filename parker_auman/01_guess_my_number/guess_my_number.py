import random

import forever as forever

print("get number or else my cat will kill you embarassing")

# select a random 1 and 100
secret_number = random.randint(1, 100)
#print(f"the secret is... {secret_number}")

# Made a guess counter set too 0
guess_counter = 0

#forever loop:
#   ask my user to guess a number
#   incremented a guess counter
#   if the number was to high, I said "too high you stupid"
#   if the number was to low, I said "too low you're a big baby"
#   if the guess was correct,exit the loop

while True:
    guess = int(input("guess a number: "))
    guess_counter = guess_counter + 1
    if guess > secret_number:
        print("too high you stupid!")
    if guess < secret_number:
        print("too low your a big baby!")
    if guess == secret_number:
        print("finally you were wasting my battery power")
        break
#tell user "finally you were wasting my battery power"
print (f"good job you took {guess_counter} guesses")




































