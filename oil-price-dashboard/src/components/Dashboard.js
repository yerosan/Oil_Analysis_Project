import React from 'react';
// Import any chart library component (e.g., Recharts or Chart.js) here

import Prediction_Charts from './Chart';

function Dashboard({ metrics, predictions }) {
    return (
        <div className="dashboard-container">
            <h2>Model Metrics</h2>
            <div className="metrics-container">
                <div className="metric-card">
                    <p className="metric-title">Mean Absolute Error (MAE)</p>
                    <p className="metric-value">{metrics.MAE}</p>
                </div>
                <div className="metric-card">
                    <p className="metric-title">Mean Squared Error (MSE)</p>
                    <p className="metric-value">{metrics.MSE}</p>
                </div>
                <div className="metric-card">
                    <p className="metric-title">Root Mean Squared Error (RMSE)</p>
                    <p className="metric-value">{metrics.RMSE}</p>
                </div>
                <div className="metric-card">
                    <p className="metric-title">R2 Score</p>
                    <p className="metric-value">{metrics['R2 Score']}</p>
                </div>
                <div className="metric-card">
                    <p className="metric-title">Mean Absolute Percentage Error (MAPE)</p>
                    <p className="metric-value">{metrics.MAPE}</p>
                </div>
            </div>

            <div className="chart-container">
                <Prediction_Charts/>
            </div>
        </div>
    );
}

export default Dashboard;
