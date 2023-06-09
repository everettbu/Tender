import requests

API_KEY = 'AIzaSyA-_xhU4zr04MiShUCvaso-atYGofXU1fM'
LOCATION = '30.2672,-97.7431'
RADIUS = 1000
SEARCH_TYPE = 'restaurant'
NUM_RESULTS = 10
NUM_PHOTOS = 3

def fetch_restaurants():
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LOCATION}&radius={RADIUS}&type={SEARCH_TYPE}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'results' in data:
        restaurants = data['results'][:NUM_RESULTS]
        formatted_restaurants = []
        for restaurant in restaurants:
            formatted_restaurant = {
                'id': restaurant['place_id'],
                'name': restaurant['name'],
                'address': restaurant['vicinity'],
            }
            formatted_restaurants.append(formatted_restaurant)
        return formatted_restaurants
    else:
        return []

def fetch_photos(place_id):
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=photos&key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'result' in data and 'photos' in data['result']:
        photos = data['result']['photos'][:NUM_PHOTOS]
        photo_urls = []
        for photo in photos:
            photo_reference = photo['photo_reference']
            photo_url = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={API_KEY}'
            photo_urls.append(photo_url)
        return photo_urls
    else:
        return []

if __name__ == '__main__':
    restaurants = fetch_restaurants()
    for restaurant in restaurants:
        place_id = restaurant['place_id']
        photos = fetch_photos(place_id)
        print(f"Photos for {restaurant['name']}: {photos}")
        print("-" * 40)
