import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.image import Image, AsyncImage
from kivy.config import Config
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import stop_words

global recommendations
global cluster_pipeline
global random_location
global random_location_2
global img_src

Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '960')

base_data = pd.read_csv("base_wiki_data.csv")
detroit_data = pd.read_csv("detroit_wiki_data.csv")

recommendations = detroit_data.copy()

def train_model(detroit_data):
    X = detroit_data["summary"]

    TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

    cluster_pipeline = Pipeline([
        ('vectorize', TfidfVectorizer(token_pattern=TOKENS_ALPHANUMERIC,
                                      ngram_range=(1, 2),
                                      stop_words=stop_words.ENGLISH_STOP_WORDS)),
        ('cluster', KMeans(n_clusters=7, random_state=22))
    ])

    cluster_pipeline.fit(X)

    return(cluster_pipeline)

def predict_cluster(attraction_row, cluster_pipeline):
    X = attraction_row["summary"]

    return(cluster_pipeline.predict(X))

def button_action(recommendations):
    train_model(recommendations)

while len(recommendations) > 15:
    cluster_model = train_model(recommendations)

    recommendations_w_clusters = recommendations
    recommendations_w_clusters['cluster'] = predict_cluster(recommendations, cluster_model)

    random_location = recommendations_w_clusters.sample(1) # This would happen in java

    recommendations = recommendations_w_clusters.loc[recommendations_w_clusters['cluster'] == random_location['cluster'].values[0],
                                                     ['attraction', 'url', 'summary', 'image']].copy()
    len(recommendations)

class MenuScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    random_location = recommendations.sample(1)
    img_str = random_location['image'].values[0]
    img_src = StringProperty(img_str)

class FourthScreen(Screen):
    random_location_2 = random_location.copy()
    while random_location_2['attraction'].values[0] == random_location['attraction'].values[0]:
        random_location_2 = recommendations.sample(1)
    random_location = random_location_2.copy()
    img_str = random_location['image'].values[0]
    img_src = StringProperty(img_str)

class FifthScreen(Screen):
    random_location_2 = random_location.copy()
    while random_location_2['attraction'].values[0] == random_location['attraction'].values[0]:
        random_location_2 = recommendations.sample(1)
    random_location = random_location_2.copy()
    img_str = random_location['image'].values[0]
    img_src = StringProperty(img_str)

class SixthScreen(Screen):
    random_location_2 = random_location.copy()
    while random_location_2['attraction'].values[0] == random_location['attraction'].values[0]:
        random_location_2 = recommendations.sample(1)
    random_location = random_location_2.copy()
    img_str = random_location['image'].values[0]
    img_src = StringProperty(img_str)

class SeventhScreen(Screen):
    random_location_2 = random_location.copy()
    while random_location_2['attraction'].values[0] == random_location['attraction'].values[0]:
        random_location_2 = recommendations.sample(1)
    random_location = random_location_2.copy()
    img_str = random_location['image'].values[0]
    img_src = StringProperty(img_str)

class EigthScreen(Screen):
    random_locations = recommendations.sample(3, replace=True)
    random_location_1 = random_locations['attraction'].values[0]
    random_location_2 = random_locations['attraction'].values[1]
    random_location_3 = random_locations['attraction'].values[2]
    label_src_1 = StringProperty(random_location_1)
    label_src_2 = StringProperty(random_location_2)
    label_src_3 = StringProperty(random_location_3)


class SwitchingScreenApp(App):
    def build(self):
        return Builder.load_file('screen.kv')
    def proceed_recommendations():
        if len(recommendations) > 15:
            cluster_model = train_model(recommendations)
            recommendations_w_clusters = recommendations.copy()
            recommendations_w_clusters['cluster'] = predict_cluster(recommendations, cluster_model)

            recommendations = recommendations_w_clusters.loc[recommendations_w_clusters['cluster'] == random_location['cluster'].values[0],
                                                         ['attraction', 'url', 'summary', 'image']].copy()
        random_location_2 = random_location.copy()
        while random_location_2['attraction'] == random_location['attraction']:
            random_location_2 = recommendations.sample(1)
        random_location = random_location_2.copy()

    def dont_proceed_recommendations():
        random_location_2 = random_location.copy()
        while random_location_2['attraction'] == random_location['attraction']:
            random_location_2 = recommendations.sample(1)
        random_location = random_location_2.copy()
        img_src = StringProperty(random_location)

    def update_random_image():
        random_location_2 = random_location.copy()
        while random_location_2['attraction'] == random_location['attraction']:
            random_location_2 = recommendations.sample(1)
        random_location = random_location_2.copy()
        img_src = StringProperty(random_location['image'].values[0])


if __name__ == '__main__':
    SwitchingScreenApp().run()
