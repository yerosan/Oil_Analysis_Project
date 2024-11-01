import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, file_path: str, missing_value_method: str = 'ffill'):
        """
        Initializes the DataPreprocessor with the dataset file path and preferred missing value handling method.

        Args:
            file_path (str): Path to the dataset CSV file.
            missing_value_method (str): Method for handling missing values; 'ffill', 'bfill', or 'drop'.
        """
        self.file_path = file_path
        self.missing_value_method = missing_value_method
        self.data = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        """Loads data from the specified CSV file path."""
        try:
            data = pd.read_csv(self.file_path, parse_dates=['Date'], index_col='Date')
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def handle_missing_values(self) -> pd.DataFrame:
        """Handles missing values in the dataset based on the specified method."""
        if self.missing_value_method == 'ffill':
            self.data = self.data.ffill()  
        elif self.missing_value_method == 'bfill':
            self.data = self.data.bfill() 
        elif self.missing_value_method == 'drop':
            self.data = self.data.dropna()
        else:
            raise ValueError("Method should be 'ffill', 'bfill', or 'drop'.")
        
        print("Missing values handled.")
        return self.data

    def remove_outliers(self) -> pd.DataFrame:
        """Removes outliers based on a Z-score threshold."""
        self.data = self.data[(np.abs(self.data - self.data.mean()) / self.data.std()) < 3]
        print("Outliers removed.")
        return self.data

    def preprocess(self) -> pd.DataFrame:
        """Complete preprocessing pipeline including loading, cleaning, and handling missing values."""
        self.handle_missing_values()
        self.remove_outliers()
        print("Data preprocessing complete.")
        return self.data
