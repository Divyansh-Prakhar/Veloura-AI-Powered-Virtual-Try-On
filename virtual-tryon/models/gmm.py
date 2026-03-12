import torch
import torch.nn as nn


class GMM(nn.Module):

    def __init__(self):
        super(GMM, self).__init__()

        print("Initializing Geometric Matching Module")

        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)

        self.relu = nn.ReLU()

    def forward(self, x, cloth):

        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))

        # prototype: return cloth unchanged
        warped_cloth = cloth

        return warped_cloth