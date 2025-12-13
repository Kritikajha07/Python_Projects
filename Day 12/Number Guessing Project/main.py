import random
import art

EASY_LIFE=10
HARD_LIFE=5

def guesses(user_guess,user_choice,turns):

    if user_guess< user_choice:
        print("Too low")
        return turns -1
    elif  user_guess>user_choice:
        print("Too high")
        return turns -1

    else:
        print(f"Congratulations! You guessed the number right ")


def set_difficulty():
    difficulty = input("Choose a Difficulty: 'Easy' or 'Hard': ")

    if difficulty == "easy":
        return EASY_LIFE
    else:
         return HARD_LIFE

def game():
    print(art.logo)
    print("Welcome to the number guessing Game.")
    print("I'm thinking of a number between 1 and 100 ")
    choice = random.randint(1, 100)

    turns=set_difficulty()
    guess=0
    while guess != choice:
        print(f"You have {turns} attempt left to guess the number ")
        guess=int(input("Make a guess:- "))
        turns=guesses(guess,choice,turns)
        if turns==0:
            print("You don't have more attempts to guess the number. You lose! ")
            return
        elif guess!=choice:
            print("Guess Again!")

game()



