try:
    age = int(input("How old are you?"))
except ValueError:
    print("You did enter an invalid number. Kindly enter a numerical entry such as 23.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at  {age}.")
else:
    print("Cannot drive  ")
