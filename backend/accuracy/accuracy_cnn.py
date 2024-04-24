from pathlib import Path
import os
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model


class AccuracyCNN():

    def cnn_accuracy(self):
        # Update the file paths and directory structure to match your test dataset
        test_labels = os.listdir(
            '/Users/lts/Documents/assignment/Data Analytics and Machine Learning/Assignment 3/DATASET/TEST')
        test_path = Path(
            '/Users/lts/Documents/assignment/Data Analytics and Machine Learning/Assignment 3/DATASET/TEST')

        x_test_data = []
        y_test_data = []

        for label in test_labels:
            path = '/Users/lts/Documents/assignment/Data Analytics and Machine Learning/Assignment 3/DATASET/TEST/{0}/'.format(
                label)
            folder_data = os.listdir(path)
            for image_path in folder_data:
                image = cv2.imread(path + image_path)
                image_resized = cv2.resize(image, (100, 100))
                x_test_data.append(np.array(image_resized))
                y_test_data.append(label)

        x_test_data = np.array(x_test_data)
        y_test_data = np.array(y_test_data)

        # Normalize pixel values of x_test_data to be in the range [0, 1]
        x_test_data = x_test_data.astype('float32') / 255

        # Encode the test labels using LabelEncoder
        y_test_encoded = LabelEncoder().fit_transform(y_test_data)
        # Convert encoded test labels to one-hot encoded formƒ
        y_test_categorical = to_categorical(y_test_encoded)

        cnn_model = load_model('model/cnn_model.h5')
        test_loss, test_accuracy = cnn_model.evaluate(x_test_data, y_test_categorical)

        # Print the test accuracy
        accuracy = test_accuracy * 100
        print('Accuracy: {:.2f}%'.format(round(accuracy, 2)))
        return round(accuracy, 2)
