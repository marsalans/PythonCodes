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

x = 0
array2 = []

while x <5:
	print "At the top i is %d" %x
	array2.append(x)

	x = x + 1
	print "Now the numbers are: ", array2
	array2.append(x)

print "The numbers: "

for num in array2:
	print num

'''
Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
Use this function to rewrite the script to try different numbers.
Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.

'''
