# Guess the number game
import random
print ("Welcome to the Guess the Number Game!, What is your name?")
name = input()
print("Well, " + name + ", I am thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)
number_of_guesses = 0
for range in range(1, 11):
    print("Take a guess.")
    guess = input()
    guess = int(guess)
    number_of_guesses += 1
    if guess < number_to_guess:
        print("Your guess is too low.")
    elif guess > number_to_guess:
        print("Your guess is too high.")
    else:
        break
print("Good job, " + name + "! You guessed my number in " + str(number_of_guesses) + " guesses!")
print("The number I was thinking of was " + str(number_to_guess) + ".")
