from art import logo
import os
print(logo)


play_game=False


new_dict={}
game_on=False
player_list=[]
price_bid_list=[]
def aution_bid(bid_record):
    highest_score=0
    winner=""

    for bidder in bid_record:
        bid_amont = bid_record[bidder]
        if bid_amont > highest_score:
            highest_score = bid_amont
            winner=bidder
    print (f"the Winner is {winner} with the amount ${highest_score}")
while not game_on:
    player= input("Who are you?")

    price_bid=int(input("What's your bid?: $"))
    player_list.append(player)
    price_bid_list.append(price_bid)
    #new_dict[player]=price_bid
    
    who_else=input("Are there other users want to bid? yes or no\n")
    if who_else =="yes":
        os.system('CLS')
    elif who_else == "no":
        game_on=True
    else:
        print("Please type yes or no")
        print("The program is still running!")
    
new_dict={key:value for key,value in zip(player_list,price_bid_list)}

aution_bid(new_dict)
    

