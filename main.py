from map import getLocation
from datetime import date
from flights import *



class Location:

    def __init__(self):
        self.city = None
        self.county = None
        self.State = None
        self.country = None
        self.airport = None


def getDates(date1, date2):
    print("What year are you leaving?")
    departyear = int(input())
    print("what is the month?")
    departmonth = int(input())
    print("what is the day?")
    departday = int(input())

    date1 = date(departyear, departmonth, departday)

    print("How Long is your trip?(days)")
    time = int(input()) + departday
    arrivemonth = departmonth
    arriveyear = departyear

    if time > 30:
        arrivemonth += 1
        time -= 30

    date2 = date(arriveyear, arrivemonth, time)


numlocations = int(input("How many locations do you want to travel to?\n")) + 1
#numlocations = 1


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

numAdults = 1
departdate = 0
arriveDate = 0
getDates(departdate, arriveDate)

for i in range(locations.__len__()):
    locations[i].airport = locationLookup(locations[i].city)


print(flightLookup(locations[1].airport, locations[0].airport, departdate, arriveDate, numAdults))


