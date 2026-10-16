# Heart Disease Prediction Using Machine Learning

A machine learning project that predicts the likelihood of heart disease based on health-related parameters using a dataset sourced from Kaggle. The project includes data preprocessing, model training, and an interactive Streamlit application.

## Project Overview

Heart disease is one of the major health concerns worldwide. This project explores how machine learning can analyze health data and identify patterns associated with the likelihood of heart disease.

The trained model is integrated into a Streamlit interface to make predictions through a user-friendly application.

## Features

- Data preprocessing and analysis
- Machine learning model training
- Heart disease prediction based on input parameters
- Saved model for reuse
- Interactive Streamlit user interface

## Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Development Environment:** Jupyter Notebook
- **Web Interface:** Streamlit
- **Dataset Source:** Kaggle

## Project Structure

```text
heart-disease-prediction/
│
├── model.ipynb
├── app.py
├── heart.csv

├── README.md
│
└── results/
    └── best_heart_model.joblib
```

## Dataset

The dataset used in this project was obtained from Kaggle and contains health-related features used for heart disease prediction.

**Dataset Link:** [Heart Disease Dataset on Kaggle](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)


## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ctrlchaoss/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

If your Streamlit application is saved as `app.py`, run:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## Model Development

The project follows a machine learning workflow that includes:

1. Loading the Kaggle dataset.
2. Exploring and preprocessing the data.
3. Training a machine learning model.
4. Evaluating model performance.
5. Saving and loading the trained model.
6. Generating predictions through the Streamlit interface.

The specific algorithm and evaluation metrics can be added once confirmed from the training notebook.

## Future Improvements

- Compare multiple machine learning algorithms.
- Improve model performance through hyperparameter tuning.
- Add visualizations and model evaluation metrics.
- Deploy the application online.
- Improve input validation and user experience.

## Disclaimer

This project is intended for educational and research purposes only. Its predictions are not a medical diagnosis and should not replace consultation with a qualified healthcare professional.

## Author

**Bidisha Chakraborty**

Explore the repository to learn more about the implementation, training workflow, and application.
