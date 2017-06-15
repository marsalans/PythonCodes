'''

def print_data(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)
print_data("Wassup", "Mah man!")

def print_none():
	print "Nopes"
print_none()

# def allows us to create user defined functions as you can see above. To get the required output pass the no. of args as required.
# Be sure to give colon after the parenthesis

'''

from sys import argv

script, in_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_line(line_count, f):
	print line_count, f.readline()

current_file = open(in_file)
print "The whole file is:\n"

print_all(current_file)
print "Now going to the beginning of the file"

rewind(current_file)
print "Printing 3 lines"

current_line = 1
print_line(current_line, current_file)

current_line = current_line + 1
print_line(current_line, current_file)

current_line = current_line + 1
print_line(current_line, current_file)

# try extending the line print by copy pasting the above 2 statements. Check data3.txt to see what would be printed