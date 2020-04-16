# Author: Srikanth Medicherla
# Date: 4/14/2020
# Description: Asks the user for an integer that the player or someone else will try to guess.
#              Counts how many tries it takes to guess the target number and also helpful comments
#              to guide the guesser: lets the guesser know if their guess is too high or too low each try.

total_attempts = 0
print(("Enter the number for the player to guess."))
num1 = int(input())
num2 = 0
while num1 != num2:
    print(("Enter your guess."))
    num2 = int(input())
    if num2 > num1:
        print("Too high - try again: ")
        total_attempts += 1
    elif num2 < num1:
        print("Too low - try again: ")
        total_attempts += 1
    else:
        total_attempts += 1
        break
if total_attempts == 1:                     # Different response needed to be created in case user guessed number in 1 try
    print("You guessed it in 1 try.")
else:
    print("You guessed it in " + str(total_attempts) + " tries.")
