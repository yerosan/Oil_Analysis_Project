# src/feature_engineering.py

import pandas as pd

class FeatureEngineer:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the FeatureEngineer with a preprocessed dataset.

        Args:
            data (pd.DataFrame): Input data frame on which to perform feature engineering.
        """
        self.data = data

    def add_lagged_features(self, column: str = 'Price', lags: int = 5) -> pd.DataFrame:
        """Adds lagged versions of the specified column to capture temporal dependencies."""
        for lag in range(1, lags + 1):
            self.data[f'{column}_lag_{lag}'] = self.data[column].shift(lag)
        print(f"{lags} lagged features added for {column}.")
        return self.data

    def add_rolling_statistics(self, column: str = 'Price', window: int = 5) -> pd.DataFrame:
        """Adds rolling mean and standard deviation features for a specified window size."""
        self.data[f'{column}_rolling_mean_{window}'] = self.data[column].rolling(window=window).mean()
        self.data[f'{column}_rolling_std_{window}'] = self.data[column].rolling(window=window).std()
        print(f"Rolling mean and standard deviation added with a window of {window}.")
        return self.data

    def add_date_features(self) -> pd.DataFrame:
        """Extracts date-related features such as month and day of the week."""
        self.data['month'] = self.data.index.month
        self.data['day_of_week'] = self.data.index.dayofweek
        print("Date-based features added (month, day_of_week).")
        return self.data

    def engineer_features(self) -> pd.DataFrame:
        """Runs the complete feature engineering pipeline."""
        self.add_lagged_features()
        self.add_rolling_statistics()
        self.add_date_features()
        print("Feature engineering complete.")
        return self.data
