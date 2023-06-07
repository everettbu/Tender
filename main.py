import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from fetch import fetch_restaurants


import ssl
ssl._create_default_https_context = ssl._create_unverified_context
"""
Needs to be fixed, replace '/path/to/certificate.pem'  with the actual path to SSL certificate file.
import ssl
ssl._create_default_https_context = ssl.create_default_context(cafile="/path/to/certificate.pem")
"""

kivy.require('2.0.0')

class Tender(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.restaurants = fetch_restaurants()
        self.current_index = 0

        self.label = Label(text=self.restaurants[self.current_index]['name'])
        self.image = AsyncImage(source=self.restaurants[self.current_index]['image_url'])
        self.restaurant_widget = BoxLayout(orientation='vertical')
        self.restaurant_widget.add_widget(self.image)
        self.restaurant_widget.add_widget(self.label)

        layout.add_widget(self.restaurant_widget)

        # Button layout
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        # Favorite Button
        favorite_button = Button(text="Favorite", size_hint=(0.5, None), height=50)
        favorite_button.bind(on_press=self.favorite_restaurant)
        button_layout.add_widget(favorite_button)

        # Skip Button
        skip_button = Button(text="Skip", size_hint=(0.5, None), height=50)
        skip_button.bind(on_press=self.skip_restaurant)
        button_layout.add_widget(skip_button)

        layout.add_widget(button_layout)

        return layout

    def favorite_restaurant(self, instance):
        # Add restaurant to user's favorites list
        restaurant = self.restaurants[self.current_index]
        # Implement your logic to add the restaurant to favorites
        print(f"Restaurant '{restaurant['name']}' added to favorites.")

        # Move to the next restaurant
        self.current_index += 1

        if self.current_index < len(self.restaurants):
            self.label.text = self.restaurants[self.current_index]['name']
            self.image.source = self.restaurants[self.current_index]['image_url']
        else:
            self.label.text = "No more restaurants"
            self.image.source = ""

    def skip_restaurant(self, instance):
        # Move to the next restaurant
        self.current_index += 1

        if self.current_index < len(self.restaurants):
            self.label.text = self.restaurants[self.current_index]['name']
            self.image.source = self.restaurants[self.current_index]['image_url']
        else:
            self.label.text = "No more restaurants"
            self.image.source = ""

if __name__ == '__main__':
    Tender().run()
    