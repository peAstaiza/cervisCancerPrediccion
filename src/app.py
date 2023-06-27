from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import numpy as np

from preprocess import *
from prediccion import *

app = FastAPI()


@app.get("/")
def index():
    return {
        "message": "Servición de procesamiento "
    }

@app.post("/prepr")
def prepro(data:dict):
    datos = jsonable_encoder(data)
    datos_dict = list(datos['data'])
    datos_prep = preprocess_data(data=datos_dict,model=modelo_genero)
    datos_pca = pca_process(datos_prep,model=modelo_pca)[0]
    resultado = [x.item() for x in datos_pca]
    return {
        "response":resultado
    }

@app.post("/pred")
def prediccion_diabetes(data:dict):
    datos = jsonable_encoder(data)
    datos_dicts = np.array(datos['response'])
    etiqueta = predict(datos_dicts,model=modelo_prediccion) 
    return etiqueta