# Heart Disease Prediction System Using Machine Learning

## Overview

The Heart Disease Prediction System is a machine learning project designed to estimate the likelihood of heart disease based on health-related parameters. It uses a dataset sourced from Kaggle and applies data preprocessing, model training, and prediction techniques to explore the role of machine learning in healthcare.

The project includes Jupyter Notebooks for model development and a Python application interface for making predictions.

## Features

- Data exploration and preprocessing
- Machine learning model development
- Prediction based on health-related input parameters
- Saved model for reuse
- Visualization of data and model results
- Streamlit-based application interface

## Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Data Visualization:** Matplotlib, Seaborn
- **Application Framework:** Streamlit
- **Development Environment:** Jupyter Notebook
- **Model Serialization:** Joblib
- **Dataset Source:** Kaggle


## Project Structure

```text
heart-disease-prediction-system/
│
├── README.md
├── model.ipynb
├── heart.xls
├── streamlit_app.py
├── app(1).ipynb
│
└── results/
    ├── .gitkeep
    ├──1_correlation_heatmap.png
    ├── 2_feature_inportance.png
    ├── 3_confusion_matrices.png
    ├── 4_model_comparison.png
    ├── best_heart_model.joblib
    └── model_comparison.csv
```

## Dataset

The dataset used in this project was obtained from Kaggle. It contains health-related attributes used to train and evaluate the machine learning model.

**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)

## How the Project Works

1. **Data Loading:** Load the dataset and inspect its structure.
2. **Data Preprocessing:** Prepare the data for machine learning.
3. **Model Training:** Train a machine learning algorithm using the selected features.
4. **Model Evaluation:** Evaluate the trained model using appropriate performance metrics.
5. **Model Saving:** Save the trained model for future predictions.
6. **Prediction Interface:** Use the Python application to collect inputs and generate predictions.

The exact algorithm and performance metrics should be documented according to the implementation in `model.ipynb`.

## Installation and Setup

### Prerequisites

- Python 3.10 or another version compatible with the project's dependencies
- pip
- Git (optional, for cloning the repository)

### 1. Clone the Repository

```bash
git clone https://github.com/ctrlchaoss/heart-disease-prediction-system.git
cd heart-disease-prediction-system
```

### 2. Install Dependencies

Install the libraries required by the project:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
```

Install any additional libraries imported by your code.

### 3. Run the Application

If `app.py` is a Streamlit application, run:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

## Results

The `results/` directory contains saved model files and visualization outputs generated during model development. These files support the analysis and reuse of the trained model.

## Future Improvements

- Compare different machine learning algorithms.
- Improve performance through hyperparameter tuning.
- Add more detailed evaluation metrics and visualizations.
- Deploy the application for online access.
- Improve input validation and interface usability.

## Disclaimer

This project is intended for educational and research purposes only. Its predictions are not a medical diagnosis and must not replace professional medical advice or clinical evaluation.

## Author

**Bidisha Chakraborty**

GitHub: [ctrlchaoss](https://github.com/ctrlchaoss)
