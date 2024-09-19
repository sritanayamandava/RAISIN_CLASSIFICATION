# Raisin Classification Using Machine Learning

## Project Overview
This project aims to classify different types of raisins based on their physical attributes using machine learning techniques. By analyzing features such as area, perimeter, axis lengths, and more, a classification model is built to assist in automating the quality control process in the agricultural industry.

## Project Workflow
1. **Data Collection**: A dataset containing various physical attributes of raisins is collected.
2. **Data Preprocessing**: The dataset is cleaned and normalized, handling missing values and preparing the data for model training.
3. **Model Training**: A machine learning classification model is developed and trained using algorithms like Random Forest and Logistic Regression.
4. **Model Evaluation**: The model is evaluated using metrics such as accuracy and F1 Score to ensure its reliability and effectiveness.
5. **Deployment**: A Flask web application is created to allow users to input raisin features and receive predictions.

## Features
- **Dataset**: Raisin physical attributes, including area, perimeter, major axis, minor axis, eccentricity, convex area, and extent.
- **Model**: Machine learning algorithms like Random Forest and Logistic Regression.
- **Web Application**: A Flask-based app that provides an easy interface for classifying raisins.

## Directory Structure
```bash
raisin_classification/
│
├── app.py               # Flask application
├── model/
│   ├── raisin_classification_model.pkl  # Trained model
│   └── raisin_scaler.pkl                # Data scaler
├── templates/
│   └── index.html       # HTML file for the web interface
├── static/
│   └── style.css        # CSS file for styling the web app
├── dataset/
│   └── raisin_dataset.csv # Raisin dataset used for training
├── README.md            # Project documentation
└── requirements.txt     # Required Python packages
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/raisin_classification.git
2. Navigate to the Project Directory
bash
Copy code
cd raisin_classification
3. Install Dependencies
Make sure you have Python installed. Then, install the required packages:

bash
Copy code
pip install -r requirements.txt
4. Run the Flask Application
bash
Copy code
python app.py
Navigate to http://127.0.0.1:5000/ in your browser to use the app.

Usage
Input the physical attributes of the raisin (e.g., area, perimeter, axis lengths) through the web interface.
Click on the "Predict" button to classify the raisin type.
The model will output the predicted raisin class.
Model Evaluation
Accuracy: 94%
F1 Score: 89%
These metrics indicate a reliable and effective model for classifying raisins based on the provided dataset.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Your Name - yourusername
Acknowledgements
Thanks to the raisin dataset contributors for providing the data used in this project.
