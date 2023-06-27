import joblib

modelo_prediccion = joblib.load('./artefactos/random_forest.sav')

encoderClases = joblib.load('./artefactos/encoder_clase.sav')

def predict(data,model):
    try:
        pred = encoderClases.inverse_transform(model.predict(data.reshape(1,-1)))[0]
    except:
        return 'error'
    return pred