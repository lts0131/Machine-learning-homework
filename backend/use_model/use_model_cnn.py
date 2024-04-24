import cv2
import numpy as np
from tensorflow.keras.models import load_model


class USECNN:
    @staticmethod
    def use_cnn(path):
        # Load the trained model
        model = load_model('model/cnn_model.h5')

        # Load and preprocess the single image
        image_path = path  # Replace with the actual path to your image
        image = cv2.imread(image_path)
        image_resized = cv2.resize(image, (100, 100))
        x = np.array([image_resized])
        x = x.astype('float32') / 255

        # Make predictions on the image
        predictions = model.predict(x)
        class_indices = np.argmax(predictions, axis=1)

        # Decode the predicted class label
        labels = ['organic', 'recoverable']  # Replace with your actual class labels
        predicted_classes = [labels[i] for i in class_indices]

        # Print the predicted class
        print('Predicted class:', str(predicted_classes[0]))
        return predicted_classes[0]
