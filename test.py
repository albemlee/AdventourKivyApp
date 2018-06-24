from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image, AsyncImage

beach_image = AsyncImage(source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/20100726_Kalamitsi_Beach_Ionian_Sea_Lefkada_island_Greece.jpg/1920px-20100726_Kalamitsi_Beach_Ionian_Sea_Lefkada_island_Greece.jpg')
city_image = AsyncImage(source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Sheth_Motisha_Tonk_01.jpg/600px-Sheth_Motisha_Tonk_01.jpg')
paragliding_image = AsyncImage(source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Paragliding_Sopelana_Biscay.jpg/440px-Paragliding_Sopelana_Biscay.jpg')
forest_image = AsyncImage(source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Biogradska_suma.jpg/440px-Biogradska_suma.jpg')
bar_image = AsyncImage(source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Bar-P1030319.jpg/1920px-Bar-P1030319.jpg')
peacock_image = AsyncImage(source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Peacock_Plumage.jpg/520px-Peacock_Plumage.jpg')


class Adventour(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Pick one!',
        font_size=15)

Builder.load_string("""
<ButtonsApp>:
    orientation: "vertical"
    Button:
        text: "B1"
        Image:
            source: 'kivy.png'
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            size: 250, 250
            allow_stretch: True
    Label:
        text: "A label"
""")

class ButtonsApp(App, BoxLayout):
    def build(self):
        return self

        layout = AnchorLayout(
        anchor_x='right', anchor_y='bottom')
        btn = Button(text='Hello World', Image=beach_image)
        layout.add_widget(btn)

        f.add_widget(beach_image)
        f.add_widget(city_image)
        f.add_widget(paragliding_image)
        s.add_widget(bar_image)
        return f

if __name__ == "__main__":
    Adventour().run()
