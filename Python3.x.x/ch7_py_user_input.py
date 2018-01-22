'''
NOTE:
    In this script I'll be disabling a lot of lines since I would have to give the input for each input code.

'''

# name = input("What is your name? ")
# print("So your name is " + name)


'''

prompt = "Tell us your name and the message will be personalized"
prompt += "\nWhat is your name? "
name = input(prompt)

print("Hello " + name)

age = input("How old are you? ")
print("So you are " + age + " years old and")
age  = int(age)
#typecasting the string value to int to compare and perform all sorts of operations
if age >= 18:
    print("Above 18!")
else:
    print("Below 18")

'''


'''

num = 5
while num >= 0 :
    print(num)
    num -= 1

prompt = "Type 'quit' to quit else I will continue: "

message = " "
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#an example of while loop



prompt = "Type 'quit' to quit else I will continue: "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#same while loop by using flag as active

'''


'''

prompt = "Type 'quit' to quit else I will continue: "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)

#while loop using break


'''


'''

c_no = 0
while c_no < 10:
    c_no += 1
    if c_no % 2 == 0:
        continue
    print(c_no)

#this loop uses continue. continue continues the loop rather than breaking out of the loop

'''

list1 = ['bob', 'james', 'lily']
list2 = []

while list1:
    list_item = list1.pop()
    list2.append(list_item)

print("List 2 contains: ")
for list_item2 in list2:
    print(list_item2)

#copying list items from 1 list to another

num_list = [1, 2, 3, 4, 1, 1, 1, 3, 4, 7, 8, 45, 23, 12, 9]

while 1 in num_list:
    num_list.remove(1)

print(num_list)
#removing several occurences of an item in a list using remove()


responses = {}

# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")



