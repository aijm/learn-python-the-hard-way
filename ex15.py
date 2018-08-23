# EXERCISE 15: Reading Files
# import argv feature from sys package
from sys import argv
# unpack argument variables
script = argv
# open file
filename = input("Enter filename: ")
txt = open(filename)

print(f"Here's your file {filename}:")
# print text of filename
print(txt.read())
txt.close()
# get filename by "input"
# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)
# # print text of file_again
# print(txt_again.read())