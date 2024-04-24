import torch
from model.full_net import Net
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


class AccuracyFCNN:
    def fcnn_accuracy(self):
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

        test_loader = datasets.ImageFolder(root=data_dir_test, transform=transform)
        test_loader = DataLoader(test_loader, batch_size=32, shuffle=True)

        model = Net()
        model.load_state_dict(torch.load('model/model.pth'))
        device = torch.device("mps")
        model = model.to(device)
        model.eval()

        # Initialize variables for accuracy calculation
        correct = 0
        total = 0

        # Make predictions on the test dataset
        with torch.no_grad():
            for i, (images, labels) in enumerate(test_loader):
                images = images.to(device)  # Move images to GPU if available
                labels = labels.to(device)  # Move labels to GPU if available

                outputs = model(images)
                _, predicted = torch.max(outputs.data, 1)

                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        # Calculate accuracy
        accuracy = 100 * correct / total
        print('Accuracy: {:.2f}%'.format(round(accuracy, 2)))
        return round(accuracy, 2)
