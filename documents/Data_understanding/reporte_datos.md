# **Reporte de datos**
**Nombre del proyecto:** Detección de diabetes a partir de información médica y análisis de laboratorio
**Elaborado por:** Pedro Alejandro Astaiza Perafán
## **1. Tipo de datos, variable objetivo y calidad de datos**
---
### **1.1. Tipo de datos, datos nulos y volumen de datos**
- **Tamaño de datos:** 50KB
- **Cantidad de datos**: 1000 filas y 13 columnas, 13000 registros
- **Datos nulos:** No hay datos nulos
- **Columnas numéricas:** ID, No_partion, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL,BMI. 
- **Columnas letras o cadenas:** Gender, CLASS. 
- **Variable objetivo:** CLASS

### **1.2. Calidad de datos**
[ ] No se encuentran valores núlos o corruptos
[ ] Se espera que la variable objetivo clase tenga solo tres posibles valores (Y, N y P), sin embargo, estos valores presentan caracteres especiales, espacio adicionales o no están estandarizados (alguno en minúscula, por ejemplo), como se observa en la Figura 1. Se hace necesario procesar esta variable y eliminar los datos que no calzen dentro de las categorías esperadas.
[ ] La variable género (*Gender*) presenta datos erróneos y no estándarizados (minúsculas, con espacios, con carácteres especiales), como se observa en la Figura 1. Se hace necesario estandarizar la variable y eliminar los datos que no calzen en la categoría esperada.
[ ] Hay desbalanceo de datos, la clase (CLASS) **Y** es, aproximadamente, 8 veces la clase **N** y 16 veces la clase **P** como se observa en las Figura 1.

<img src="/documents/Data_understanding/data_img/EDA_distribucion_clases_barplot.png" alt="drawing" width="215px" height='215px'/>
<img src="/documents/Data_understanding/data_img/EDA_distribucion_genero_countplot.png" alt="drawing" width="400" height='200px'/>
<p style="text-align: center;"><b>Figura 1. Diagrama de Barras de las variables género (Gender) y clase (CLASS)</b></p>

## **2. Variable objetivo** 
---
La variable clase (**CLASS**) corresponde al diagnóstico de diabetes de un determinado paciente. Se esperan tres categorías o clases:
- **Y:** Detectado 
- **N:** No detectado
- **P:** Previsto<br>

Existen algunas categorías con algunos carácteres adicionales (espacios) y no se toman como iguales al momento del conteo. Se hace necesario limpiar los datos. Hay desbalanceo de datos, la cantidad de clases **Y** es, aproximadamente, 8 veces la clase **N** y 16 veces la clase **P**. 
## **3. Características**
---
De las variables de posibles características se eliminan las variables ID y el No_pation, dado que corresponden a variables categóricas (ID de la prueba y Número de paciente). De esta manera, las posibles características para el modelamiento son:
[ ] **Variables numéricas:** ID, No_partion, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL,BMI, AGE. 
[ ] **Variables categórica:** Gender.
En la Tabla 1 se muestran las medidas de tendencia central para el vector de características numéricas y en la Figura 2 se observa la distribución aproximada de las variables numéricas.

||Urea|Cr|HbA1c|Chol|TG|HDL|LDL|VLDL|BMI|AGE|
|---|---|---|---|---|---|---|---|---|---|---|
|mean|5.124743|68.943|8.28116|4.86282|2.34961|1.20475|2.60979|1.8547|29.57802|53.528000|
|max|38.900000|800.000|16.00000|10.30000|13.80000|9.90000|9.90000|35.0000|47.75000|79.000000|
|min|0.500000|6.000|0.90000|0.00000|0.30000|0.20000|0.30000|0.1000|19.00000|20.000000|
<p style="text-align: center;"><b>Tabla 1. Medidas de tendencia central para el vector de características</b></p>
<br>
<img src="/documents/Data_understanding/data_img/EDA_distribucion_caracter%C3%ADsticas_kdeplot.png" alt="drawing" width="1000" height='500px'/>
<p style="text-align: center;"><b>Figura 2. Distribución de las carecterísticas numéricas</b></p><br>

### 3.1. Pruebas de normalidad.
Los pruebas de normalidad (Shapiro, Kolmogorov-Smirnov, Kurtosis y Simetria) arrojan resultado negativo, por lo cual no se puede asumir que la distribución de las características sea Normal. En la Figura 3 se observan los gráficos QQ (cuartil-cuartil) de las características numéricas y en la Figura 4 de la edad (Se hizo aparte para una mejor distribució de las visualizaciones). 
<img src="/documents/Data_understanding/data_img/EDA_grafica_cuartiles_QQ.png" alt="drawing" width="1000" height='500px'/>
<p style="text-align: center;"><b>Figura 3. Graficas QQ </b></p><br>

<img src="/documents/Data_understanding/data_img/EDA_distribucion_edad_histplot.png" alt="drawing" width="500" height='300px'/>
<p style="text-align: center;"><b>Figura 4. Graficas QQ para la variable EDAD (AGE)</b></p><br>

Se puede buscar, en la etapa de procesamiento, si es posible normalizar las características.

## **4. Correlaciones**
---
### **4.1. Correlaciones entre las características**
En la Figura 5 se observa la matriz de correlación entre las variables numéricas y en la Figura 6 se observan los gráficos de cajas y bigotes de las variables numéricas por género. En general, no se observa una relación lineal entre las variables numéricas (sus correlaciones son bajas); en el caso de la relación con la variable categórica, no se observa dependencia entre estas.
<img src="/documents/Data_understanding/data_img/EDA_matriz_correlacion.png" alt="drawing" width="500" height='500px'/>
<p style="text-align: center;"><b>Figura 5.Matriz de correlación</b></p><br>
<img src="/documents/Data_understanding/data_img/EDA_relacion_genero.png" alt="drawing" width="1000" height='500px'/>
<p style="text-align: center;"><b>Figura 5. Cajas y bigotes por género.</b></p><br>

### **4.2. Relaciones con la variable objetivo**
<img src="/documents/Data_understanding/data_img/EDA_relacion_variable_objetivo.png" alt="drawing" width="1000" height='500px'/>
<p style="text-align: center;"><b>Figura 6. Cajas y bigotes por clase.</b></p><br>



