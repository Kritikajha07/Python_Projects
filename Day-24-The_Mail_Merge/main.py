# with open("Day 24/my.txt") as my_file:
#     contents=my_file.read()
#     print(contents)


with open("Day 24/my.txt",mode="w") as my_file:
    my_file.write("Hello World")
    my_file.write("\n how are you doing?")