import sys
from pydantic import BaseModel
import pandas as pd
from pycaret.regression import *
import joblib

from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

# Initialize model artifacte files. This will be loaded at the start of FastAPI model server.
model = joblib.load('insurance_gbr_model_23122020.pkl')

class PredictionRequest(BaseModel):
    """
    Define the input schema for the prediction request
    """
    age: int
    sex: str
    bmi: float
    children: int
    smoker: bool
    region: str
    
@app.get("/")
async def read_root():
    message = f"Hello PyCaret! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}

@app.post("/predict")
async def predict(request: PredictionRequest):
    # Load the trained model
    # model = load_model('./k8s_streamlit/insurance_gbr_model_23122020')
    
    # Convert the input data to a DataFrame
    input_data = {
        'age': request.age,
        'sex': request.sex,
        'bmi': request.bmi,
        'children': request.children,
        'smoker': request.smoker,
        'region': request.region
    }
    
    input_df = pd.DataFrame(input_data, index=[0])
    
    # Make predictions using th loaded model
    predictions = predict_model(model, data=input_df)
    # print(predictions.columns)
    
    # Return the predictions as a dictionary
    return {"predictions": float(predictions['prediction_label'][0])}