from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
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
        return data['results'][:NUM_RESULTS]
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
        print(f"No photos found for {place_id}")
        return []

class RestaurantApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        restaurants = fetch_restaurants()
        for restaurant in restaurants:
            place_id = restaurant['place_id']
            photos = fetch_photos(place_id)
            for photo_url in photos:
                image = Image(source=photo_url)
                layout.add_widget(image)

        return layout

if __name__ == '__main__':
    RestaurantApp().run()
