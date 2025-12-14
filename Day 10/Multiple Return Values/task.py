# def format_name(f_name, l_name):
#     if f_name=="" or l_name=="":
#         return "Please enter your first name and last name"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("What is your first name? "), input("What is your last name? ")))
#

def is_leap_year(year):
    if year % 4 == 0:
        return "True"

    elif year % 100 != 0:
        return "False"

    elif year % 400 == 0:
        return "True"


print(is_leap_year(2028))
