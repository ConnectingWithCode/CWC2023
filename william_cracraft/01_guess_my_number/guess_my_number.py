
import random

print("Welcome to guess my number")


secret_number = random.randint(0, 2000)
#print(secret_number)

counter = 0
while True:
    guess = int(input("guess a number"))
    counter = counter + 1
    if guess > secret_number:
        print("too high")
    if guess < secret_number:
        print("too low")
    if guess == secret_number:
        break
if counter == 1:
    print(f"You took {counter} guess")
elif counter > 1:
    print(f"You are correct! you took {counter} guesses")



#select a random number 1 to 100
#made a guess counter set to 0

#forever loop:
#ask my user to guess a number
#incremented a guess counter
#If the guess was too high I told him "too high"
#If the guess was too low I told him "too low"
# if the guess was correct, exit the loop

#tell my user "good job it took you xxxx guesses"