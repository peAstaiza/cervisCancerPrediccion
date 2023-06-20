# Documento de Línea base para modelos
---
**Nombre del proyecto:** Detección de diabetes a partir de información médica y análisis de laboratorio.
**Elaborado por:** Pedro Alejandro Astaiza Perafán.<br>

## **1. Análisis de componentes principales (PCA)**
---
En la Figura 1 se muestra la gráfica de varianza explicativa, respecto al número de componentes principales para el conjunto de datos de entrenamiento. A partir de la Figura se toma seis componentes principales.

<div style="text-align: center;">
  <p align="center">
    <img src="/documents/Modelamiento/imagenes/pca.png" alt="drawing" width="400px" height='400px'/>
  </p>
</div>
<p align="center"><b>Figura 1. Varianza acumulada de los componentes principales</b></p>

## **2. Regresión logística (modelo base).**
---
Tomado de: [pyspark-diabetes-eda-and-prediction](https://www.kaggle.com/code/kelvinfoo123/pyspark-diabetes-eda-and-prediction)
### **2.1. Parámetros de entrenamiento.**
Ninguno
### **2.2. Desempeño**
- [ ] *Accuracy:* 0.90
- [ ] *F1-Score:* 0.58
- [ ] *Matriz de confusión:*
<div style="text-align: center;">
  <p align="center">
    <img src="/documents/Modelamiento/imagenes/Base.png" alt="drawing" width="400px" height='400px'/>
  </p>
</div>
<p align="center"><b>Figura 2. Matriz de confusión para el modelo de regresión logística</b></p>

## **3. Regresión logística con pesos ponderados.**
### **3.1. Parámetros de entrenamiento**
- [ ] **Pesos ponderados:** 
```
0: 3.24 # Clase N
1: 0.39  # Clase Y
2: 6.19 # Clase P
```
### **3.2. Desempeño**
- [ ] *Accuracy:* 0.92
- [ ] *F1-score:* 0.77
- [ ] *Matriz de confusion:*
<div style="text-align: center;">
  <p align="center">
    <img src="/documents/Modelamiento/imagenes/RL.png" alt="drawing" width="400px" height='400px'/>
  </p>
</div>
<p align="center"><b>Figura 3. Matriz de confusión para el modelo de regresión logística</b></p>

## **4. árbol de decisión**
---
### **4.1. Parámetros de entrenamiento**
- [ ] **Máxima profundadid (*max_depth*):** 20
### **4.2. Desempeño**
- [ ] *Accuracy:* 0.94
- [ ] *F1-score:* 0.84
- [ ] *Matriz de confusion:*
<div style="text-align: center;">
  <p align="center">
    <img src="/documents/Modelamiento/imagenes/DT.png" alt="drawing" width="400px" height='400px'/>
  </p>
</div>
<p align="center"><b>Figura 4. Matriz de confusión para el árbol de decisión</b></p>

## **5. Bosques aleatorios**
---
### **5.1. Parámetros de entrenamiento**
- [ ] **Máxima profundadid (*max_depth*):** 10 
- [ ] **Pesos ponderados:** 
```
0: 3.24 # Clase N
1: 0.39  # Clase Y
2: 6.19 # Clase P
```
- [ ] **Número de estimadores:** 300
### **5.2. Desempeño**
- [ ] *Accuracy:* 0.93
- [ ] *F1-score:* 0.80
- [ ] *Matriz de confusion:*
<div style="text-align: center;">
  <p align="center">
    <img src="/documents/Modelamiento/imagenes/RF.png" alt="drawing" width="400px" height='400px'/>
  </p>
</div>
<p align="center"><b>Figura 5. Matriz de confusión para el bosque aleatorio</b></p>

### **6. Resultados finales**
---
**Accuracy y F1-score para modelos**
|Modelo|Accuracy|F-score|
|----|----|----|
|Regresión logística|0.92|0.77|
|Árboles de decisión|0.94|0.84|
|Bosqués aleatorios|0.93|0.80|

**F1-Score por clase para modelos**
|Modelo|Clase N|Clase Y|Clase P|
|---|---|---|---|
|Regresión Logística base|0.70|0.95|0|
|Regresión Logística|0.79|0.96|0.55|
|Árboles de decisión|0.76|0.97|0.78|
|Bosques aleatorios|0.76|0.96|0.67|

**Accuracy por clase para modelos**
|Modelo|Clase N|Clase Y|Clase P|
|---|---|---|---|
|Regresión Logística base|0.70|0.94|0|
|Regresión Logística|0.70|0.99|0.50|
|Árboles de decisión|0.76|0.98|0.69|
|Bosques aleatorios|0.76|0.96|0.75|


## **7. Guardado de métricas y artefactos**
---
- [ ] Las métricas de desempeño (*accuracy, F1-score*) se almacenaron el archivo *metrics.csv* (*.\documents\Modelamiento\metrics.csv*)
- [ ] La matriz de confusión de los modelos se almacenan en la carpeta *imagenes* (.\documents\Modelamiento\imagenes*)
- [ ] Los modelos desarrollados se almacenan en la carpeta *artefactos* (*.\scripts\Modelamiento\artefactos*).
- [ ] Los artefactos de preprocesamiento se almacenan en la caréta *artefactos* (*.\scripts\Preprocesamiento\artefactos*)