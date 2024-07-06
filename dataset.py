"""
Generate datasets for training, testing and validation

Author: Daniel H Choi
"""

from params import *
from torch.utils.data import DataLoader, random_split
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from torch.utils.data import Dataset
import torch
import numpy as np

# compute TF-IDF
# merge documents into a single corpus
train_data_path = "./train_data"

corpus = []
labels = []

for file in os.listdir(train_data_path):
    file_path = os.path.join(train_data_path, file)

    if os.path.isfile(file_path):
        if file[:3] == 'abc':
            labels.append(1)

        elif file[:3] == 'fox':
            labels.append(2)

        with open(file_path, 'r') as file:
            corpus.append(file.read())

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

tfidf_tensor = torch.tensor(tfidf_matrix.toarray(), dtype=torch.float32)

class NewsTextDataset(Dataset):
    def __init__(self, text, label, tfidf_tensor):
        self.text = text
        self.label = label
        self.tfidf_tensor = tfidf_tensor
        self.vocab = vectorizer.get_feature_names_out()

    def __len__(self):
        return len(self.text)
    
    def __getitem__(self, idx):
        text = self.text[idx]
        label = self.label[idx]
        tfidf_value = self.tfidf_tensor[idx]
        
        # Compute document index and offset index
        document_index = idx
        offset_index = np.arange(len(text.split()))

        return {
            'label': torch.tensor(label, dtype=torch.long),
            'text': text,
            'document_index': torch.tensor(document_index, dtype=torch.long),
            'offset_index': torch.tensor(offset_index, dtype=torch.long),
            'tfidf_value': tfidf_value
        }

news_dataset = NewsTextDataset(corpus, labels, tfidf_tensor)

training_data, validation_data, testing_data = random_split(news_dataset, [0.7,0.1,0.2]) 

def generate_train_dataloader(): 
    return DataLoader(training_data, batch_size=batch_size, shuffle=False)

def generate_validation_dataloader():

    return DataLoader(validation_data, batch_size=batch_size, shuffle=False)

def generate_test_dataloader():

    return DataLoader(testing_data, batch_size=batch_size, shuffle=False)

