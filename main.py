import os
from numpy import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sample_files = [doc for doc in os.listdir('sample') if doc.endswith('.txt')]
sample_contents = [open(File).read() for File in sample_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(sample_contents)
s_vectors = list(zip(sample_files, vectors))

def check_plagiarism():
    plagiarism_results = set()
    for Title1, Text1 in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((Title1, Text1))
        del new_vectors[current_index]
        for Title2, Text2 in new_vectors:
            sim_score = similarity(Text1, Text2)[0][1]
            if sim_score > 0.75:
                plagiarism_results.add((Title1, Title2))
    return plagiarism_results

for Title1, Title2 in check_plagiarism():
    print(f'{Title1} is similar to {Title2}')
    