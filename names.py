# number guessing code
# guess a number between 1-9
# you have 3 guess
from random import choice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random_number = choice(numbers)
guesses_left = 3


user_input = int(input("Try to guess: "))
if user_input not in numbers:
    print("Invalid Input. You must choose a number between 1 and 9")

if user_input == random_number:
    print("You are correct.")
else:
    print("You are wrong.")


print(random_number)
print(user_input)
