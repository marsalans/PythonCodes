True and True
False and False
1==1 and 1==0

cars = 27
buses = 14
trucks = 30

if cars > buses:
	print "Cars are more than buses!"

if buses < trucks:
	print "Buses are less than !"

if cars > trucks:
	print "Cars are more than buses!"
else:
	print "Check statement!"

if cars > buses and buses > trucks:
	print True
else:
	print False

if cars < buses or buses > trucks:
	print True
elif cars > buses:
	print False
