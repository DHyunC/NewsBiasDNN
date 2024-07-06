"""
Generate datasets for training, testing and validation

Author: Daniel H Choi
"""

from params import *
from torch.utils.data import DataLoader, random_split
from sklearn.feature_extraction.text import TfidfVectorizer

def generate_train_dataloader():

    return DataLoader()

def generate_validation_dataloader():

    return DataLoader()

def generate_test_dataloader():

    return DataLoader()

# compute TF-IDF
# merge documents into a single corpus
corpus = []
vectorizer = TfidfVectorizer()
result = vectorizer.fit_transform(corpus)

print(result.toarray())