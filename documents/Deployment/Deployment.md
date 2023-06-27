# **Despliegue: Información técnica**
---
- **Nombre del proyecto**: Detección de diabetes a partir de información médica y análisis de laboratorio
- **Elaborado por:** Pedro Alejandro Astaiza Perafán
---
## **1.Infraestructura**

- **Nombre del modelo:** Predicción
- **Plataforma de despliegue:** FastAPI, uvicorn
- **Requisitos técnicos:** 
    - python 3.11.4
- **Diagrama de arquitectura:** 
<p align="center">
  <img src="./documents/Deployment/Arquitectura.png" alt="drawing" width="500" height='200px'/>
</p>

## **2.Código de despliegue**
- **Archivo principal:** *.\src\app.py* 
- **Rutas de acceso a los archivos:** 
    - *.\src\prediccion.py*
    - *.\src\preprocess.py*
    - *.\src\artefactos\random_forest.sav*
    - *.\src\artefactos\encoder_genero.sav*
    - *.\src\artefactos\encoder_clase.sav*
    - *.\src\artefactos\pca.sav*
    - *.\src\requeriments.txt*
- **Variables de entorno:** No se consideran.

## **3. Documentación del despliegue**

- Crear un entorno virtual e instala las dependencias 
```
python3.11.4 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
- Acceder al directorio src
```
$cd src
```
- Desplegar la aplicación (usando uvicorn)
```
uvicorn app:app --reload
``` 