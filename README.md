# Smart Ambulance Assignment

This project analyzes patient vital data, detects anomalies, classifies risk level, and provides an API using FastAPI.

The project includes data cleaning, anomaly detection, risk classification, plots, and a FastAPI server to display results.

---

## Project Steps

1. Data cleaning using Python (Google Colab)
2. Anomaly detection
3. Risk classification
4. Plot generation
5. FastAPI app to show results

---

## Files in this project

app.py  
requirements.txt  
vitals.csv  
vitals_clean.csv  
anomaly.csv  
risk.csv  
final_output.csv  
spo2_plot.png  
anomaly_plot.png  
README.md  

---

## How to run this project

### Step 1 — Clone repository

```
git clone https://github.com/rithi0508/smart-ambulance-assignment.git
cd smart-ambulance-assignment
```

### Step 2 — Install requirements

```
pip install -r requirements.txt
```

### Step 3 — Run FastAPI server

```
uvicorn app:app --reload
```

### Step 4 — Open in browser

```
http://127.0.0.1:8000/docs
```

You will see the API documentation page.

---

## Output

- Cleaned data
- Anomaly detection
- Risk classification
- Final output CSV
- Plots
- FastAPI endpoint

---
