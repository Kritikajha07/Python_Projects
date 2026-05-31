# with open("Day 24-The_Mail_Merge/my.txt") as my_file:
#     contents=my_file.read()
#     print(contents)


# with open("Day 24-The_Mail_Merge/my.txt",mode="r") as my_file:
#     my_file.write("Hello World")
#     my_file.write("\n how are you doing?")

# with open("Day-24-The_Mail_Merge/my.txt", "r") as file:
#     print(file.read())


# here 'a' stands for append as we want to add any kind of text to our existing file.
# if we use 'w' instead os 'a' then it will delete the existing text and write new text from scratch. 
# 'r' is to read the file contents.


# with open("Day-24-The_Mail_Merge/my.txt", "a") as file:   
#     file.write("\n i am doing great  thanks ")

# with open("Day-24-The_Mail_Merge/my_file1.txt", "w") as file:   
#     file.write("this is a new file which is untracked")    

with open("Day-24-The_Mail_Merge/Input/Names/invited_names.txt",'r') as my_file:    
    names=my_file.readlines()

with open("Day-24-The_Mail_Merge/Input/Letters/starting_file.txt",'r') as my_file:    
    letter=my_file.read()

for name in names:
    name=name.strip()

    new_letter=letter.replace("[name]",name)

    with open(f"Day-24-The_Mail_Merge/Output/ReadyToSend/letter_for_{name}.txt",'w') as my_file:
        my_file.write(new_letter)
        