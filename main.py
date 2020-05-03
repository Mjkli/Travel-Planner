class Location:
    name = None

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


numlocations = int(input("How many locations do you want to travel to?\n"))


locations = [Location() for i in range(numlocations)]


for i in range(numlocations):
    if i == 0:
        print("What is your starting location?")
    else:
        print("What is the " + str(i) + " place?")

    locations[i].name = input()


for i in range(numlocations):
    print(Location.name + "\n" + Location.nextLocation + "\n")
