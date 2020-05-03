

class Location:
    def __init__(self):
        self.name = None
        self.hotel = None
        self.hotelcost = 0
        self.totalcost = self.hotelcost


numlocations = int(raw_input("How many locations do you want to travel to?\n"))

locations = [Location() for i in range(numlocations)]

locations[0].name = raw_input("What is the first location you want to travel?\n")

locations[0].hotelcost = 300
print(locations[0].hotelcost)

