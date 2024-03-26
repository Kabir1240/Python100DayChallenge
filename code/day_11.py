from ascii_art import blackjack_logo
from day_11_cards import cards, suits, card_scores, players_cards, cpu_cards
import random


def blackjack():
    print(blackjack_logo)
    print("Welcome to Blackjack! (double, split and insure pending)")

    possible_amounts = [1000, 1500, 2500]
    total_amount = int(input("How much pot would you like to start with, 1000, 1500 or 2500?: $"))
    while total_amount not in possible_amounts:
        total_amount = int(input("Choose one of these amounts; 1000, 1500 or 2500: $"))

    # start game loop
    while total_amount > 0:
        # set betting amount
        #TODO Add chip denominations instead of random amounts of money
        bet = int(input(f"How much money would you like to bet? You have ${total_amount}: $"))
        while bet > total_amount:
            print("That's more than you can afford, pick a suitable amount")
            bet = int(input(f"How much money would you like to bet? You have ${total_amount}: $"))

        print("\nDealing Cards\n")

        for i in range(2):
            # pick random player card
            pick_random_card(players_cards)
            # pick random cpu card
            pick_random_card(cpu_cards)

        # display both user cards and first cpu card + the scores
        print("Your Hand: ")
        display_score(players_cards)
        display_second_card_only(cpu_cards)

        # implement blackjack mechanic
        if players_cards["score"] == 21:
            print("\nDealer's Hand: ")
            display_score(cpu_cards)
            print()

            if cpu_cards["score"] != 21:
                print("BLACKJACK! You Win!")
                total_amount += 1.5*bet
            elif cpu_cards["score"] == 21:
                print("DRAW!")
            reset_cards(players_cards, cpu_cards)
            print(f"remaining pot: ${total_amount}")

        # if dealer gets blackjack
        elif cpu_cards["score"] == 21:
            print("\nDealer's Hand: ")
            display_score(cpu_cards)
            print("\nDealer Wins!")
            total_amount -= bet
            reset_cards(players_cards, cpu_cards)
            print(f"remaining pot: ${total_amount}")
        else:
            hit = ask_hit_or_stand()
            while players_cards["score"] < 21 and hit:
                pick_random_card(players_cards)
                if players_cards["score"] > 21:
                    if players_cards["aces"] > 0:
                        players_cards["aces"] -= 1
                        players_cards["score"] -= 10
                    else:
                        print("BUST! Dealer Wins")
                        total_amount -= bet
                        break

                print("\nYour Hand: ")
                display_score(players_cards)
                display_second_card_only(cpu_cards)

                hit = ask_hit_or_stand()
                if hit:
                    continue
                else:
                    break

            while cpu_cards["score"] < 17:
                pick_random_card(cpu_cards)

            # display final score
            print("Your Hand: ")
            display_score(players_cards)
            print("\nDealer's Hand: ")
            display_score(cpu_cards)

            player_score = players_cards["score"]
            cpu_score = cpu_cards["score"]
            print()
            if player_score <= 21:
                if cpu_score > 21:
                    print("You Win!")
                    total_amount += bet
                elif player_score > cpu_score:
                    print("You Win!")
                    total_amount += bet
                elif cpu_score > player_score:
                    print("Dealer Wins")
                    total_amount -= bet
                elif cpu_score == player_score:
                    print("Draw!")

            print(f"remaining pot: ${total_amount}")
            reset_cards(players_cards, cpu_cards)


def ask_hit_or_stand() -> bool:
    hit_inputs = ['hit', 'h', 'stand', 's']
    # ask to hit or stand
    hit = input("type 'hit' or 'h' to hit and 'stand' or 's' to stand")
    print()
    if hit.lower() in hit_inputs:
        if hit.lower() == 'hit' or hit.lower() == 'h':
            hit = True
        elif hit.lower() == 'stand' or hit.lower() == 's':
            hit = False
    else:
        while hit not in hit_inputs:
            print("Not a valid input, try again")
            hit = input("type 'hit' or 'h' to hit and 'stand' or 's' to stand")

    return hit


def display_score(card_dictionary):
    for i in card_dictionary["cards"]:
        print(i)
    player_current_score = card_dictionary["score"]
    print(f"Total score is {player_current_score}")


def pick_random_card(card_dictionary):
    # choose the suit
    random_suit_idx = random.randrange(0, len(suits))
    random_suit = suits[random_suit_idx]

    # choose the card
    random_card_idx = random.randint(0, len(cards[random_suit]) - 1)
    random_card = cards[random_suit].pop(random_card_idx)
    if random_card.lower() == 'ace':
        card_dictionary["aces"] += 1

    # update score and store card
    card_dictionary["score"] += card_scores[random_card]
    card_dictionary["cards"].append(f"{random_card} of {random_suit}")


def display_second_card_only(card_dictionary):
    print("\nDealer's Hand: ")
    second_card = card_dictionary["cards"][1].split()[0]
    score = card_scores[second_card]
    print(card_dictionary["cards"][1])
    print(f"Total score is {score}")


def reset_cards(players_deck, cpu_deck):
    players_deck["score"] = 0
    players_deck["cards"] = []
    players_deck["aces"] = 0

    cpu_deck["score"] = 0
    cpu_deck["cards"] = []
    cpu_deck["aces"] = 0



blackjack()