helpers = 1
#the above declared variable is a global variable mtlb ki isko poore code mein kahi bhi use kar sakte ho.
def game():
    def increase_enemies():
        enemies = 2 # local variable hai ye isme ye variable sirf ye function hi access kar sakta hai bas..
        print(f"enemies inside function: {enemies}")
        print(f"helpers outside function: {helpers}")

    increase_enemies()

game()