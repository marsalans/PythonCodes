from sys import exit

def room1():
    print "Welcome mortal! Which room do you choose?\n1, 2 or 3?"

    choice1 = raw_input("Enter Option: ")
    if (choice1 == "1" or choice1 == "3"):
        #Remember to use brackets to combine two if statements into 1.
        print "Congratulations! You have proceeded to the next room!"
        room2()
    elif choice1 == "2":
        print "No luck. You die here"
    else:
        dead("Type the correct room no.");

def room2():
    print "Oh! I see you've made it this far\nNow choose! Room 4 or 5?\nAnd a no: 6 or 7"

    choice2 = raw_input("Enter Option: ")
    choice2b = raw_input("Enter Option: ")

    if "4" in choice2 and "6" in choice2b:
        dead("Congratulations! You have completed the game!")
    else:
        dead("No luck. You die here")

def dead(reason):
    print reason, "Bye!"
    exit(0)

room1()
