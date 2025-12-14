MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money=0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print("Sorry!! we dont have enough ingredients to fulfill your order..")
            return False
    return True

def coins():
    print("Please insert the coins. ")
    total=int(input("How many Quarters? ")) * 0.25
    total+=int(input("How many Dimes? ")) * 0.1
    total+=int(input("How many Nickles? ")) * 0.05
    total+=int(input("How many Pennies? ")) * 0.01
    return total

def transaction(money_received,drink_cost):
    if money_received >= drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is your change: ${change}")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry!! That's not enough money. Your money is refunded")
        return False

def is_transaction_successful(order_ingredients,drink_name):
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"here is your {drink_name}. Enjoy your coffee!! ")



should_continue=True

while should_continue:
    coffee_input = input("What kind of coffee would you like? (latte/espresso/cappuccino) ").lower()


    if coffee_input=="off":
        should_continue=False
    elif coffee_input == "report":
        print(f"Water: {resources["water"]} ml ")
        print(f"Milk: {resources["milk"]} ml ")
        print(f"Coffee: {resources["coffee"]} g ")
        print(f"Money: ${money}")
    else:
        drink = MENU[coffee_input]
        if is_sufficient(drink["ingredients"]):
            payment=coins()

            if transaction(payment,drink["cost"]):
                is_transaction_successful(drink["ingredients"], coffee_input)

# till it comes should continue=False