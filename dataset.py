"""
Generate datasets for training, testing and validation

Author: Daniel H Choi
"""

from params import *
from torch.utils.data import DataLoader, random_split
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# compute TF-IDF
# merge documents into a single corpus
train_data_path = "./train_data"

corpus = []

for file in os.listdir(train_data_path):
    file_path = os.path.join(train_data_path, file)

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            corpus.append(file.read())

vectorizer = TfidfVectorizer()
result = vectorizer.fit_transform(corpus)

print(result.shape)

print(result.toarray())

def generate_train_dataloader():
    training_data = corpus
    return DataLoader(training_data, batch_size=batch_size, shuffle=False)

def generate_validation_dataloader():

    return DataLoader()

def generate_test_dataloader():

    return DataLoader()

