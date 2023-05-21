#!/usr/bin/env python3

class Dog:
    # body class
    def sit(self):
        print("The dog is sitting.")
    
    def bark(self):
        print("Woof!")

# an instance of the Dog class
snoopy = Dog()

# Calling the sit() method on the snoopy instance
snoopy.sit()

# Calling the bark() method on the snoopy instance
snoopy.bark()