#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculation")

bill=float(input("Please enter the total bill:$"))
tip=int(input("Please enter your tip: 10,12 or 15 %"))
people= int(input("How many people to split the bill?"))

tip_calculation= float((tip * bill)/100)

total_amount= float((bill + tip_calculation)/people)

print(f"Each person should pay:$ {round(total_amount,2)}")
