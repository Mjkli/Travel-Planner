# Locations to define where the user wants to travel
import geopy
from functools import partial
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Testing_app")
geocode = partial(geolocator.geocode, language="en")


def getLocation(string):
    return geocode(string)
