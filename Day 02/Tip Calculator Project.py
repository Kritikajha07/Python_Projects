print("welcome to the tip calculator")
bill=float(input("what was the total bill $ "))
# print(bill)
tip=float(input("what tip would you like to give 10,12 or 15 "))
# print(tip)
split=int(input("how many people want to split the bill? "))
# print(split)
total_bill_tip=tip / 100 *bill + bill
total_bill=total_bill_tip / split
print(f"each person should pay {total_bill}")


