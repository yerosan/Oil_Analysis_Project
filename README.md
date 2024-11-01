# Brent Oil Prices Analysis Project

This project aims to analyze and forecast oil prices using a robust data science workflow. I am utilizing both traditional time series analysis techniques and advanced machine learning methods to explore patterns, trends, and factors influencing oil prices. The project is structured for modularity, enabling easy extension to additional datasets or variables.

## Project Structure

Here is a brief overview of the current folder structure:

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
│   └── Preprocessing.ipynb           # Jupyter notebook for initial data exploration and preprocessing
├── scripts/
│   ├── __init__.py
│   ├── data_preprocessing.py         # Module for data loading and preprocessing functions
│   └── feature_engineering.py        # Module for creating and extracting features from the data
├── src/
│   └── __init__.py                   # Core package for project-specific modules
├── tests/
│   └── __init__.py                   # Placeholder for unit tests
├── .gitignore                        # Specifies files and folders to ignore in version control
├── README.md                         # Project overview and documentation
└── requirements.txt                  # List of dependencies for the project
```
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
