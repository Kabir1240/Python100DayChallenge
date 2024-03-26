from ascii_art import higher_lower_logo as logo, vs
from day_13_gamedata import data
import random
import os


def higher_lower():
    """
    Higher Lower game that allows user to guess who has more followers between two instagram personalities
    :return: None
    """

    data_len = len(data)
    score = 0

    while True:
        # select random personalities
        personalities = select_random_personalities(data_length=data_len)

        # display game
        higher_lower_display(personality_a=personalities[0], personality_b=personalities[1])

        # ask user to guess between A or B having higher follower count
        follower_count_a = personalities[0]["follower_count"]
        follower_count_b = personalities[1]["follower_count"]

        # below function returns True if user is correct and False if not
        user_is_correct = ask_comparison(follower_count_a, follower_count_b)

        # compare and check if user is right. If they are, add to their score
        if user_is_correct:
            score += 1
            print(f"You're correct, your score is: {score}")
            os.system('clear')
            input("press 'Enter' to continue")

        # end game if user guesses wrong
        elif not user_is_correct:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

    return


def higher_lower_display(personality_a, personality_b):
    """
    prints out the logo and the two random personalities for the higher lower game module
    :param personality_a: first personality
    :param personality_b: second personality
    :return: None
    """

    print(logo)
    print(f"Compare A: {format_data(personality_a)}")
    print(vs)
    print(f"Against B: {format_data(personality_b)}")

    return


def select_random_personalities(data_length:int):
    """
    selects two random personalities from data dictionary
    :param data_length: length of list, data
    :return: a list of length 2, with 2 dictionaries, each containing one instagram personality
    """

    personality_a_index = random.randint(0, data_length - 1)
    personality_b_index = random.randint(0, data_length - 1)
    # make sure we don't get the same celebrity twice
    while personality_a_index == personality_b_index:
        personality_b_index = random.randint(0, data_length - 1)

    personality_a = data[personality_a_index]
    personality_b = data[personality_b_index]
    return [personality_a, personality_b]


def ask_comparison(follower_count_a: int, follower_count_b: int) -> bool:
    """
    Part of higher lower module. Asks user to guess who they think has more followers. Returns True if they are right
    and False if they are wrong
    :param follower_count_a: follower count of personality A
    :param follower_count_b: follower count of personality B
    :return: Returns True if they are right and False if they are wrong
    """
    guess = input("Who do you think has more followers? Type 'A' or 'B': ")
    while guess.lower() not in ['a', 'b']:
        guess = input("Enter either 'A' or 'B'")

    if follower_count_a > follower_count_b:
        return guess.lower() == 'a'
    else:
        return guess.lower() == 'b'


def format_data(personality):
    name = personality["name"]
    description = personality["description"]
    country = personality["country"]

    return f"{name}, a {description}, from {country}."

higher_lower()