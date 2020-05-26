# skyscanner flight look up

import requests
from skyscanner.skyscanner import Flights
from skyscanner.skyscanner import FlightsCache
import json

flights_service = Flights('4514fef5c4mshcc9b62cf94b5e59p151d73jsn4fe875a542d7')


def flightLookup(origin, destination, indate, outdate, adults):
    result = flights_service.get_result(
        country='US',
        currency='USD',
        locale='en-US',
        originplace=origin,
        destinationplace=destination,
        outbounddate=outdate,
        inbounddate=indate,
        adults=adults
    ).parsed
    return result


def locationLookup(location):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

    querystring = {"query": location}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "4514fef5c4mshcc9b62cf94b5e59p151d73jsn4fe875a542d7"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    js = json.loads(response.text)

    return js['Places'][1]['PlaceId']


def flighttake2(origin, destination, indate, outdate):

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/"
    # url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/country/%currency%/%locale%/%originplace%/%destinationplace%/%outboundpartialdate%/%inboundpartialdate%"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "4514fef5c4mshcc9b62cf94b5e59p151d73jsn4fe875a542d7"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)