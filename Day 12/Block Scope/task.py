# import random
#
# game_level=random.randint(1,4)
# enemies=["Vecna","Voldemort","Hyde"]
#
# def create_enemy():
#     new_enemy=""
#     if game_level<5:
#         new_enemy=random.choice(enemies)
#
#     print(new_enemy)
#
# create_enemy()

def is_prime(num):
    if num % 2 !=0 and num!=0 and num!=1 and num %1==0:

        return "True"

    else:
        return "False"
is_prime(73)
