# **Reporte final**
---
- **Nombre del proyecto**: Detección de diabetes a partir de información médica y análisis de laboratorio
- **Elaborado por:** Pedro Alejandro Astaiza Perafán
---
Este informe describe los resultados del proyecto de detección de diabetes a partir de información y análisis de laboratorio y diagnóstico.

## **1. Resultados del proyecto**
---
### **1.1. Resumen de los entregables y logros alcanzados en cada etapa del proyecto.**
- **1. Fase de entendimiento de negocio y datos:** 
    - [ ] Se entrega los documentos de diccionario de datos, resumen de datos, reporte de datos y entendimiento de negocio.  
    - [ ] Se entrega scripts de Análisis exploratorio de datos (*.ipynb*)
    - [ ] Se entrega la documentación técnica de los procesos y scripts de ingesta, exploración de datos.
- **2. Fase de Procesamiento:**
    - [ ] Se entregan el *script* de procesamiento y los artefactos generados.
    - [ ] Se entrega el conjunto de datos preprocesado.
- **3. Fase de modelamiento y selección:** 
    - [ ] Se entrega el documento de linea base y modelado final.
    - [ ] Se entrega el resumen de métricas obtenidas (*.csv*)
    - [ ] Se entrega el script de modelamiento (*ipynb*) y los artefactos obtenidos durante ese proceso.
- **4. Fase de evaluación y entrega:**
    - [ ] Se entregan los *scripts* (*.py*) de los servicios de preprocesamiento y predicción.
    - [ ] Se entrega el documento de despliegue del servicio.    

### **1.2. Evaluación del modelo final y comparación con el modelo base.**
**Accuracy y F1-score para modelos**
|Modelo|Accuracy|F-score|
|----|----|----|
|Regresión logística|0.92|0.77|
|Bosqués aleatorios (final)|0.93|0.80|

**F1-Score por clase para modelos**
|Modelo|Clase N|Clase Y|Clase P|
|---|---|---|---|
|Regresión Logística base|0.70|0.95|0|
|Bosques aleatorios  (final)|0.76|0.96|0.67|

**Accuracy por clase para modelos**
|Modelo|Clase N|Clase Y|Clase P|
|---|---|---|---|
|Regresión Logística base|0.70|0.94|0|
|Bosques aleatorios (final)|0.76|0.96|0.75|


## **2. Lecciones aprendidas**
---
### **2.1. Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.**
- El conjunto de datos presentaba bastantes valores vacios (nulos).
- El conjunto de datos presentaba fuerte desbalanceo.
### **2.2. Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.**
- Metodología y documentación para los proyectos de ML
- Versionamiento de datos y manejo de datos y artefactos y conexión con el versionamiento de código.
- Veriosanmiento de modelos y experimentos, y conexión con el versionamiento de código.
- Despliegue de modelos y servicios de procesamiento y predicción.

## **3. Impacto del proyecto**
---
- Como proyecto pedagógico y de aprendizaje, permite conocer los elementos y fases de un proyecto de ML, desde su entendimiento hasta su despliegue.
- Como proyecto de ML, se propone un modelo con mejor desempeño y que maneja de manera eficiente el desbalanceo de datos presente en el conjunto de datos, respecto al modelo de línea base. 

## **4. Conclusiones**
- El modelo propuesto cumple con los objetivos de desempeño (precisión y f-score) del proyecto.
- Como recomendación, un conjunto de datos más grande que permita entender la distribución de los datos y aplicar mejores métodos de procesamiento y modelado. 
- Como recomendación, usar herramientas de versionamiento de modelos (como *mlflow*). En este caso, debido a ciertas limitaciones, no se hizo uso de estas herramienta. 

## **5. Agradecimientos**

- Agradecimientos al equipo del programa de Formación en ML de la Universidad Nacional. A los profesores, docentes guías y personal de acompañamiento y administrativo, mis sinceros agradecimientos. 