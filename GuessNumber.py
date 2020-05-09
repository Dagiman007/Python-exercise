'''
Title: Guess the number game
Adapted from: inventwithpython.com
'''
import random

guessesTaken = 0

myName = input("Hello! What's your name? ")

number = random.randint(1,20)

print("Well, "+ myName +", I'm thinking of a number between 1 and 20.")

while guessesTaken < 6:
    guess = int(input("Take a guess."))
    guessesTaken += 1

    if guess < number:
        print("your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job, " + myName + "! you guessed my number in " + guessesTaken + " guesses")
if guess != number:
    print("Nope. The number I was thinking was ",number)
          

      
