### Project Summary

#### Introduction
Waste management is a significant issue in Malaysia, primarily handled through landfill disposal, leading to environmental contamination and other related problems. This project aims to address waste segregation by developing a system that classifies waste images as organic or recyclable. Python was chosen for its machine learning capabilities, and VUE for front-end development. Two models, CNN and FCNN, were employed for image classification.

#### Dataset Description and Pre-processing
The dataset consists of 22,564 training images and 2,513 test images, classified as organic (O) or recyclable (R). Data normalization was performed to standardize pixel values. Code snippets demonstrate the pre-processing steps using OpenCV and scikit-learn for CNN, and torchvision for FCNN.

#### Web Application Prototype Design
The project is divided into front-end and back-end components. The front-end utilizes Vue.js, while the back-end uses Flask for REST API implementation. TensorFlow and PyTorch are employed for training CNN and FCNN models, respectively. A SQLite database is used for user data storage. Initial project development involved prototyping with Axure and development using NodeJS, Flask, and WebStorm.

##### Features:
- **Login Page**: Essential for system security.
- **Home Page**: Allows uploading and categorizing images, displaying current weather, the day's word, and previous detection results.

#### Architecture Diagram and Explanation
The project architecture involves:
- **Front-end**: Vue.js with element-ui for UI components.
- **Back-end**: Flask for REST API.
- **Models**: TensorFlow (CNN) and PyTorch (FCNN).
- **Database**: SQLite.

##### Technologies:
- **Vue**: JavaScript-based framework for building UI components.
- **Flask**: Lightweight Python web framework for backend development.
- **TensorFlow**: Machine learning framework for building CNN models.
- **PyTorch**: Open-source machine learning framework for building FCNN models.
- **SQLite**: Embedded relational database for storing user data.

#### Model Practical Implementation and Comparisons
**CNN Model**:
- 9-layer model with convolutional, pooling, dropout, and fully connected layers.

**FCNN Model**:
- Three fully connected layers with ReLU activation function.

##### Model Comparison:
- **CNN** is better suited for image and spatial data processing.
- **FCNN** is commonly used for non-spatial and sequential data.
- **CNN** typically has fewer parameters and lower computational complexity.
- **FCNN** is less interpretable compared to CNN due to its fully connected structure.

#### Conclusion and Future Work
The CNN model outperformed the FCNN model in terms of accuracy, likely due to the spatial nature of the image data. Future work includes:
- Enhancing the system with image recognition for real-time classification.
- Increasing the model's accuracy by tweaking CNN algorithm settings.
- Implementing a large data database for storing images for iterative model training.
- Deploying the system to the cloud for scalability and performance improvement.

### Additional Notes
The project prototype was not fully implemented as initially planned, lacking some features like user setup and partial weather display. Future improvements include refining the garbage categorization, adding more garbage classification categories, and packaging the project as a Docker image.

