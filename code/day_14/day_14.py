from day_14_data import MENU, resources

def coffee_machine() -> None:
    """
    Coffee machine simulator.
    :return: None
    """

    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino):\n")
        while user_input.lower() not in ["espresso", "latte", "cappuccino", "off", "report"]:
            user_input = input("INVALID INPUT\nPLease try again (espresso/latte/cappuccino/off):\n")

        if user_input.lower() == "off":
            print("exiting...")
            break
        elif user_input.lower() == "report":
            print_report(resources)
        else:
            coffee = MENU[user_input.lower()]
            if is_resources_sufficient(resources, coffee["ingredients"]):
                amount_entered = process_coins()
                if is_amount_sufficient(amount_entered, coffee["cost"], resources):
                    make_coffee(user_input.lower(), resources, coffee["ingredients"])


def is_resources_sufficient(current_resources, resources_needed) -> bool:
    """
    Returns True if the coffee machine has sufficient resources to make required coffee, False otherwise
    :param current_resources: current resources available in coffee machine
    :param resources_needed: resources required by coffee choice
    :return: True if the coffee machine has sufficient resources to make required coffee, False otherwise
    """

    ret_val = True
    for resource in resources_needed:
        if not(current_resources[resource] >= resources_needed[resource]):
            ret_val = False
            print(f"Sorry, there is not enough {resource}")
    return ret_val


def process_coins() -> float:
    """
    Asks user to enter coins and accumulates the result
    :return: amount inserted by user
    """

    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    amount_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return amount_inserted


def is_amount_sufficient(amount_entered, coffee_cost, current_resources) -> bool:
    """
    Returns True if amount entered by user is sufficient to make coffee of choice, False otherwise.
    :param amount_entered: amount entered by user. Can be obtained by process_coins()
    :param coffee_cost: cost of coffee of choice
    :param current_resources: current resources available in the coffee machine
    :return: True if amount entered by user is sufficient to make coffee of choice, False otherwise.
    """

    if amount_entered == coffee_cost:
        current_resources["money"] += coffee_cost
        return True
    elif amount_entered > coffee_cost:
        extra_amount = round(amount_entered - coffee_cost, 2)
        print(f"Here is ${extra_amount} in change")
        current_resources["money"] += coffee_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_choice, current_resources, resources_used) -> None:
    """
    Prepares coffee and updates resources in coffee machine
    :param drink_choice: type of coffee selected by user
    :param current_resources: resources available in coffee machine
    :param resources_used: resources used in the making of coffee of choice
    :return: None
    """

    for resource in resources_used:
        current_resources[resource] -= resources_used[resource]
    print(f"Here is your {drink_choice}. Enjoy!")


def print_report(current_resources) -> None:
    """
    Reports the amount of resources available in coffee machine in user readable format.
    :param current_resources: resources available in coffee machine
    :return: None
    """

    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${current_resources['money']}")


coffee_machine()