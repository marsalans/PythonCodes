#creation of class

class MyStuff(object):

    def firstClass(self):
        self.text = "This is a statement"

    def firstClass_a(self):
        print "This is another statment"

param = MyStuff() #declaration and instatiation of an object
param.firstClass_a()

#the statament below has been commented since it is giving errors
#check exercise 40

#print param.text #check why this is giving errors

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()