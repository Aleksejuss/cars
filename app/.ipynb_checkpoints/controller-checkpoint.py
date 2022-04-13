import fastai
from fastai.vision.all import *
import pathlib
from fastbook import *
from fastai.vision.widgets import *
import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.staticfiles import StaticFiles
import torch


app = FastAPI()
app.mount("/static",StaticFiles(directory="static"), name = "static")

model = load_learner("./static/model.pkl", cpu = True)
model


@app.get("/")
def root():
    return "Hello Ondato"

# is my service is health.
@app.get("/health")
def health():
    return "OK"


@app.post("/predict")
async def predict(file: UploadFile):
    image = PILImage.create(file.file)
    pred, pred_idx, probs = model.predict(image)
    return {"class": pred}
    



