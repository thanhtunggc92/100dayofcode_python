

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu= Menu()
coffee_maker=CoffeeMaker()
Money_machine=MoneyMachine()


print("Welcome to coffee machine in OOP")
is_machine_on=False

while not is_machine_on:


    option = menu.get_items()
    choice=input(f"what would you like: ({option})")
    if choice=='report':
            coffee_maker.report()
            Money_machine.report()
    elif choice =='off':
        is_machine_on = True
    else:
        find_a_drink= menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(find_a_drink):
            if Money_machine.make_payment(find_a_drink.cost):
                make_cooffee=coffee_maker.make_coffee(find_a_drink)