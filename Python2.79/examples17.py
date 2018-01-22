content = {"name": "James", "age": "20", "country": "Denmark"}
print content["name"]
# this is called dictionary. It is used to store information and to
# retrieve the stored information
print content['age']

content2 = ['a', 'b', 'c']
print content2[0]

# to delete stuff use del keyword

del content2[1]
print content2

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

for x in states:
	print states[x]

state = states.get('Texas')

if not state:
    print "Sorry, no Texas."
