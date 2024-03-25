import os
from ascii_art import gavel


def blind_auction():
    bid_dictionary = {}
    print(gavel)
    print("Welcome to the secret auction program.")

    while True:
        name = input("What is your name?: \n")
        bid = int(input("What's your bid?: \n$"))
        bid_dictionary[name] = bid

        repeat = input("Are there any other bidders? Type 'yes' or 'no': \n")
        os.system('clear')

        valid_input = repeat.lower() == 'yes' or repeat.lower() == 'no'
        if valid_input:
            if repeat.lower() == "no":
                find_highest_bidder(bid_dictionary)
                break
            elif repeat.lower() == 'yes':
                continue

        else:
            while not valid_input:
                print("Invalid input, try again")
                repeat = input("Are there any other bidders? Type 'yes' or 'no': \n")
                valid_input = repeat.lower() == 'yes' or repeat.lower() == 'no'
                os.system('clear')

def find_highest_bidder(bid_dictionary):
    winner = ("", 0)
    for key in bid_dictionary:
        value = bid_dictionary[key]
        if value > winner[1]:
            winner = (key, value)

    print(f"The winner is {winner[0]} with a bid of ${winner[1]}.")


blind_auction()