from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

class TimeSeriesVisualizer:
    def __init__(self, date_column: str = 'Date', price_column: str = 'Price'):
        """
        Initializes the TimeSeriesVisualizer.

        Args:
            date_column (str): Name of the date column in the DataFrame.
            price_column (str): Name of the price column in the DataFrame.
        """
        self.date_column = date_column
        self.price_column = price_column

        # return self.date_column,self.price_column

    def _prepare_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Converts the date column to datetime format and sets it as the index.

        Args:
            df (pd.DataFrame): The DataFrame containing the time series data.

        Returns:
            pd.DataFrame: The prepared DataFrame with the date set as index.
        """
        if self.date_column in df.columns:
            df[self.date_column] = pd.to_datetime(df[self.date_column], errors='coerce')
            df.set_index(self.date_column)
        elif not pd.api.types.is_datetime64_any_dtype(df.index):
            df.index = pd.to_datetime(df.index, errors='coerce')
        
        # Drop rows with non-datetime index values
        df = df[~df.index.isnull()]
        df = df.copy()
        df[self.date_column] = pd.to_datetime(df[self.date_column], errors='coerce')
        df.set_index(self.date_column)
        df.dropna(subset=[self.price_column], inplace=True)
        return df

    def plot_time_series(self, df: pd.DataFrame):
        """
        Plots the time series data.

        Args:
            df (pd.DataFrame): The DataFrame containing the time series data.
        """
        df = self._prepare_data(df)
        
        plt.figure(figsize=(10, 6))
        plt.plot(df[self.price_column], label=self.price_column, color='blue')
        plt.title("Brent Oil Prices Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.show()
        



    def decompose_time_series(self, df: pd.DataFrame, frequency: int = 12):
        """
        Decomposes the time series data into trend, seasonal, and residual components.
        
        Args:
            df (pd.DataFrame): The DataFrame containing the time series data.
            frequency (int, optional): The seasonal period to use in the decomposition.
        """
        # Prepare data and ensure it's at a daily frequency for decomposition
        df = self._prepare_data(df).asfreq('D')  # Adjust frequency to your data
        
        # Forward-fill remaining missing values for decomposition to work properly
        if df[self.price_column].isnull().any():
            df[self.price_column] = df[self.price_column].fillna(method='ffill')
        
        try:
            decomposition = sm.tsa.seasonal_decompose(df[self.price_column], model='additive', period=frequency)
            fig = decomposition.plot()
            fig.set_size_inches(14, 10)
            plt.suptitle('Time Series Decomposition', fontsize=16)
            plt.show()
        except ValueError as e:
            # logging.error("Decomposition failed: " + str(e))
            print("Decomposition cannot proceed due to missing values or frequency issues.")

    

    def visualize_time_series(self, df: pd.DataFrame, seasonal_period: Optional[int] = 365, acf_lags: Optional[int] = 365):
        """
        Creates a comprehensive visualization of the time series, including raw data, decomposition, and autocorrelation.

        Args:
            df (pd.DataFrame): The DataFrame containing the time series data.
            seasonal_period (int, optional): Period for seasonal decomposition.
            acf_lags (int, optional): Number of lags for autocorrelation plot.
        """
        df = self._prepare_data(df)

        plt.figure(figsize=(14, 10))

        # Plot the raw time series data
        plt.subplot(3, 1, 1)
        plt.plot(df[self.price_column], label=self.price_column, color='blue')
        plt.title("Brent Oil Prices Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)

        # Seasonal decomposition
        plt.subplot(3, 1, 2)
        decomposition = sm.tsa.seasonal_decompose(df[self.price_column], model='additive', period=seasonal_period)
        decomposition.plot()
        plt.title("Seasonal Decomposition")
        
        # Autocorrelation plot
        plt.subplot(3, 1, 3)
        sm.graphics.tsa.plot_acf(df[self.price_column], lags=acf_lags, ax=plt.gca())
        plt.title("Autocorrelation Plot")
        
        plt.tight_layout()
        plt.show()