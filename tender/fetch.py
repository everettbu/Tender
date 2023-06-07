import requests
import json

def fetch_restaurants():
    # TODO: Implement this function to fetch a list of restaurants from the Yelp API
    API_KEY = "S63qf_Ltc5hLAzK5gFx84Co0TrJ1rX3Tn5thptEThAA2jLp6EhVLoI9nUbqUZ77mv9jJdBUx8d6xr_P5q1usbCyYsFXAnNGKNHo9idWQqvWKzMOiQfOFVPZ4J3F_ZHYx"
    url = "https://api.yelp.com/v3/businesses/search?term=restaurants&location=austin"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    restaurants = data["businesses"]

    return restaurants
