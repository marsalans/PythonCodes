print "These are examples of lists"

colours = ['red', 'green', 'blue']
numbers = [1, 2, 3]

print colours
print numbers

for colour in colours:
	print "This is: %r" %colour

for number in numbers:
	print "This is: %d" %number

#to build lists, use the following code as shown below

array1 = [] #defining an empty array

for i in range(0,5): 
	#this adds the numbers from 0 to 4
	print "Adding %d to the list" %i
	array1.append(i) 
	#to add the elements in the array

#similarly to print the added elements

for i in array1:
	print "This is: %d" %i