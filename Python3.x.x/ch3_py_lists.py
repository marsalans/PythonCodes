alphabets = ['a', 'b', 'c', 'd']
print (alphabets)
#this will print the list as is

print (alphabets[2])
print (alphabets[-1])
#specifically mentioning which element to print

alphabets[2] = 'changed'
print (alphabets[2])
#modifying an element of the list

alphabets.append('e')
print (alphabets[-1])
#appending an element to the list

del alphabets[-1]
print  (alphabets[-1])
#deleting the last element

pop_alpha = alphabets.pop()
print (pop_alpha)
#popping the element (which is the last one) and storing it to get the popped value
#you cannot do this in case of del

print (alphabets[-1])
#verifying that the pop operation is completed

print (alphabets[0].title())
#just showing that you can use title, rstrip, etc for lists too

alphabets.remove('b');
print (alphabets)
#removeing an element by value

alphabets.append('to be removed')
print (alphabets)

rem1 = alphabets[-1]
alphabets.remove(rem1)
print (alphabets)
#you can use remove to remove assigned value too

nos = [2, 4, 1, 76, 43, 12, 90]
print (nos)

nos.sort()
print (nos)
#sorting the list. you can do this for strings too
#this sorts the list permanently

nos.sort(reverse=True)
print (nos)
#sorting the list in reverse fashion

#to maintain the original order of a list but present it in a sorted order, you can use the sorted() function.

names = ['john', 'ram', 'anthony', 'mayur']

print (names)
print (sorted(names))
print (names)

names.reverse()
print (names)
#reversing the list and not sorting the list in reverse order

print (len (names))
print (len (alphabets))
print (len (nos))