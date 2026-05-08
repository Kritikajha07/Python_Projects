rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose=int(input("what do you choose? type 0 for Rock,1 for Paper or 2 for Scissors \n"))
if choose==0:
    print(rock)
elif choose==1:
    print(paper)
else:
    print(scissors)
import random
choice=random.randint(0,2)
print(f"Computer chose {choice} \n")
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
else:
    print(scissors)

if choose==0 and choice==2:
    print("You Win!")
elif choice > choose:
    print("You Lose!")
elif choice < choose:
    print("You Win!")
elif choose==choice:
    print("It's a tie!")
else:
    print("enter a valid number")

