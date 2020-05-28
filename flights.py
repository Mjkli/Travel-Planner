# skyscanner flight look up

import requests
from skyscanner.skyscanner import Flights
from skyscanner.skyscanner import FlightsCache
import json

flights_service = Flights('4514fef5c4mshcc9b62cf94b5e59p151d73jsn4fe875a542d7')



def locationLookup(location):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

    querystring = {"query": location}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "4514fef5c4mshcc9b62cf94b5e59p151d73jsn4fe875a542d7"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    js = json.loads(response.text)

    return js['Places'][0]['PlaceId']


def flightLookup(origin, destination, outdate):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-USD/"
    url += origin + "/" + destination + "/" + str(outdate)

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "4514fef5c4mshcc9b62cf94b5e59p151d73jsn4fe875a542d7"
    }

    response = requests.request("GET", url, headers=headers)

    return response.text
