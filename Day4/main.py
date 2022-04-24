import random

 

print("Welcom to Rock Paper and Scissors game")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game=[rock,paper,scissors]



stop_game= False   
computer_win=0
user_win=0
drawing =0
while not stop_game:
    comp_choice=random.randint(0,2)
    user_choice= int(input("Please pick one of the number to play the game: 0 for rock, 1 for paper and 2 for scissors and any different keys for quit"))
    
   
    if user_choice==0 and comp_choice==1:
        print(game[comp_choice])
        print(game[user_choice])
        print("Computer win. Want to try again?")
        computer_win +=1

    elif user_choice == 0 and comp_choice == 2:
        print(game[comp_choice])
        print(game[user_choice])
        print("User win. One more time?")
        user_win +=1
    elif user_choice == 0 and comp_choice == 0:
        print(game[comp_choice])
        print(game[user_choice])
        print(" Drawing. try again?")
        drawing +=1
    elif user_choice ==1 and comp_choice == 2:
        print(game[comp_choice])
        print(game[user_choice])
        print("Computer win. Want to try again?")
        computer_win +=1
    elif user_choice==1 and comp_choice == 0:
        print(game[comp_choice])
        print(game[user_choice])
        print("User win. One more time?")
        user_win +=1
    elif user_choice==1 and comp_choice == 1:
        print(game[comp_choice])
        print(game[user_choice])
        print(" Drawing. try again?")
        drawing +=1
    elif user_choice ==2 and comp_choice ==0:
        print(game[comp_choice])
        print(game[user_choice])
        print("Computer win. Want to try again?")
        computer_win +=1
    elif user_choice ==2 and comp_choice == 1:
        print(game[comp_choice])
        print(game[user_choice])
        print("User win. One more time?")
        user_win +=1
    elif user_choice == 2 and comp_choice == 2:
        print(game[comp_choice])
        print(game[user_choice])
        print(" Drawing. try again?")
        drawing +=1
    else:
        break

print(f"Computer win: {computer_win} times")
print(f"User win: {user_win} times")
print (f"drawing: {drawing}times")