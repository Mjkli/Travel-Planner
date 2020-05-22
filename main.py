from map import getLocation
from datetime import date
from flights import flightLookup


class Location:

    def __init__(self):
        self.city = None
        self.county = None
        self.State = None
        self.country = None


def getDates(date1, date2):
    print("What year are you leaving?")
    departyear = int(input())
    print("what is the month?")
    departmonth = int(input())
    print("what is the day?")
    departday = int(input())

    date1 = date(departyear, departmonth, departday)

    print("What year are you coming back?")
    arriveyear = int(input())
    print("what is the month?")
    arrivemonth = int(input())
    print("what is the day?")
    arriveday = int(input())

    date2 = date(arriveyear, arrivemonth, arriveday)


numlocations = int(input("How many locations do you want to travel to?\n")) + 1

locations = [Location() for i in range(numlocations)]

for i in range(numlocations):
    if i == 0:
        print("What is your starting location? (city,country)")
    else:
        print("What is the " + str(i) + " place? (city,country)")

    getLocation(input())

for i in range(numlocations):
    print(locations[i].city)
"""
print("How Many Adults are going?")
numAdults = int(input())
if numAdults > 8:
    numAdults = 8

departdate = 0
arriveDate = 0
getDates(departdate, arriveDate)

print(flightLookup(locations[0], locations[1], departdate, arriveDate, numAdults))
"""
