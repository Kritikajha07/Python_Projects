# LIST COMPREHENSION 
# new_list=[new_item for item in list]

# numbers=[1,2,3]
# new_numbers=[n+1 for n in numbers]
# print(new_numbers)

# name="kritika"
# new_name=[letter for letter in name]
# print(new_name)

# new_list=[n*2 for n in range(1,5)]
# print(new_list)


# Conditional List Comprehension
# new_list=[new_item for item in list if test]

# number=[1,2,3,4,5,6]
# new_num=[n for n in number if n>4]
# print(new_num)

# name=["kritika","suman","priya","sneha"]
# new_name=[n.upper() for n in name if len(n)>1]
# print(new_name)

# Dictionary Comprehension
# new_dict={new_key:new_value for item in list}
# new_dict={new_key:new_value for (key,value) in dict.items()}
# new_dict={new_key:new_value for (key,value) in dict.items() if test}

# import random
# names=["kritika","suman","priya","sneha"]
# students_score={student:random.randint(1,100) for student in names} 

# passed_students={s:score for (s,score) in students_score.items() if score>=60}
# print(passed_students)

# LOOPING THROUGH DICTIONARIES
# item={"name":["kritika","Angela","Connor"],
#       "marks":[24,30,28]}
     

# for (key,values) in item.items():
#     print(key)

# import pandas
# student_data_frame=pandas.DataFrame(item)
# print(student_data_frame)

#LOOPING THROUGH A DATAFRAME
# for (key,values) in student_data_frame.items():
#     print(values)

#LOOPING THROUGH ROWS OF  A DATAFRAME
# for(index,row) in student_data_frame.iterrows():
#     print(row)



# NATO ALPHABET PROJECT

import pandas as pd
data=pd.read_csv("Day-26-NATO_alphabet_project/nato_phonetic_alphabet.csv")
nato_dict={row["letter"]:row["code"] for _, row in data.iterrows()}

user_input=input("Enter a word: ").upper()
output=[nato_dict[letter] for letter in user_input]
print(output)

