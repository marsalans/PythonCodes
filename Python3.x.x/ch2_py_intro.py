name = "James bond"
print (name.title())

#changing case to lower and upper
print (name.lower())
print (name.upper())

#concatinating the sentences
part_one = "Blood "
part_two = "Sweat and "
part_three = "Pixels"
complete_title = part_one + part_two + part_three
print (complete_title)

# >>> fav = 'python '
# >>> fav
# 'python '
# >>> fav.rstrip()
# 'python'

#the above code was written in terminal. rstrip() is used to remove the whitespace if present at the right side
#use lstrip to remove whitespace from left side

# >>> fav1 = ' python '
# >>> fav1.rstrip()
# ' python'
# >>> fav1.lstrip()
# 'python '
# >>> fav1.lstrip().rstrip()
# 'python'

#converting int to string since python doesn't know whether it is 23 or 2 and 3
age = 20
message = "You are " + str(age) + " years old"
print (message)

#creating the ans in float: you should have at least one value in float
ans = 2.7/1.2
print (ans)

no1 = 5
message2 = "My fav no is " + str(no1 - 3)
print (message2)