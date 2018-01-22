'''

with open('texts\pi_digits.txt') as txt_obj1:
    txt_contents = txt_obj1.read()
    print(txt_contents)

#the keyword 'with' is used as it closes the file once the access is no longer required
#rstrip() method removes, or strips, any whitespace characters from the right side of a string

print("*******************")

file_dest = 'texts\pi_digits.txt'

with open(file_dest) as txt_obj2:
    for line in txt_obj2:
        print(line.rstrip())
        #try printing w/o rstrip

print("*******************")

with open(file_dest) as txt_obj3:
    lines = txt_obj3.readlines()

#stores the contents of the file line by line in lines


# for line in lines:
#     print(line.rstrip())

#printing contents line by line

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

file_dest2 = 'texts\pi_mil_digits.txt'

with open(file_dest2) as txt_obj4:
    lines = txt_obj4.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Birth date in ddmmyy: ")
if birthday in pi_string:
    print("Your birth date " + birthday + " is in the first million digits of pi")

file_dest3 = 'texts\write.txt'
choice = 'yes'

with open(file_dest3, 'a') as txt_obj4:
    while choice != 'no':
        input_text = input("Type some text: ")
        txt_obj4.write(input_text + "\n")
        choice = input('Do you want to continue?\nyes or no: ')

'''


try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")

file_name = 'texts\pi_digits.txt'

try:
    with open(file_name) as txt_obj5:
        print(txt_obj5.read())
except FileNotFoundError:
    print("File not found!")

file_war = 'texts\war_and_peace.txt'
file_tale_of_two_cities = 'texts\cities.txt'
no_file = 'texts\sample.txt'


def count_words(filename):
    try:
        with open(filename) as txt_obj6:
            file_content = txt_obj6.read()
    except FileNotFoundError:
            pass
            # print("File not found!")

            #the pass keyword tells python to continue the operation without producing a traceback. try uncommenting the print 
    else:
        words = file_content.split()
        num_words = len(words)
        print("There are " + str(num_words) + " words")


count_words(file_tale_of_two_cities)
count_words(no_file)





# with open('file1.pdf') as pdf_obj1:
#     pdf_con = pdf_obj1.read()
#     print(pdf_con)
