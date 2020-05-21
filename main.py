from map import *


class Location:

    def __init__(self):
        self.name = None

    def setname(self, name):
        self.name = name


numlocations = int(input("How many locations do you want to travel to?\n")) + 1

locations = [Location() for i in range(numlocations)]

for i in range(numlocations):
    if i == 0:
        print("What is your starting location? (city,country)")
    else:
        print("What is the " + str(i) + " place? (city,country)")

    locations[i].setname(getLocation(input()))

for i in range(numlocations):
    print(locations[i].name)
