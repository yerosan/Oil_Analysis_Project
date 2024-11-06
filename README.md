# Brent Oil Prices Analysis Project

This project aims to analyze and forecast oil prices using a robust data science workflow. I am utilizing both traditional time series analysis techniques and advanced machine learning methods to explore patterns, trends, and factors influencing oil prices. The project is structured for modularity, enabling easy extension to additional datasets or variables.

## Project Structure

Here is a brief overview of the current folder structure:


## Project Progress

The project is currently in the data preprocessing and feature engineering stages. Below is an overview of the completed work and ongoing tasks in these areas.

### 1. Data Preprocessing

The `data_preprocessing.py` module handles the following tasks:

- **Data Loading**: Reads data from CSV files, with date parsing and handling of various date formats.
- **Missing Value Handling**: Provides options to forward-fill, backward-fill, or drop missing values.
- **Outlier Removal**: Identifies and removes outliers using a Z-score threshold.

**Usage**: The `DataPreprocessor` class in `data_preprocessing.py` is designed in an object-oriented manner, making it easy to preprocess different datasets consistently.

### 2. Feature Engineering

The `feature_engineering.py` module is currently under development. This module will:

- **Create Features**: Generate meaningful features from raw data, such as moving averages, rolling statistics, and volatility measures.
- **Transform Data**: Prepare the data for advanced time series models and machine learning algorithms.

**Usage**: Once complete, the `FeatureEngineer` class in `feature_engineering.py` will provide utilities for easy feature creation and transformation.

**Progress**: Basic setup is complete, and feature engineering functions are being implemented.

## Setup and Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository_url>
cd <repository_folder>
pip install -r requirements.txt
```
### Running the Code
You can test the data preprocessing functionalities by running the script in the scripts folder:

```bash
python scripts/data_preprocessing.py
```




# Brent Oil Price Prediction Dashboard

This project aims to forecast Brent oil prices using Long Short-Term Memory (LSTM) neural networks, complemented by a comprehensive Exploratory Data Analysis (EDA) of historical data. The final result is an interactive dashboard, enabling stakeholders to explore trends, understand volatility, and analyze the impact of global events on oil prices.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Data and Methodology](#data-and-methodology)
- [Model Performance](#model-performance)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Insights and Recommendations](#insights-and-recommendations)
- [Contributions](#contributions)
- [License](#license)

## Project Overview
The Brent Oil Price Prediction Dashboard leverages LSTM models to forecast oil prices accurately and supports decision-making by analyzing historical price trends. By combining machine learning with time series analysis, the project offers insights into market dynamics and price drivers, making it a valuable tool for energy market analysts and financial stakeholders.

## Features
- **Time Series Analysis**: EDA to uncover trends, seasonality, and volatility in historical Brent oil prices.
- **LSTM Prediction Model**: A robust LSTM model trained on historical data to predict future prices with high accuracy.
- **Interactive Dashboard**: Built using Flask (backend) and React (frontend) with dynamic visualizations.
  - Historical trend exploration with filters and zoom.
  - Event highlighting to show price spikes/drops during key events.
  - Real-time performance metrics (e.g., RMSE, MAE).
- **Insights into Volatility**: Analysis of high-risk periods for better risk management.

## Data and Methodology
- **Data Source**: Historical Brent oil prices, spanning multiple years.
- **EDA Techniques**: Rolling averages, volatility analysis, and event correlation.
- **Model Architecture**: Long Short-Term Memory (LSTM) neural network trained on an 80-20 train-test split.
- **Performance Metrics**:
  - Mean Absolute Error (MAE): 2.007
  - Root Mean Squared Error (RMSE): 2.911
  - R² Score: 0.98

## Model Performance
The LSTM model demonstrated strong predictive performance, with an R² score of 0.98, indicating that it captures price trends accurately. The model performs particularly well in stable periods but may require additional features or hybrid models for volatile periods.

## Installation and Setup

### Prerequisites
- Python 3.7+
- Node.js and npm
- Flask, Pandas, Numpy, TensorFlow (for LSTM model)
- React (for frontend)

### Steps
Clone the repository:
```bash
git clone https://github.com/yourusername/brent-oil-price-prediction.git
cd brent-oil-price-prediction
```
Install Python dependencies:

```bash
pip install -r requirements.txt
```

Set up frontend:

```bash
Copy code
cd oil-price-dashboard
npm install
npm start
```

Set up frontend:

```bash
Copy code
cd oil-price-dashboard
npm install
npm start
```
Start Flask backend:

```bash
Copy code
python app.py
```

### Project Structure
```bash
.
├── .github/
│   └── workflows/
│       └── unittests.yml             # CI workflow for running unit tests
├── .vscode/
│   └── settings.json                 # VSCode configuration settings
├── Data/                             # Folder for storing raw and processed data files
├── notebooks/
│   ├── __init__.py
│   └── Preprocessing.ipynb           # Jupyter notebook for initial data exploration, preprocessing, model building and training
├── scripts/
│   ├── __init__.py
│   ├── data_preprocessing.py         # Module for data loading and preprocessing functions
│   └── feature_engineering.py        # Module for creating and extracting features from the data
    └── model.py                  # Model and training scripts LSTM training code
├── src/
    ├── app.py                  # Flask backend application
│   └── __init__.py                   # Core package for project-specific modules
├── tests/
│   └── __init__.py                   # Placeholder for unit tests
├── oil-price-dashboard/    # React frontend application
│   ├── public/
│   ├── src/
│       ├── components/     # UI components (Dashboard, Graphs, etc.)
│       ├── services/       # API interaction
│       ├── App.js
│       └── index.js
├── .gitignore                        # Specifies files and folders to ignore in version control
├── README.md                         # Project overview and documentation
└── requirements.txt                  # List of dependencies for the project
```
## Usage

- **View Dashboard**: Open [http://localhost:3000](http://localhost:3000) in your browser to access the React frontend.
- **Explore Predictions**: Use the dashboard to navigate historical trends, explore LSTM predictions, and analyze volatility and event impacts.
- **API Access**: The Flask backend provides endpoints for accessing model data and performance metrics, allowing for integration with other applications.

## Insights and Recommendations

- **Predictive Accuracy**: The model provides reliable medium-term forecasts, especially useful in stable market conditions.
- **Impact of Volatility**: The model shows a slight lag during high-volatility events; incorporating additional economic indicators could improve accuracy.
- **Event Analysis**: The dashboard's event allow to understand how specific events (e.g., conflicts, policy changes) influence prices.
