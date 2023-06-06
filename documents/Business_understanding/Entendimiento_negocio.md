# Entendimiento del negocio.
## Histórico del documento
- **Nombre del proyecto**: Detección de diabetes a partir de información médica y análisis de laboratorio
- **Elaborado por:** Pedro Alejandro Astaiza Perafán

| Nombre de documento | Versión | Fecha de entrega | Entregado por | Descripción |
|------|---------|-------|-------|-------|
| Entendimiento de negocio | 1.0 | 6 de junio de 2023 | Pedro Astaiza | Primera versión del documento de entendimiento del negocio |


## 1. Objetivo del Proyecto
La diabetes es una enfermedad crónica que afecta a millones de personas en todo el mundo, que se caracteriza por la presencia de altos niveles de glucosa en la sangre. Esta enfermedad puede tener graves consecuencias para la salud si no se detecta a tiempo. Por esta razón, es importante que los pacientes se realicen exámenes médicos periódicos para detectarla en sus primeras etapas.La detección temprana de la diabetes puede ayudar a prevenir complicaciones graves en el futuro, dado que se pueden tomar medidas para controlar los niveles de glucosa en la sangre y prevenir los problemas de salud asociados.<br>
De esta manera, el objetivo es predecir diagnósticamente si un paciente tiene diabetes, basándose en determinadas mediciones diagnósticas y resultados de laboratorio.

## 2. Alcance del Proyecto
### 2.1. Conjunto de datos:
El conjunto de datos se encuentra disponible en [Diabetes Dataset](https://data.mendeley.com/datasets/wj9rwkp9c2/1) y corresponde a Los datos de la sociedad iraquí, obtenidos del laboratorio del Hospital de la Ciudad Médica y del Centro Especializado en Endocrinología y Diabetes del Hospital Docente Al-Kindy (Rashid, Ahlam (2020), “Diabetes Dataset”, Mendeley Data, V1, doi: 10.17632/wj9rwkp9c2.1). El conjunto de datos consiste en un archivo plano (.csv) con los siguientes atributos: Número de pacientes, nivel de azúcar en sangre, edad, sexo, índice de creatinina (Cr), índice de masa corporal (IMC), urea, colesterol (Chol), perfil lipídico en ayunas, incluidos colesterol total, LDL, VLDL, triglicéridos (TG) y HDL, HBA1C, clase (la clase de enfermedad diabética del paciente puede ser diabético, no diabético o diabético previsto).
### 2.3. Resultados esperados
Se espera un modelo que permita predecir si un paciente tiene diabetes, dado un conjunto de mediciones diagnósticas.

### 2.4. Criterios de éxito del proyecto
- Métricas de desempeño del modelo: precisión, valor-F

### 2.2. Excluye:

- El proyecto no incluye elementos de desarrollo web o el desarrollo de un aplicativo para el uso del modelo.
- El proyecto no incluye elementos, recursos o servicios, que necesiten pago.

## 3. Metodología

Para la ejecución del proyecto se propone la metología CRISP-DM, la cual plantea 6 pasos iterativos y cíclicos:
- **Entendimiento del negocio:** Entendimiento de los requerimientos, objetivos del proyecto, tareas a desarrollar, entre otros.
- **Entendimiento de los datos:** Análisis exploratorio de datos (EDA), revisión de datos nulos, corruptos, relación entre variables, tipos de datos y variable objetivo.
- **Preparación de los datos:** Limpieza de datos, preprocesamiento, ingeniería de características.
- **Modelado:** Selección del algoritmo (o algoritmos) a desarollar, selección de hiperparámetros, desarollo e implementación del modelo.
- **Evaluación:** Métricas de desempeño del modelo, ajuste en caso de ser necesario y retroalimentación.
- **Despliegue** Puesta en producción del modelo.

## 4. Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas | del 22 de mayo al 2 de junio |
| Preprocesamiento, análisis exploratorio | 1 semanas | del 29 de mayo al 2 de junio |
| Modelamiento y extracción de características | 2 semanas | del 5 de junio al 16 de junio |
| Evaluación, retroalimentación y verificación| 1 semanas | del 19 de junio al 23 de junio | 
| Despliegue | 1 semanas | del 26 de junio al 30 de junio |
| Evaluación y entrega final | 1 semanas | del 26 de junio al 30 de junio |

## 5. Equipo del Proyecto
- Pedro Alejandro Astaiza Perafán

## 6. Entregas y entregables
- **Fase 1:** Documento de entendimiento de negocio, diccionario de datos y código de cargue de datos.
- **Fase 2:** Código de preprocesamiento de datos, código y reporte de EDA, documento de definición de datos y reporte de resumen de datos.

## 7. Aprobaciones