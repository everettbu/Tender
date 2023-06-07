import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from fetch import fetch_restaurants

# Bypasses SSL verification (needs to be fixed)
import ssl
from urllib.request import urlopen
ssl._create_default_https_context = ssl._create_unverified_context

kivy.require('2.0.0')

class Tender(App):
    def build(self):
        layout = StackLayout()

        for restaurant in fetch_restaurants():
            label = Label(text=restaurant['name'])
            image = AsyncImage(source=restaurant['image_url'])

            restaurant_widget = StackLayout()
            restaurant_widget.add_widget(image)
            restaurant_widget.add_widget(label)

            layout.add_widget(restaurant_widget)

        return layout

    def favorite_restaurant(self, restaurant):
        # TODO: Add restaurant to user's favorites list.
        pass


if __name__ == '__main__':
    Tender().run()