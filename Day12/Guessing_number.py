from art import logo
import random

number= random.randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of the number between 1 and 100.")

def level():
    choose_level=input("Choose a difficult: 'easy' or 'hard'")
    if choose_level =='easy':
        n=10
    else:
        n= 5
    return n
n= level()

print(number)
print(f"You have {n} attemps to guess a number.")
while n > 0: 
    user_guess=int(input('Pick your number: '))

    if user_guess == number:
        print("Correct! You win!")
        n = 0
    elif user_guess>number:
        print("too high. Again")
        n -=1
        print(f"You have {n} attempts to guess a number")
    elif user_guess < number:
        print("too low. one more time")
        n -= 1
        print(f"You have {n} attempts to guess a number")
