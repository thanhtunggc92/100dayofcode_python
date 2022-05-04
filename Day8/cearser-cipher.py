
from cmath import log
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop_game=False

def ceapher(ceapher_text,shift,ceapher_direction):
    ceaphered=""
   
    if ceapher_direction == "decode":
            shift *=-1
    
    for letter in ceapher_text:
        #todo:3
        if letter not in alphabet:
           ceaphered += letter
        else:
            
            position= alphabet.index(letter)
            new_pos = position + shift  
            ceaphered +=alphabet[new_pos]
    print(f"The {ceapher_direction}d for your text is: {ceaphered}")
while not stop_game:
    print (logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
   
    if shift > 36:
        shift= shift %26
    else:
        shift=shift
    ceapher(text,shift,direction)
    user_input= input("Do you want to restart the program. Yes or No\n").lower()
    if user_input == 'yes':
        ceapher(ceapher_text=text,shift=shift,ceapher_direction=direction)
    else:
        stop_game=True
#Shorter answer. combine two encrypt and decrypt into one function.

    
# def encryupt(text,shift):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#     encrypted=""
    
#     for c in text:
#         position=alphabet.index(c)    

#         new_pos= position + shift
#         encrypted += (alphabet[new_pos])
#     print( encrypted)
            
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word ''?🐛
# def decrypt(text,shift):
#     decrypted=""
#     for letter in text:
#         position= alphabet.index(letter)
#         new_pos= position - shift
#         decrypted += alphabet[new_pos]
#     print(decrypted)
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# # if direction == 'encode':


# #     encryupt(text,shift)
# # else:
# #     decrypt(text,shift)

    
# ceapher(ceapher_text=text,shift=shift,ceapher_direction=direction)