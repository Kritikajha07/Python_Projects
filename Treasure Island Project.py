print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
side=input("you've reached a cross road where do you want to go? Type 'left' or 'right' for choosing a direction \n")
if side=="left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake=input("type 'wait' to wait for a boat and type 'swim' to swim across the lake \n")
    if lake=="wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door=input("you've three doors in front of you one red,one yellow,one blue.Select a door colour\n ")
        if door=="red":
            print("Oops! this room is full of fire. Game Over!")
        elif door=="yellow":\
            print("Congratulations! You've found the treasure ")
        else:
            print("you enter a room of beasts! . Game Over! ")
    else:
        print("there are crocodiles in the lake they ate you . Game Over! ")
else:
    print("you've been attacked by the lions . Game Over!")
