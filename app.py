from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/price_model.pkl")

# Initialize FastAPI
app = FastAPI(
    title="Aluminium Price Forecasting API",
    description="REST API for predicting aluminium prices using ML model",
    version="1.0"
)

# Input data schema
class InputData(BaseModel):
    Open: float
    High: float
    Low: float
    Volume: float


# Home route
@app.get("/")
def home():
    return {"message": "Aluminium Price Forecast API is running successfully"}


# Prediction endpoint
@app.post("/predict")
def predict_price(data: InputData):

    # Convert input to dataframe
    input_df = pd.DataFrame([[data.Open, data.High, data.Low, data.Volume]],
                            columns=["Open", "High", "Low", "Volume"])

    # Model prediction
    prediction = model.predict(input_df)

    return {
        "Predicted_Aluminium_Price": float(prediction[0])
    }
