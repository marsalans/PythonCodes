'''
print "Hey man!"
res = raw_input()

print "Did you enjoy the film?"
res2 = raw_input()

print "How many did you watch?"
res3 = int(raw_input())

print "So you are %r. %r you liked the film. You watched %r films" %(res, res2, res3)

'''
#i used ''' to give multi-line comment

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third