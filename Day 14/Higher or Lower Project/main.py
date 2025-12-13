import random
import game_data
import art
print(art.logo)
def get_data(compare):
    account_name=compare["name"]
    account_description=compare["description"]
    account_country=compare["country"]
    return f"{account_name} a {account_description} from {account_country}"

def followers(user_guess,a_follower,b_follower):

    if a_follower > b_follower:
        return user_guess=="a"
    else:
        return user_guess=="b"

score=0
should_continue=True
compare_b=random.choice(game_data.data)
while should_continue:

    compare_a= compare_b
    compare_b=random.choice(game_data.data)
    if compare_a==compare_b:
        compare_b=random.choice(game_data.data)


    print(f"Column A:- {get_data(compare_a)}")
    print(art.vs)
    print(f"Column B:- {get_data(compare_b)}")
    followers_input = input("Guess who has more followers on Instagram.. A or B? ").lower()
    print("\n "*20)

    a_follower_count=compare_a["follower_count"]
    b_follower_count=compare_b["follower_count"]

    is_correct=followers(followers_input,a_follower_count,b_follower_count)

    if is_correct:
        score +=1
        print(f"Yayy!! you scored a point.. Now your score is {score}")
    else:
        print(f"Oopsies.. You got it wrong. Your final score is {score}")
        should_continue=False

