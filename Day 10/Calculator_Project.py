

import art


def add(n1, n2):
    return n1 + n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def subtract(n1,n2):
    return n1 - n2

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
# print("+")
# print("-")
# print("*")
# print("/")
#
# result=operation[choice](n1=first,n2=second)
# print(result)
def calculator():
    print(art.logo)
    should_continue=True
    first = float(input("What is the first number? "))

    while should_continue:
        for symbol in operation:
            print(symbol)
        choice = input("Pick an operation: ")
        second = float(input("What is the second number? "))
        result = operation[choice](first,second)
        print(f"{first} {symbol} {second}={result}")

        should=input(f"do you want to continue with {result} type 'y' or 'n' ")

        if should=="y":
            first = result
        else:
            should_continue=False
            print("\n"*20)
            calculator()

calculator()
