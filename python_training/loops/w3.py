#question 10: Simple Number Guessing Game
#Problem Statement:
#Write a Python program where the user needs
# to guess a predefined secret number.
#Store a secret number in a variable.
#Ask the user to guess the number.
#If the guess is greater than the secret number, 
#display "Too high".
#If the guess is smaller, display "Too low".
#If the guess is correct, 
#display "Congratulations! You guessed it".
#Continue asking until the user guesses correctly.
#Use a while loop.
#Sample Input:
#text
#Guess the number: 30
#Guess the number: 15
#Guess the number: 25
#Expected Output:
#text
#Too high!
#Too low!
#Congratulations! You guessed it.
#Solution:

secret_number = 25
guess = 0
while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed it.")
