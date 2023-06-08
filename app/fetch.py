import requests
import json

API_KEY = "jUfIkEVK3dqjWE56cm0fwJYb3Q9reoBLfB-Glts0gHp17-6OLgSwl-ttbTvhjL_datKjk1KB-rnrR3r-2bdz4tCdVcCfD6WcEBV0b_Nb5J3saM1O9gi_J6VpheKAZHYx"

def fetch_restaurants():
    url = "https://api.yelp.com/v3/businesses/search?term=restaurants&location=austin&limit=2"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    restaurants = data["businesses"]

    return restaurants

def fetch_photos(business_id):
    url = f"https://api.yelp.com/v3/businesses/{business_id}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    photos = data.get("photos", [])

    return photos
