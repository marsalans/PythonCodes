butter = 100
milk = 2
print "I am buying %d" % butter, "g butter and %d" % milk, "l milk"
shirt_colour = 'red'
print "I am wearing %r" % shirt_colour, "colour shirt" #by using format specifier 'r' you tell python to print it no matter what. 's' is used for printing string
													   #notice that i have not given comma after the 1st print message as i am using format specifier
is_python = 'cool'
print "learning python is %s" % is_python #see that i have not used double quotes for cool, stil it is being printed
grade1 = 'A'
grade2 = "B"
print "I have got %s in Math and %s in Geography" % (grade1, grade2) 

anime = "Naruto "
cool = "is awesome!"
print anime + cool

print "---------------------------------------" #just to create a partition

print "I want %s" %'bananas' " They are %s" %"awesome"
print "." * 39 #just learned this.

char1 = "pa"
char2 = "ra"
char3 = 'no'
char4 = 'id'

char5 = "an"
char6 = "dr"
char7 = "oid"

print char1 + char2 + char3 + char4  #see that the comma at the end of line 34 makes a difference
print char5 + char6 + char7

print char1 + char2 + char3 + char4,
print char5 + char6 + char7

array = "%r %r %r"
print array %(1, 2, 3)
print array %('one', 'two', 'three')
print array %(array, array, array) #if you give only 2 arguments, it will not work
print array %("You can even", "write", "sentences")

print "*" * 39

print """ you can multiple lines
with
three double quotes
this is just awesome! """ #do not use spaces between double quotes

print "\a" #bell sound

# \\ 	Backslash (\)
# \' 	Single-quote (')
# \" 	Double-quote (")
# \a 	ASCII bell (BEL)
# \b 	ASCII backspace (BS)
# \f 	ASCII formfeed (FF)
# \n 	ASCII linefeed (LF)
# \N{name} 	Character named name in the Unicode database (Unicode only)
# \r 	Carriage Return (CR)
# \t 	Horizontal Tab (TAB)
# \uxxxx 	Character with 16-bit hex value xxxx (u'' string only)
# \Uxxxxxxxx 	Character with 32-bit hex value xxxxxxxx (u'' string only)
# \v 	ASCII vertical tab (VT)
# \ooo 	Character with octal value ooo
# \xhh 	Character with hex value hh

#while True:
#	for i in ["/","-","|","\\","|"]:
#       	print "%s\r" % i,             cool program to try!


string1 = "Hello man!"
string2 = "how are you?"

print "I said %r " %string1, "%s" %string2

var1 = "Kya baat hain"

print "Mast", var1 #see that i have not used %