# Diccionario de datos
- **Nombre del proyecto:** Detección de diabetes a partir de información médica y análisis de laboratorio
- **Elaborado por:** Pedro Alejandro Astaiza Perafán

## Base de datos 1

El conjunto de datos se encuentra disponible en Diabetes Dataset y corresponde a Los datos de la sociedad iraquí, obtenidos del laboratorio del Hospital de la Ciudad Médica y del Centro Especializado en Endocrinología y Diabetes del Hospital Docente Al-Kindy (Rashid, Ahlam (2020), “Diabetes Dataset”, Mendeley Data, V1, doi: 10.17632/wj9rwkp9c2.1). El conjunto de datos consiste en un archivo plano (.csv) con los siguientes atributos: Número de pacientes, nivel de azúcar en sangre, edad, sexo, índice de creatinina (Cr), índice de masa corporal (IMC), urea, colesterol (Chol), perfil lipídico en ayunas, incluidos colesterol total, LDL, VLDL, triglicéridos (TG) y HDL, HBA1C, clase (la clase de enfermedad diabética del paciente puede ser diabético, no diabético o diabético previsto).

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| ID | Número de registro | Entero | [1 \infty) | Dataset of Diabetes.cvs |
| No_Pation | Número de registro del paciente | Entero | Rango/Valores posibles | Dataset of Diabetes.cvs |
| Gender | Género/sexo del paciente | Cadena (Categórico nominal) | {M,F} | Dataset of Diabetes.cvs |
| AGE | Edad en años del paciente | Entero | min: 20 max: 80 | Dataset of Diabetes.cvs |
| Urea | Tase de úrea en la sangre | Flotante | Mayor que cero | Dataset of Diabetes.cvs |
| Cr | Tasa de creatinina en la sangre | Flotante | Mayor que cero | Dataset of Diabetes.cvs |
| HbAlc | Prueba de hemoglobina glicosilada | Flotante (porcentaje) | [0,100] | Dataset of Diabetes.cvs |
| Chol | Prueba de colesterol | Flotante | Mayor que cero | Dataset of Diabetes.cvs |
| TG | Prueba de triglicéridos | Floatante | Mayor que cero | Dataset of Diabetes.cvs |
| HDL | Nivel de HDL en la sangre | Flotante | Mayor que cero | Dataset of Diabetes.cvs |
| LDL | Nivel de LDL en la sangre | Flotante | Mayor que cero | Dataset of Diabetes.cvs |
| VLDL | Nivel de VLDL en la sangre | Flotante | Mayor que cero | Dataset of Diabetes.cvs |
| BMI | Indice de masa corporal (IMC) | Flotante | Mayor que cero | Dataset of Diabetes.cvs |
| CLASS | Diagnóstico del paciente | Cadena (Categórico nominal) | {Y: diabético, N: no diabético, P: diabético previsto} | Dataset of Diabetes.cvs |

