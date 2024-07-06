"""
Train the model with the training dataset.

Author: Daniel H Choi
"""

from params import *
from dataset import *
from modules import *
import torch
import matplotlib.pyplot as plt
import time

optimizer = torch.optim.Adam(lr=learning_rate, betas=betas, 
                             weight_decay=weight_decay, amsgrad=amsgrad)

criterion = torch.nn.CrossEntropyLoss()

model = TextClassifier()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = model.to(device)

model.train()
total_acc, total_count = 0, 0

dataloader = generate_train_dataloader

for epoch in range(1, epochs + 1):
    for idx, (label, text, offsets) in enumerate(dataloader):
        optimizer.zero_grad()
        predicted_label = model(text, offsets)
        loss = criterion(predicted_label, label)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 0.1)
        optimizer.step()
        total_acc += (predicted_label.argmax(1) == label).sum().item()
        total_count += label.size(0)
        if idx % 100 == 0 and idx > 0:
            elapsed = time.time() - start_time
            print(
                "| epoch {:3d} | {:5d}/{:5d} batches "
                "| accuracy {:8.3f}".format(
                    epoch, idx, len(dataloader), total_acc / total_count
                )
            )
            total_acc, total_count = 0, 0
            start_time = time.time()