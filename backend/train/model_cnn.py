import os
from pathlib import Path
import numpy as np
from sklearn.preprocessing import LabelEncoder
import cv2
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from keras import models, layers

gpu = len(tf.config.list_physical_devices('GPU')) > 0
print("GPU is", "available" if gpu else "NOT AVAILABLE")

labels = os.listdir(
    '/Users/lts/Documents/assignment/Data Analytics and Machine Learning/Assignment 3/DATASET/TRAIN')
path = Path('/Users/lts/Documents/assignment/Data Analytics and Machine Learning/Assignment 3/DATASET/TRAIN')

x_data = []
y_data = []

for label in labels:
    path = '/Users/lts/Documents/assignment/Data Analytics and Machine Learning/Assignment 3/DATASET/TRAIN/{0}/'.format(
        label)
    folder_data = os.listdir(path)
    for image_path in folder_data:
        image = cv2.imread(path + image_path)
        image_resized = cv2.resize(image, (100, 100))
        x_data.append(np.array(image_resized))
        y_data.append(label)

x_data = np.array(x_data)
y_data = np.array(y_data)
# Pixel value normalization
x_data = x_data.astype('float32') / 255
# Label the value of y
y_encoded = LabelEncoder().fit_transform(y_data)
y_categorical = to_categorical(y_encoded)
# shuffle data
r = np.arange(x_data.shape[0])
np.random.seed(42)
np.random.shuffle(r)

X = x_data[r]
Y = y_categorical[r]

# Convolutional Neural Networks
# build Sequential model
cnn_model = models.Sequential()
# A Conv2D layer was added, using 32 convolution kernels of size 5x5 for convolution and a ReLU activation function for activation.
# The shape of the input tensor is X_train.shape[1:], i.e. a dimension other than the number of samples.
cnn_model.add(layers.Conv2D(filters=32, kernel_size=(5, 5), activation='relu', input_shape=X.shape[1:]))
# Add a MaxPool2D layer to downsample the input tensor using a 2x2 pooling window.
cnn_model.add(layers.MaxPool2D(pool_size=(2, 2)))
# Add another Conv2D layer with 64 convolution kernels of size 3x3 for convolution operations and use the ReLU activation function for activation.
cnn_model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
# Added MaxPool2D layer to downsample the input tensor using a 2x2 pooling window.
cnn_model.add(layers.MaxPool2D(pool_size=(2, 2)))
# A Dropout layer has been added to prevent overfitting using a random deactivation technique.
cnn_model.add(layers.Dropout(rate=0.25))
# A Flatten layer has been added to flatten the input tensor into a one-dimensional vector.
cnn_model.add(layers.Flatten())
# A fully connected layer containing 256 neurons was added and activated using the ReLU activation function.
cnn_model.add(layers.Dense(256, activation='relu'))
# Add a Dropout layer to prevent over-fitting
cnn_model.add(layers.Dropout(rate=0.5))
# Added a fully connected layer with two outputs, using the Sigmoid activation function for activation
cnn_model.add(layers.Dense(2, activation='sigmoid'))
# Specify loss functions, optimisers and evaluation metrics.
cnn_model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])
# Fit method for training models
history = cnn_model.fit(X, Y, epochs=20, validation_split=0.2)

# save model
tf.keras.models.save_model(cnn_model, "../model/cnn_model.h5")
