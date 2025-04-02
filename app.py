from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.linear_model import LogisticRegression


X_train = np.array([[5.1, 3.5], [4.9, 3.0], [6.0, 2.7], [5.8, 2.8]])  # długość i szerokość płatka
y_train = np.array([0, 0, 1, 1])  # 0=setosa, 1=versicolor

model = LogisticRegression()
model.fit(X_train, y_train)

app = FastAPI(
    title="Flower Classification API",
    description="API do klasyfikacji gatunków irysów",
    version="1.0.0"
)


class PredictionInput(BaseModel):
    sepal_length: float
    sepal_width: float

@app.get("/")
def home():
    return {"message": "Witaj w API modelu ML!"}

@app.get("/info")
def info():
    return {
        "model_type":str(type(model).__name__),
        "title":app.title,
        "description":app.description,
        "input_features":2,
        "feature_names":["sepal_length", "sepal_width"],
        "classes":["setosa","versicolor"],
        "api_version": app.version
    }

@app.get("/health")
def health():
    return {"status":"OK", "details":"Serwer działa poprawnie"}

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        features = [[input_data.sepal_length, input_data.sepal_width]]
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].tolist()
    
        return {
            "prediction": int(prediction),
            "class_name": "setosa" if prediction == 0 else "versicolor",
            "probability": probability,
            "input_data": input_data.dict()
                }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "error":"Błąd podczas predykcji",
                "message":str(e)
            }
        )
