from map import getLocation
from datetime import date
from flights import *


class Location:

    def __init__(self):
        self.city = None
        self.airport = None


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


leg1 = int(flightLookup(locations[0].airport, locations[1].airport, departdate))
leg2 = int(flightLookup(locations[1].airport, locations[0].airport, arriveDate))

print("First leg = " + str(leg1) + "\nSecond leg = " + str(leg2) + "\nTotal = " + str(leg1 + leg2))

