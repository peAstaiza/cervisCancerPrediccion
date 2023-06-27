from preprocess import *
from prediccion import *

r = ["F",50,4.7,46,4.9,4.2,0.9,2.4,1.4,0.5,24]

X = preprocess_data(r,model=modelo_genero)
pca = pca_process(X,model=modelo_pca)[0]
pred = predict(pca.reshape(1,-1),modelo_prediccion)
print(pred)


