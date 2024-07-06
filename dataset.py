"""
Generate datasets for training, testing and validation

Author: Daniel H Choi
"""

from params import *
from torch.utils.data import DataLoader, random_split
from sklearn.feature_extraction import TfidfVectorizer

def generate_train_dataloader():

    return DataLoader()

def generate_validation_dataloader():

    return DataLoader()

def generate_test_dataloader():

    return DataLoader()

# compute TF-IDF
corpus = []
vectorizer = TfidfVectorizer()
result = vectorizer.fit_transform(corpus)

idf_dict = {}
for string, idf in zip(vectorizer.get_feature_names(), vectorizer.idf_):
    idf_dict[string] = idf