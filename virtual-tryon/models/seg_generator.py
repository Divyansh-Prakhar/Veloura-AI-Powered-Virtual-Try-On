import torch
import torch.nn as nn


class SegGenerator(nn.Module):

    def __init__(self):
        super(SegGenerator, self).__init__()

        print("Initializing Segmentation Generator")

        # simple convolution layers (prototype)
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.conv3 = nn.Conv2d(64, 13, 3, padding=1)

        self.relu = nn.ReLU()

    def forward(self, x):

        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.conv3(x)

        return x