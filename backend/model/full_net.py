import torch.nn as nn


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        # Define the fully connected layers and activation function
        self.fc1 = nn.Linear(224 * 224 * 3, 512)  # Input size: 224x224x3, Output size: 512
        self.fc2 = nn.Linear(512, 256)  # Input size: 512, Output size: 256
        self.fc3 = nn.Linear(256, 10)  # Input size: 256, Output size: 10
        self.relu = nn.ReLU()

    def forward(self, x):
        # Reshape the input tensor to a 1D vector
        x = x.view(x.size(0), -1)

        # Perform forward pass through the network layers
        x = self.relu(self.fc1(x))  # Apply ReLU activation to the first fully connected layer
        x = self.relu(self.fc2(x))  # Apply ReLU activation to the second fully connected layer
        x = self.fc3(x)  # Output layer

        return x
