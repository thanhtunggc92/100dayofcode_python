from cmath import log
from art import logo , vs
from data import game_data
import random
import os

Data=game_data

def random_pick(dict):
    for _ in range(1):
        R= random.choice(dict)
    return R
    
A= random_pick(Data)
B=random_pick(Data)
game_is_on=False
print(logo)
n=0
while not game_is_on:
    while A==B:
        B=random_pick(Data)
    
    if n >0:
        print(f"You're right! current scrore: {n}")
    print(f"Compare A: {A['name']},a {A['description']}, from {A['country']} ")
    print(vs)
    print(f"Against B: {B['name']},a {B['description']},from {B['country']} ")
    user_chose= input("Who has more followers? Type 'A' or 'B'")
    os.system('CLS') # clear the screen
    
    if user_chose=='A'and A['follower_count'] > B['follower_count']:
        
        A = B
        n +=1
    elif user_chose =='A' and A['follower_count'] < B['follower_count']:
     
        game_is_on= True
        print(f"Sorry! WRONG. your final score: {n}")
    elif user_chose=='B'and A['follower_count'] > B['follower_count']:
        
        game_is_on=True
        print(f"Sorry! WRONG. your final score: {n}")
    elif user_chose=='B'and A['follower_count'] < B['follower_count']:
      
        A =B
        n +=1
    