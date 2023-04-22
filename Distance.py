# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 08:50:43 2023

@author: Tuo Sa
"""

import requests

def get_distance(origin, destination, api_key):
    """
    Calculate the driving distance (in miles) between two locations using the Google Maps API.

    Args:
        origin (str): The starting location. Can be an address or latitude/longitude coordinates.
        destination (str): The destination location. Can be an address or latitude/longitude coordinates.
        api_key (str): Your Google Maps API key.

    Returns:
        float: The driving distance (in miles) between the two locations.
    """

    # Build the API request URL.
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "mode": "driving",
        "units": "imperial",
        "key": api_key
    }

    # Send the API request and parse the response.
    response = requests.get(url, params=params)
    data = response.json()

    # Extract the driving distance from the response.
    try:
        distance_text = data["rows"][0]["elements"][0]["distance"]["text"]
        #the dictionary only consiist of 1 row and 1 element in the row, hence we access by [0].
        distance_value = float(distance_text.replace(",", "").split(" ")[0])
        return distance_value
    except Exception as e:
        print(f"Error getting distance: {e}")
        return None

#Implement the function
origin = input('Your startig location:')
destination = input('Your destination:')
api_key = input('Your API Key:')

distance = get_distance(origin, destination, api_key)
print(f"The driving distance from {origin} to {destination} is {distance} miles.")







