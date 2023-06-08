import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from app.fetch import fetch_restaurants, fetch_photos
from app.circlebutton import CircleButton

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

kivy.require('2.0.0')


class Tender(App):
    def build(self):
        layout = FloatLayout()
        self.restaurants = fetch_restaurants()
        self.current_restaurant = 0
        self.photos = fetch_photos(self.restaurants[self.current_restaurant]['id'])
        self.current_photo = 0

        # Display the first photo
        self.image = AsyncImage(source=self.photos[self.current_photo], size_hint=(1, 0.9))
        self.image.bind(on_touch_down=self.on_image_touch_down)
        layout.add_widget(self.image)


        # Button to skip to the next restaurant
        skip_button = CircleButton(
            source='skip.png',
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={'center_x': 0.4, 'y': 0.1}
        )
        skip_button.bind(on_release=self.on_skip_button_release)
        layout.add_widget(skip_button)

        # Button to favorite the restaurant
        favorite_button = CircleButton(
            source='favorite.png',
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={'center_x': 0.6, 'y': 0.1}
        )
        favorite_button.bind(on_release=self.on_favorite_button_release)
        layout.add_widget(favorite_button)

        return layout

    def on_image_touch_down(self, instance, touch):
        if touch.is_double_tap:
            return

        # Increment the current photo index
        self.current_photo += 1

        # Check if all photos for the current restaurant have been displayed
        if self.current_photo >= len(self.photos):
            # Reset the photo index
            self.current_photo = 0

        # Update the displayed photo
        self.image.source = self.photos[self.current_photo]

    def all_restaurants_displayed(self):
        return self.current_restaurant >= len(self.restaurants)

    def display_no_restaurants_available_message(self):
        self.image.source = ''  # Clear the current photo
        self.image.opacity = 0.5  # Set the image opacity to indicate no more restaurants
        self.image.disabled = True  # Disable touch events on the image

        message_label = Label(
            text='No more restaurants available',
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            color=(1, 0, 0, 1)  # Set the label text color to red
        )
        self.root.add_widget(message_label)

    def on_favorite_button_release(self, instance):
        # Add your logic to handle favoriting the current restaurant
        print("Restaurant favorited!")

        # Increment the current restaurant index
        self.current_restaurant += 1

        # Check if all restaurants have been displayed
        if self.all_restaurants_displayed():
            self.display_no_restaurants_available_message()
            return

        # Fetch photos for the next restaurant
        self.photos = fetch_photos(self.restaurants[self.current_restaurant]['id'])
        self.current_photo = 0

        # Update the displayed photo
        self.image.source = self.photos[self.current_photo]

    def on_skip_button_release(self, instance):
        # Increment the current restaurant index
        self.current_restaurant += 1

        # Check if all restaurants have been displayed
        if self.all_restaurants_displayed():
            self.display_no_restaurants_available_message()
            return

        # Fetch photos for the next restaurant
        self.photos = fetch_photos(self.restaurants[self.current_restaurant]['id'])
        self.current_photo = 0

        # Update the displayed photo
        self.image.source = self.photos[self.current_photo]


    def on_pause(self):
        return True


if __name__ == '__main__':
    Tender().run()
