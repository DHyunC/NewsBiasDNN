"""
Hyper parameter for the NLP classifier and training
"""

batch_size = 64
epochs = 100
learning_rate = 0.0001
weight_decay = 0
betas = (0.9, 0.999)
amsgrad = False

classes = {1: "left", 2: "right"}

data_path = ""
train_test_ratio = 0.3