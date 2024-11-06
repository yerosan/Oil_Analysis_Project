import React, { useEffect, useState } from 'react';
import Dashboard from './components/Dashboard';
import { fetchMetrics, fetchPredictions } from './services/api';
import './App.css';
import Prediction_Charts from './components/Chart';
function App() {
    const [metrics, setMetrics] = useState({});
    const [predictions, setPredictions] = useState({});

    useEffect(() => {
        async function fetchData() {
            const metricsData = await fetchMetrics();
            const predictionData = await fetchPredictions();
            setMetrics(metricsData);
            setPredictions(predictionData);
        }
        fetchData();
    }, []);

    return (
        <div className="App">
            <h1>Brent Oil Price Dashboard</h1>
            <Dashboard metrics={metrics} predictions={predictions} />
        </div>
    );
}

export default App;
