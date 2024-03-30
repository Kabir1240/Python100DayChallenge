from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def coffee_machine_oop():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while True:
        user_input = input(f"What would you like? ({menu.get_items()}):\n")
        while user_input.lower() not in ["espresso", "latte", "cappuccino", "off", "report"]:
            user_input = input("INVALID INPUT\nPLease try again (espresso/latte/cappuccino/off):\n")

        if user_input.lower() == "off":
            print("Exiting...")
            break
        elif user_input.lower() == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            coffee = menu.find_drink(user_input.lower())
            if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
                    coffee_maker.make_coffee(coffee)

coffee_machine_oop()