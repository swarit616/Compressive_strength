# Compressive Strength Predictor

The Compressive Strength Predictor is an application designed to estimate the compressive strength of a material based on four input parameters: Grade, UPV (Ultrasonic Pulse Velocity), Rebound, and Age.

## Overview

The predictive model utilizes a Random Forest Regressor trained on a dataset, visualized, and tested within the Google Colab environment. Evaluation metrics, such as R2 error scores ranging from 0.63 to 0.83, demonstrate the model's accuracy.

## Model Architecture

The trained model generates two values: "STRENGTH TO" and "STRENGTH FROM". These values are stored in a pickle file, facilitating easy retrieval and utilization within the application.

## Implementation Details

1. **Training Procedure**: The code for model training is encapsulated within the `comp_strength.ipynb` notebook, showcasing the entire training process, including data preprocessing, model fitting, and evaluation.

2. **API Integration**: A Flask API is employed to interface with the trained model. Using the POST method, parameters are passed to the pickle file, and predictions for the two values are generated. The API is rigorously tested using Postman to ensure functionality and reliability.

3. **Deployment**: The Flask API is deployed on an AWS EC2 Linux instance, rendering it accessible via the live server at http://13.232.91.214. This deployment strategy ensures scalability and robustness.

4. **User Interface**: A simple Android application, leveraging Volley libraries, serves as the graphical user interface. Users input parameters via the application, which sends API requests to the Flask server hosted on the EC2 instance. The predicted values are then displayed within the application interface.

## Usage

Detailed documentation and instructions for utilizing the application, including how to input parameters and interpret predicted values, are provided within the repository.

## Future Enhancements

Potential future enhancements include expanding the dataset, refining the model architecture, and improving the user interface for enhanced user experience and functionality.

## Contributions

Contributions to the project, including bug fixes, feature enhancements, and optimizations, are welcome. Please refer to the contribution guidelines outlined in the repository for more information.

## License

This project is licensed under the [MIT License](LICENSE), granting users the freedom to modify, distribute, and utilize the codebase as per their requirements.

