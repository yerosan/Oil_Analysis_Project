const API_BASE = 'http://localhost:5000/api';

export const fetchPredictions = async () => {
    const response = await fetch(`${API_BASE}/predict`);
    return response.json();
};

export const fetchMetrics = async () => {
    const response = await fetch(`${API_BASE}/metrics`);
    return response.json();
};
