# **Reporte de modelo final**
---
**Nombre del proyecto:** Detección de diabetes a partir de información médica y análisis de laboratorio.
**Elaborado por:** Pedro Alejandro Astaiza Perafán.<br>
## Información sobre el modelo escogido.
- [ ] Librería: scikit-learn 1.2.2
- [ ] Algoritmo seleccionado: Bosques aleatorios (*RandomForestClassifier*)
- [ ] Hiperparámetros de entrenamiento:
    - *Máxima profundidad:* 10
    - *Número de estimadores:* 300
    - *Pesos ponderados:* 
```
0: 3.24 # Clase N
1: 0.39  # Clase Y
2: 6.19 # Clase P
```
## Desempeño y evaluación del modelo
En la Figura 1 se presenta la matriz de confusión.

<div style="text-align: center;">
  <p align="center">
    <img src="/documents/Modelamiento/imagenes/RF.png" alt="drawing" width="400px" height='400px'/>
  </p>
</div>
<p align="center"><b>Figura 1. Matriz de confusión para el bosque aleatorio</b></p>

A continuación, se muestra el reporte de evaluación (*classification report*)
```
  precision    recall  f1-score   support

           0       0.76      0.76      0.76        21
           1       0.96      0.97      0.96       169
           2       0.75      0.60      0.67        10

    accuracy                           0.93       200
   macro avg       0.82      0.78      0.80       200
weighted avg       0.93      0.93      0.93       200
```