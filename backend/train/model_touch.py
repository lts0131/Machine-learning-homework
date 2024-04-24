import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
from model.full_net import Net

# Load the training file and test file
data_dir_train = '/Users/lts/Documents/assignment/Data Analytics and Machine Learning/Assignment 3/DATASET/TRAIN'  # 数据集文件夹路径
data_dir_test = '/Users/lts/Documents/assignment/Data Analytics and Machine Learning/Assignment 3/DATASET/TEST'  # 数据集文件夹路径

# Graphic processing
transform = transforms.Compose([
    # Adjust the input image to the specified size (224x224 pixels)
    transforms.Resize((224, 224)),
    # Converts an image to a Tensor data type.
    transforms.ToTensor(),
    # Standardize images
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Create test and training sets
train_dataset = datasets.ImageFolder(root=data_dir_train, transform=transform)
test_loader = datasets.ImageFolder(root=data_dir_test, transform=transform)
# Training loading
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
# Load the model
model = Net()
# An example of cross-entropy loss function is created
criterion = nn.CrossEntropyLoss()
# A random gradient drop has been created.
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9, weight_decay=0.001)
# The number of iterations of the training cycle is defined.
num_epochs = 10
# Use the GPU for mac m1
device = torch.device("mps")
model.to(device)

for epoch in range(num_epochs):
    running_loss = 0.0
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        if (i + 1) % 200 == 0:
            print(
                f'Epoch [{epoch + 1}/{num_epochs}], Step [{i + 1}/{len(train_loader)}], Loss: {running_loss / 200:.4f}')
            running_loss = 0.0

model.eval()
# Disables gradient calculation, useful during evaluation

with torch.no_grad():
    # Initialize variables to keep track of correct and total predictions
    correct = 0
    total = 0

    # Iterate over the data in the train_loader
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)

        # Forward pass: compute model predictions
        outputs = model(images)

        # Get the predicted classes by finding the maximum value along dimension 1
        _, predicted = torch.max(outputs.data, 1)

        # Update the total count by adding the number of labels in the current batch
        total += labels.size(0)

        # Update the correct count by adding the number of correctly predicted samples in the current batch
        correct += (predicted == labels).sum().item()

    # Print the test accuracy
    accuracy = correct / total
    print(f'Test Accuracy: {accuracy:.4f}')

# Save the model's state dictionary to a file named 'model.pth' in the '../model' directory
torch.save(model.state_dict(), '../model/model.pth')
