import torch
import torchvision.transforms as transforms
from PIL import Image
from model.full_net import Net


class USEFCNN:

    @staticmethod
    def use_fcnn(path):
        # Load the trained model
        model = Net()
        model.load_state_dict(torch.load('model/model.pth'))
        model.eval()

        # Define the transformation for the input image
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

        # Load and preprocess the single image
        image_path = path  # Replace with the actual path to your image
        image = Image.open(image_path).convert('RGB')
        image = transform(image).unsqueeze(0)

        # Make prediction on the image
        with torch.no_grad():
            outputs = model(image)
            _, predicted = torch.max(outputs, 1)

        # Decode the predicted class label
        labels = ['organic', 'recoverable']  # Replace with your actual class labels
        predicted_class = labels[predicted.item()]

        # Print the predicted class
        print('Predicted class:', predicted_class)
        return predicted_class
