
import torch
import torch.nn as nn

class ColorClassifier(nn.Module):
    def __init__(self):
        super(ColorClassifier, self).__init__()
        self.fc1 = nn.Linear(3, 16)
        self.fc2 = nn.Linear(16, 32)
        self.fc3 = nn.Linear(32, 10)
        self.fn1 = nn.ReLU()

    def forward(self, x):
        x = self.fn1(self.fc1(x))
        x = self.fn1(self.fc2(x))
        x = self.fc3(x)
        return x
 
