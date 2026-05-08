
# small_price=15
# medium_price=20
# large_price=25
# small_pepperoni_price=2
# medium_pepperoni_price=3
# large_pepperoni_price=3
# cheese_price=1
# if size=="S":
#     small_price=15
#     print("total for a small pizza is $15")
#     if size=="M":
#         medium_price=20
#         print("total for a medium pizza is $20")
#     if size=="L":
#         large_price=25
#         print("total for a large pizza is $25")
#
#
# if pepperoni=="Y":
#     small_pepperoni_price=small_price + 2
#     print(f"the total for small pizza is {small_pepperoni_price} ")
# if pepperoni=="Y":
#     medium_pepperoni_price=medium_price + 3
#
#     print(f"the total for your pizza is {medium_pepperoni_price} ")
# elif pepperoni=="Y":
#     large_pepperoni_price=large_price + 3
#     print(f"the total for your pizza is {large_pepperoni_price} ")
# # if pepperoni=="N":
# #     print("your total bill without pepperoni is ")
#
# if extra_cheese=="Y":
#     cheese_price=small_price + 1
#     print(f"your bill adding extra cheese in small pizza  is {cheese_price} ")
# elif extra_cheese=="Y":
#     cheese_price=medium_price + 1
#     print(f"your bill adding extra cheese in medium pizza  is {cheese_price} ")
# else:
#     cheese_price=large_price + 1
#     print(f"your bill adding extra cheese in large pizza  is {cheese_price} ")
#
# # else:
# # print("choose a valid  size")
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
bill=0
if size=="S":
    bill +=15
elif size=="M":
    bill +=20
elif size=="L":
        bill +=25
else:
    print("kindly check the size you want")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="Y":
    if size=="S":
        bill +=2
    else:
        bill+=3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese=="Y":
    bill +=1

print(f"Your final bill is: ${bill}.")

