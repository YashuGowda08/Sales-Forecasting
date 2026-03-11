from fastapi import FastAPI
import joblib

app = FastAPI()

# load saved sales data
sales_series = joblib.load("sales_series.pkl")

@app.get("/")
def home():
    return {"message": "Sales Forecast API running"}

@app.get("/forecast")
def forecast(months: int = 6):

    last_value = float(sales_series.iloc[-1])

    predictions = [last_value for _ in range(months)]

    return {"forecast": predictions}
