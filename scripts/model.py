import os
from datetime import datetime
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

class LSTMModelling:
    def __init__(self, time_step: int = 60, model_folder: str = 'models'):
        """
        Initializes the LSTMModelling class with default time_step and model_folder.
        
        Args:
            time_step (int): The number of previous time steps to consider in each training example.
            model_folder (str): The directory where models will be saved.
        """
        self.time_step = time_step
        self.model_folder = model_folder

    def _scale_data(self, train_data: pd.Series, test_data: pd.Series) -> tuple:
        """
        Scales the training and testing data to a range between 0 and 1.

        Args:
            train_data (pd.Series): Training data.
            test_data (pd.Series): Testing data.

        Returns:
            tuple: Scaled training data, scaled testing data, and the scaler object.
        """
        scaler = MinMaxScaler(feature_range=(0, 1))
        train_scaled = scaler.fit_transform(train_data.values.reshape(-1, 1))
        test_scaled = scaler.transform(test_data.values.reshape(-1, 1))
        return train_scaled, test_scaled, scaler

    def _create_dataset(self, data: np.ndarray) -> tuple:
        """
        Prepares data for LSTM with the specified time steps.

        Args:
            data (np.ndarray): Scaled data.

        Returns:
            tuple: Features (X) and targets (Y) for the LSTM model.
        """
        X, Y = [], []
        for i in range(len(data) - self.time_step - 1):
            X.append(data[i:(i + self.time_step), 0])
            Y.append(data[i + self.time_step, 0])
        return np.array(X), np.array(Y)

    def _build_lstm_model(self, input_shape: tuple) -> Sequential:
        """
        Builds and compiles an LSTM model.

        Args:
            input_shape (tuple): The shape of the input data.

        Returns:
            Sequential: The compiled LSTM model.
        """
        model = Sequential([
            LSTM(units=50, return_sequences=True, input_shape=input_shape),
            Dropout(0.2),
            LSTM(units=50),
            Dropout(0.2),
            Dense(units=1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def train_lstm(self, data: pd.DataFrame, model_name: str) -> tuple:
        """
        Trains an LSTM model on the provided data and saves it with a timestamped filename.

        Args:
            data (pd.DataFrame): DataFrame containing 'Date' and 'Price' columns.
            model_name (str): Base name for the saved model file.

        Returns:
            tuple: Original test data, true values (y_test), and predictions (test_predict).
        """
        data = data[['Date', 'Price']].copy()
        data['Price'] = data['Price'].astype(float)
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        
        train_size = int(len(data) * 0.8)
        train_data, test_data = data['Price'][:train_size], data['Price'][train_size:]
        
        train_scaled, test_scaled, scaler = self._scale_data(train_data, test_data)
        X_train, y_train = self._create_dataset(train_scaled)
        X_test, y_test = self._create_dataset(test_scaled)
        
        # Reshape for LSTM input
        X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
        X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
        
        # Build and train model
        model = self._build_lstm_model(input_shape=(X_train.shape[1], 1))
        history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test), verbose=1)
        
        # Predictions
        train_predict = scaler.inverse_transform(model.predict(X_train))
        test_predict = scaler.inverse_transform(model.predict(X_test))
        y_train = scaler.inverse_transform(y_train.reshape(-1, 1))
        y_test = scaler.inverse_transform(y_test.reshape(-1, 1))

        # Save the model
        self._save_model(model, model_name)

        return test_data, y_test, test_predict

    def _save_model(self, model: Sequential, model_name: str):
        """
        Saves the trained model with a timestamped filename.

        Args:
            model (Sequential): The trained model.
            model_name (str): Base name for the saved model file.
        """
        os.makedirs(self.model_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        filename = os.path.join(self.model_folder, f"{model_name}-{timestamp}.pkl")
        
        with open(filename, 'wb') as file:
            pickle.dump(model, file)
        
        print(f"Model saved as {filename}")

    def evaluate_model(self, y_true: np.ndarray, y_pred: np.ndarray) -> dict:
        """
        Evaluates the LSTM model's performance using various metrics.

        Args:
            y_true (np.ndarray): True values.
            y_pred (np.ndarray): Predicted values.

        Returns:
            dict: Evaluation metrics.
        """
        metrics = {
            'MAE': mean_absolute_error(y_true, y_pred),
            'MSE': mean_squared_error(y_true, y_pred),
            'RMSE': np.sqrt(mean_squared_error(y_true, y_pred)),
            'R2 Score': r2_score(y_true, y_pred),
            'MAPE': mean_absolute_percentage_error(y_true, y_pred)
        }
        
        # Print metrics
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")
        
        return metrics

    def plot_results(self, y_test: np.ndarray, y_pred: np.ndarray):
        """
        Plots the actual vs. predicted prices.

        Args:
            y_test (np.ndarray): True values.
            y_pred (np.ndarray): Predicted values.
        """
        plt.figure(figsize=(14, 5))
        plt.plot(y_test, label="Original Price")
        plt.plot(y_pred, label="Predicted Price")
        plt.title('LSTM Model Brent Oil Price Prediction')
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.legend()
        plt.show()
