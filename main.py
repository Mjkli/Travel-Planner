class Location:

    def __init__(self):
        self.name = None
        self.hotel = None
        self.hotelcost = 0
        self.totalcost = self.hotelcost
        self.nextLocation = None

    def Location(self):
        pass


    def nlocation(self, Location):
        self.nextLocation = Location

    def setname(self, name):
        self.name = name


numlocations = int(input("How many locations do you want to travel to?\n")) + 1


locations = [Location() for i in range(numlocations)]


for i in range(numlocations):
    if i == 0:
        print("What is your starting location?")
    else:
        print("What is the " + str(i) + " place?")

    locations[i].setname(input())


