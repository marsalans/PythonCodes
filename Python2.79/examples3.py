from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

# run command like this: python ex13.py first 2nd 3rd in cmd
# first, 2nd 3rd names can be any names

script, user_name = argv
cmd = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(cmd)

print "Where do you live %s?" % user_name
lives = raw_input(cmd)

print "What kind of computer do you have?"
computer = raw_input(cmd)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

# by removing script and respective arguments, some unexpected things happen.
# do check that out

