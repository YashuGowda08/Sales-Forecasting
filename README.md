# Sales Forecasting API

A Machine Learning powered **Sales Forecasting API** built with **FastAPI** and deployed online.
This project predicts future sales based on historical sales data and exposes the prediction through a REST API.

---

## Live API

Example endpoint:

```
https://sales-forecast-api.onrender.com/forecast?months=6
```

This returns the predicted sales for the next **N months**.

---

## Project Overview

Sales forecasting is important for businesses to:

* Plan inventory
* Predict revenue
* Improve supply chain decisions
* Optimize production

This project uses **historical sales data** to generate future sales predictions and exposes the model as an API.

---

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pandas
* Joblib
* Render (deployment)

---

## Project Structure

```
Sales-Forecasting
│
├── app.py                # FastAPI application
├── sales_series.pkl      # Processed sales data
├── requirements.txt      # Python dependencies
├── runtime.txt           # Python version for deployment
└── README.md             # Project documentation
```

---

## ⚙️ Installation (Local Setup)

Clone the repository:

```
git clone https://github.com/YashuGowda08/Sales-Forecasting.git
```

Navigate to the project folder:

```
cd Sales-Forecasting
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the FastAPI server:

```
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## API Endpoints

### Home Endpoint

```
GET /
```

Response:

```json
{
  "message": "Sales Forecast API running"
}
```

---

### Forecast Endpoint

```
GET /forecast?months=6
```

Example response:

```json
{
  "forecast": [5200, 5200, 5200, 5200, 5200, 5200]
}
```

---

## API Documentation

FastAPI automatically generates documentation:

```
/docs
```

Example:

```
https://sales-forecast-api.onrender.com/docs
```

---

## Deployment

The application is deployed using **Render**.

Deployment steps:

1. Push project to GitHub
2. Create a Web Service on Render
3. Connect the GitHub repository
4. Start command:

```
uvicorn app:app --host 0.0.0.0 --port $PORT
```

---

## Free Tier Note

Render free services may sleep after inactivity.
The first request may take **30–60 seconds** to wake the server.

---

## Future Improvements

* Add real ML forecasting models (ARIMA / Prophet)
* Add visualization dashboard
* Allow dataset upload
* Add prediction accuracy evaluation
* Build a web dashboard using Streamlit

---

## Author

**Yashwanth M Gowda**

B.Tech CSE Student
Machine Learning & AI Enthusiast
