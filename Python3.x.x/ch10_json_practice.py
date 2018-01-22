import json

nos = [1, 4, 23, 89, 12, 34, 6]

file1 = 'numbers.json'
with open(file1, 'w') as obj1:
    json.dump(nos, obj1)

with  open(file1, 'r') as obj2:
    nos2 = json.load(obj2)

print(nos2)










