import os 
from numpy imporrt vertorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sample_files = [doc for doc in os.listdir('sample') if doc.endswith('.txt')]\