# Working in creating outdates for everylocation so the flight data can be accurate to that specific date

from map import getLocation
from datetime import date
from flights import *


class Location:

    def __init__(self):
        self.city = None
        self.airport = None
        self.outPrice = 0
        self.outDate = 0


# Gets Dates from the user so that it can have a date to look up
def getDates(locations):
    print("What year are you leaving?")
    departyear = int(input())
    print("What is the month?")
    departmonth = int(input())
    print("What is the day?")
    departday = int(input())

    departdate = date(departyear, departmonth, departday)

    print("How Long is your trip?(days)")
    time = int(input())

    timeline = int(time / len(locations)) + 1

    for i in range(len(locations)):
        if i == 0:
            locations[i].outDate = departdate
        else:
            departday += timeline
            if departday > 31:
                departday -= 31
                departmonth += 1
            departdate = date(departyear, departmonth, departday)
            locations[i].outDate = departdate


numlocations = int(input("How many locations do you want to travel to?\n")) + 1

locations = [Location() for i in range(numlocations)]

for i in range(numlocations):
    if i == 0:
        print("What is your starting location? (city)")
    else:
        print("What is the " + str(i) + " place? (city)")

    locations[i].city = input()

for i in range(numlocations):
    print(locations[i].city)

print("How Many Adults are going?")
numAdults = int(input())
if numAdults > 8:
    numAdults = 8

# get the dates for cities when you need to leave that location
getDates(locations)

# lookup the airport for the cities given by the user
for i in range(locations.__len__()):
    locations[i].airport = locationLookup(locations[i].city)

# Cycle through all list of locations and find the price from first location to the next
total = 0
for i in range(len(locations)):
    if i == len(locations) - 1:
        locations[i].outPrice = int(flightLookup(locations[i].airport, locations[0].airport, locations[i].outDate))
    else:
        locations[i].outPrice = int(flightLookup(locations[i].airport, locations[i + 1].airport, locations[i].outDate))
    total += locations[i].outPrice
    print(locations[i].city + ": " + str(locations[i].outPrice) + " : " + str(locations[i].outDate))

print("total price: " + str(total))
