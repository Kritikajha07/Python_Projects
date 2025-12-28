# def format_name(f_name,l_name):
#     f_name= f_name.title()
#     l_name=l_name.title()
#     return f_name+" "+ l_name
#
# print(format_name(f_name="kritiKa",l_name="JhA"))
#
#

def function_1(text):
    return text+" "+ text

def function_2(text):
    return text.title()

output=function_2(function_1("hieeeee"))
print(output)
