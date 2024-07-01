"""
Train the model with the training dataset.

Author: Daniel H Choi
"""

from params import *
from dataset import *
import torch
import matplotlib.pyplot as plt

optimiser = torch.optim.Adam(lr=learning_rate, betas=betas, 
                             weight_decay=weight_decay, amsgrad=amsgrad)

criterion = torch.nn.CrossEntropyLoss()