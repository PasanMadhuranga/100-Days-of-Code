import os
import time

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    os.system("cls")
    print("My Coffee Machine")
    drink_want = input(f"What would you like? ({menu.get_items()})\n").lower()
    if drink_want == "report":
        print(coffee_maker.report())
        print(money_machine.report())
        time.sleep(5)
    elif drink_want == "off":
        print("Coffee Machine turned off...")
        time.sleep(3)
        break
    else:
        drink = menu.find_drink(drink_want)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                while True:
                    change = money_machine.make_payment(drink.cost)
                    if change:
                        print(f"Here is your {drink.name}!")
                        print(change)
                        coffee_maker.make_coffee(drink)
                        time.sleep(3)
                        break
                    else:
                        print("Insufficient money.")
                        time.sleep(1)
            else:
                print("Sorry! Resources are not sufficient.")
                time.sleep(1)
        else:
            print("That Coffee is not available")
            time.sleep(1)
