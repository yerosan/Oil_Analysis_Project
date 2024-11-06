import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import { Chart as ChartJS, CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend } from 'chart.js';
rt
ChartJS.register(CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend);

const Prediction_Charts = () => {
    const [yTest, setYTest] = useState([]);
    const [testPredict, setTestPredict] = useState([]);

    useEffect(() => {
        // Fetch y_test and test_predict from Flask API
        axios.get("http://localhost:5000/get_model_data")
            .then(response => {
                setYTest(response.data.y_test.map(item => item[0])); // Flatten y_test
                setTestPredict(response.data.test_predict.map(item => item[0]));
            })
            .catch(error => console.error("Error fetching model data:", error));
    }, []);

    // Chart data for y_test and test_predict
    const data = {
        labels: Array.from({ length: yTest.length }, (_, i) => i), // Indexes as labels
        datasets: [
            {
                label: "Original Price (y_test)",
                data: yTest,
                borderColor: "#3498db",
                fill: false,
                pointRadius: 5, // Optionally adjust point size
                pointHoverRadius: 7 // Optionally adjust point hover size
            },
            {
                label: "Predicted Price (test_predict)",
                data: testPredict,
                borderColor: "#e74c3c",
                fill: false,
                pointRadius: 5, // Optionally adjust point size
                pointHoverRadius: 7 // Optionally adjust point hover size
            }
        ]
    };

    const options = {
        responsive: true,
        scales: {
            x: { title: { display: true, text: 'Time' } },
            y: { title: { display: true, text: 'Price' } }
        }
    };

    return (
        <div className="chart-container">
            <h2>LSTM Model Brent Oil Price Prediction</h2>
            <Line data={data} options={options} />
        </div>
    );
};

export default Prediction_Charts;
