# Smart Ambulance Monitoring Assignment

This project simulates patient vital signals for a smart ambulance system.

Steps:
- Generated 30 min time-series data
- Removed sensor artifacts
- Detected anomalies
- Created risk score
- Evaluated alerts
- Built FastAPI service

Run API:

cd api
uvicorn app:app --reload

Open:
http://127.0.0.1:8000/docs