from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("risk.csv")


@app.post("/predict")
def predict(index: int):

    if index >= len(df):
        return {"error": "index out of range"}

    row = df.iloc[index]

    risk = int(row["risk"])

    anomaly = False
    alert = "Normal"

    if risk > 2:
        anomaly = True
        alert = "PATIENT DISTRESS — SEND ALERT TO AMBULANCE"

    return {
        "hr": float(row["hr"]),
        "spo2": float(row["spo2"]),
        "risk": risk,
        "anomaly": anomaly,
        "alert": alert
    }