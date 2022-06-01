MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("Welcome to Coffee Machine")
def check_resuorce(Menu):
    """Check resource enough or not """
    for order in Menu:
        if resources[order] <= Menu[order]:
            print(f"Sorry there is not enough {order}")
            return False
    return True

def process_coin():
    """Return toal coin the buyer insert"""
    print("Please insert coin:")
    total=int(input("How many Quaters"))*0.25
    total +=int(input("How many dimes"))*0.1
    total +=int(input("How many nickles"))*0.05
    total +=int(input("How many pennies"))*0.01
    return total

def transaction_success(drink_cost,money_receive):
    """Return True if buyer pay enough money else return false"""
    global profit
    if money_receive < drink_cost:
        print("Sorry that is not enough money. Money refunded")
        return False
    else:
        changed=round(money_receive - drink_cost,2)
        print(f"here is your {changed}$ in changed")
        profit +=  drink_cost
        return True
def make_coffee(drink_name,drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your order {drink_name}☕🤟🤟🤟 enjoy!")
profit=0  
on_machine=False
while not on_machine:
    coffee_type=input("What would you like? 'espresso/latte/cappuccino' or off to quit\n")
    if coffee_type =='off':
        quit()
    elif coffee_type == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: $2.5")
    else:
        drink=MENU[coffee_type]
        if check_resuorce(drink['ingredients']):
            payment=process_coin()
            if transaction_success(drink['cost'],payment):
                make_coffee(coffee_type,drink['ingredients'])
            


