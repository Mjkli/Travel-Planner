#need config.py to hold apikey


from map import getLocation
from datetime import date
from flights import *


class Location:

    def __init__(self):
        self.city = None
        self.airport = None
        self.outPrice = 0


def getDates():
    global departdate
    global arriveDate
    print("What year are you leaving?")
    departyear = int(input())
    print("what is the month?")
    departmonth = int(input())
    print("what is the day?")
    departday = int(input())

    departdate = date(departyear, departmonth, departday)

    print("How Long is your trip?(days)")
    time = int(input()) + departday - 1
    arrivemonth = departmonth
    arriveyear = departyear

    if time > 30:
        arrivemonth += 1
        time -= 30

    arriveDate = date(arriveyear, arrivemonth, time)
    print(arriveDate)


numlocations = int(input("How many locations do you want to travel to?\n")) + 1


locations = [Location() for i in range(numlocations)]

for i in range(numlocations):
    if i == 0:
        print("What is your starting location? (city)")
    else:
        print("What is the " + str(i) + " place? (city)")

    locations[i].city = getLocation(input())

for i in range(numlocations):
    print(locations[i].city)


print("How Many Adults are going?")
numAdults = int(input())
if numAdults > 8:
    numAdults = 8

departdate = 0
arriveDate = 0
getDates()

for i in range(locations.__len__()):
    locations[i].airport = locationLookup(locations[i].city)


total = 0
for i in range(len(locations)):
    if i == len(locations) - 1:
        locations[i].outPrice = int(flightLookup(locations[i].airport, locations[0].airport, departdate))
    else:
        locations[i].outPrice = int(flightLookup(locations[i].airport, locations[i + 1].airport, departdate))
    total += locations[i].outPrice
    print(locations[i].city + ": " + str(locations[i].outPrice))

print("total price: " + str(total))


