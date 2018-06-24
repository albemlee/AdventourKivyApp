from flask import Flask, abort, jsonify, request


import json
import urllib3
from bs4 import BeautifulSoup
import csv
import wikipedia
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import stop_words

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

app = Flask(app)

@app.route('/api', methods=['GET', 'POST'])
def create_rec():
    data = request.json['summary']

    cluster_model = train_model(recommendations)

    recommendations_w_clusters = recommendations.copy()
    recommendations_w_clusters['cluster'] = cluster_model.predict(recommendations['summary'])

    recommended_cluster = cluster_model.predict(data)

    recommendations = recommendations_w_clusters.loc[recommendations_w_clusters['cluster'] == recommended_cluster, ['attraction', 'url', 'summary', 'image']].copy()

    return(recommendations.to_json())


if __name__ == '__main__':
    app.run(port = 9000, debug=True)
