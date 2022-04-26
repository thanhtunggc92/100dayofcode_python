
from hangman import stages,logo
from hangman_wordlists import word_list
import random


print(logo)

pick_a_work= random.choice(word_list)
guess=['_'for x in range(len(pick_a_work))] # replace the character of choosing word with '_'
print(pick_a_work)
print(guess)
end_game=False # condition
turn=6 #total turn of guessing
while not end_game:
    user_guess= input("Guess your word").lower()
    for i in range (len(pick_a_work)):
        letter= pick_a_work[i] # set leeter = index of the character in the choosing word.
        if user_guess== letter:
            guess[i]=letter
    print(" ".join(guess))
    if "_"not in guess:
        end_game =True 
        print("You Win!")
    if user_guess not in pick_a_work:
        turn -=1

        print(stages[turn])
        print(f"You have {turn} lives left.")
    if turn ==0:
            end_game =True 
            print("Game over")
   
       

