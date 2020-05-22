#skyscanner flight look up

import requests
from skyscanner.skyscanner import Flights

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
    result =