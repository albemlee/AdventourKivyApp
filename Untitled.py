import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction import stop_words

base_data = pd.read_csv("base_wiki_data.csv")
detroit_data = pd.read_csv("detroit_wiki_data.csv")

recommendations = detroit_data.copy()
