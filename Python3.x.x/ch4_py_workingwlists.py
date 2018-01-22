count = 0
names = ['abc', 'def', 'ghi', 'jkl', 'mno']
for name in names:
    print(name)
    count = count + 1
print("There are " + str(count) + " names")
#name is the variable in which you are storing value and names is the list you want to iterate
#indentation is important in loops

print("\n*******************************************\n")

for value in range(2, 7):
    print(value)

numbers = list(range(2, 11))
print(numbers)
#list() function converts the gievn param into list

numbers2 = list(range(2, 11, 2))
print(numbers2)
#range() takes 3 params: start, stop, and steps. in this case it will skip 1 no and store the value

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

print("\n*******************************************\n")

numbers3 = list(range(1, 11))
print(min(numbers3))
print(max(numbers3))
print(sum(numbers3))

squares2 = [value ** 2 for value in range(1,11)]
print(squares2)
#list comprehension

million = list(range(1, 1000001))
print(sum(million))

print("\n*******************************************\n")

cubes = [value ** 3 for value in range(1, 11)]
for value in cubes:
    print(value)

players = ['john', 'dinesh', 'rita', 'sona', 'mohan', 'mona', 'tillu']
print(players[2:5])
#this is called slicing of lists to print a part of list

print(players[:3])
#to start from beginning till 4th element

print(players[-3:])
#to print from 3rd last element till the last element

print("\n*******************************************\n")

for player in players[:3]:
    print(player)

original_list = [1, 2, 3, 4]
copied_list = original_list[:]

print(original_list)
print(copied_list)

param = (10, 20)
print(param[0])
for val in param:
    print(val)

print("\n*******************************************\n")

#param is a tuple. tuple is basically a list whose values cannot be changed
#try the below example

#param[0] = 22

#although you can’t modify a tuple, you can assign a new value to a variable that holds a tuple. 

param = (20, 30)
for val in param:
    print(val)