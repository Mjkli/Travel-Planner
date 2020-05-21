class Location:

    def __init__(self):
        self.name = None
    def setname(self,name):
        self.name = name



numlocations = int(input("How many locations do you want to travel to?(city,country)\n")) + 1


locations = [Location() for i in range(numlocations)]


for i in range(numlocations):
    if i == 0:
        print("What is your starting location?")
    else:
        print("What is the " + str(i) + " place?")

    locations[i].setname(input())

for i in range(numlocations):
    print(locations[i].name)


    #test




