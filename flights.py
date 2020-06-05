# Skyscanner flight look up

import requests
import json
import config


# Get the (Generic) airport for the specified location
def locationLookup(location):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

    querystring = {"query": location}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': config.api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    js = json.loads(response.text)
    return js['Places'][0]['PlaceId']


# Get flight pricing for starting location to destination at specified date
def flightLookup(origin, destination, outdate):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-USD/"
    url += origin + "/" + destination + "/" + str(outdate)

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': config.api_key
    }

    response = requests.request("GET", url, headers=headers)

    js = json.loads(response.text)

    if js['Quotes']:
        return js['Quotes'][0]['MinPrice']
    else:
        print("Error! No route from " + origin + " to " + destination + " date: " + str(outdate))
        return 0
