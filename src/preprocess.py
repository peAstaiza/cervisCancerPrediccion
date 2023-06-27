import joblib
import numpy as np

def procesar_variables_categoricas(x):
    try:
        return x.strip().upper()
    except:
        return ''

def preprocess_data(data,model):
    try:
        data[0] = model.transform(np.array([procesar_variables_categoricas(data[0])]))[0]
    except:
        return 0    
    return data

def pca_process(data,model):
    try:
        pca = model.transform(np.array(data).reshape(1,-1))
    except:
        return 0
    return pca


modelo_genero = joblib.load('./artefactos/encoder_genero.sav')

modelo_pca = joblib.load('./artefactos/pca.sav')

