from sys import argv

script, filename = argv

txt = open(filename)
print "Here is your filename %r" %filename
print txt.read()


print "Type the filename again: "
filename_again = raw_input()

txt_again = open(filename_again)
print txt_again.read()
txt_again.close()