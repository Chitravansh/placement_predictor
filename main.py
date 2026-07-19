from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle 
import numpy as np 

app = FastAPI() # making an object of the fast api 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

model = pickle.load(open("model.pkl","rb"))
scaler= pickle.load(open("scaler.pkl","rb"))

class Student(BaseModel):
    cgpa: float
    iq: float 

    


@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.post("/predict")
def predict(student: Student ):
    data = np.array([[student.cgpa, student.iq]])

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    return {
        "placement" : int(prediction[0])
    }


# @app.post("/predict")
# def predi t