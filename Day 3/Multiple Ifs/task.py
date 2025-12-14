print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
age=int(input("What is your age? "))
if height >= 120:
    print("You can ride the rollercoaster")
    if age<12:
        bill=5
        print("child tickets are $5")
    elif age <=18:
        bill=7
        print("teenagers tickets are  $7")
    else:
        bill=27
        print("adult tickets are  $27")

    want_photo=input("do you want to take a photo? if yes then type y and if no then type n")
    if want_photo=="y":
        bill+=3
        print(f"your total bill is {bill}")
    else:
        print(f"your total bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
