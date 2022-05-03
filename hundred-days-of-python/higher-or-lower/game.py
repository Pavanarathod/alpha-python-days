import random
import art
from data import data

def get_random_data():
    """
    return the random list item
    """
    account_one = random.choice(data)
    account_two = random.choice(data)
    if account_one == account_two:
        account_two = random.choice(data)
    generated_data = {
        "data_one": account_one,
        "data_two": account_two,
    }
    return generated_data

def format_data(account_details: dict):
    """Format the account data into printable format"""
    return f"{account_details['name']}, a {account_details['description']}, from {account_details['country']}"

def get_followers(account_details: dict):
    # * GET ALL THE FOLLOWERS FROM THE DICTIONARY 
    followers = account_details['follower_count']
    return followers

def check_answer(guess: str, a_followers, b_followers):
    # * Take user guess and followers count and returns if the got it right
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(art.logo)
    score = 0
    game_should_continue = True

    while game_should_continue:  
        print(f"Compare A: {format_data(get_random_data()['data_one'])}")
        print(art.vs)
        print(f"Against B: {format_data(get_random_data()['data_two'])}")
        user_ans = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
        a_followers_account = get_followers(get_random_data()['data_one'])
        b_followers_account = get_followers(get_random_data()['data_two'])
        is_user_correct = check_answer(user_ans, a_followers_account, b_followers_account)
        
        if is_user_correct:
            score += 1
            print(f"You'r right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry , that's wrong. Final Score {score}")

