from ascii_art import calculator_logo
import os


def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    print(calculator_logo)
    print("Welcome to my simple calculator app!")
    n1 = float(input("Enter the first number: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    n2 = float(input("Enter the second number: "))

    while True:
        calculation_function = operations[operation]
        answer = calculation_function(n1, n2)
        repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n")

        valid_input = repeat.lower() == 'y' or repeat.lower() == 'n'
        if valid_input:
            os.system('clear')
            if repeat.lower() == "n":
                print(f"{n1} {operation} {n2} = {answer}")
                break
            elif repeat.lower() == 'y':
                print(calculator_logo)
                n1 = answer
                operation = input("Pick an operation: ")
                n2 = float(input("Enter the second number: "))
                continue
        else:
            while not valid_input:
                os.system('clear')
                print("Invalid input, try again")
                repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n")
                valid_input = repeat.lower() == 'y' or repeat.lower() == 'n'


def add(n1: float, n2: float):
    """
    returns the sum of 2 numbers
    :param n1: first number
    :param n2: second number
    :return: sum of n1 and n2
    """

    return n1 + n2


def subtract(n1: float, n2: float):
    """
    subtracts n2 from n1 and returns the answer
    :param n1: first number
    :param n2: second number
    :return: n1 - n2
    """

    return n1 - n2


def multiply(n1: float, n2: float):
    """
    returns the product of 2 numbers
    :param n1: first number
    :param n2: second number
    :return: product of n1 and n2
    """

    return n1 * n2


def divide(n1: float, n2: float):
    """
    divides n1 with n2 and returns the answer
    :param n1: first number
    :param n2: second number
    :return: n1/n2
    """

    return n1/n2


calculator()
