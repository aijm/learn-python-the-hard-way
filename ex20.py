# EXERCISE 20: Functions and Files

from sys import argv
script, input_file = argv

# define a function to print file
# arguments: f (TextIOWrapper)
def print_all(f):
    print(f.read())

# 设置文件当前位置为最开始处
def rewind(f):
    f.seek(0)

# print a line of file with line number
def print_a_line(line_count, f):
    print(line_count,f.readline(),end = '')

# open input_file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
