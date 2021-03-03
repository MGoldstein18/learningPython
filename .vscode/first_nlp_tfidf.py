import pandas as pd
import numpy as np
from articles import articles
from preprocessing import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

processed_articles = [preprocess_text(article) for article in articles]

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(processed_articles)

transformer = TfidfTransformer(norm=None)
tfidf_scores_transformed = transformer.fit_transform(counts)

vectorizer = TfidfVectorizer(norm=None)
tfidf_scores = vectorizer.fit_transform(processed_articles)
