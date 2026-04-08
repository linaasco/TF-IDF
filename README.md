Motor de Búsqueda de Reglamento Estudiantil (TF-IDF) 
Este proyecto implementa un motor de búsqueda básico para fragmentos de un reglamento institucional utilizando el algoritmo TF-IDF (Term Frequency - Inverse Document Frequency). El sistema permite realizar consultas en lenguaje natural y devuelve los artículos más relevantes ordenados por su puntaje de importancia.

Características
Dataset: 10 artículos reales/simulados del reglamento estudiantil.

Procesamiento: Cálculo manual de TF (frecuencia local) e IDF (importancia global).

Búsqueda Multi-palabra: El score final es la suma de los pesos de cada término de la consulta.

Ranking: Resultados ordenados de mayor a menor relevancia.

Tecnologías utilizadas
Python 3.14.3

Numpy: Para operaciones matemáticas eficientes.

Math: Para el cálculo de logaritmos en la fórmula IDF.

Estructura del Proyecto
TF-IDF.py: Script principal con la lógica del motor de búsqueda.

README.md: Documentación del proyecto.

Instalación y Uso

Crear entorno virtual
Bash
python -m venv venv    

Activar entorno
Bash
.\venv\Scripts\Activate

Ejecutar el motor:

Bash
python TF-IDF.py

Ejemplos de Ejecución
A continuación se muestran los resultados obtenidos tras realizar búsquedas específicas en el sistema:

Caso 1: Búsqueda de 'créditos académicos'
El sistema identifica correctamente los artículos que definen el valor y la homologación de créditos.
<img width="1012" height="110" alt="Captura de pantalla 2026-04-07 200910" src="https://github.com/user-attachments/assets/c574ab15-fe90-4ce5-b5de-b1c6719f68a4" />

Caso 2: Búsqueda de 'proceso admisión'
Filtra artículos relacionados con el ingreso y la reserva de información.
<img width="976" height="117" alt="image" src="https://github.com/user-attachments/assets/a8677edb-57d5-4878-a232-fd6a60043b80" />

Caso 3: Búsqueda de 'estudiantes regulares'
Filtra artículos relacionados con los procesos que deben cumplir los estudiantes regulares.
<img width="970" height="99" alt="image" src="https://github.com/user-attachments/assets/afce6a67-4159-4978-8310-b34895fecff3" />

¿Por qué TF-IDF?
A diferencia de una búsqueda simple de palabras (que daría la misma importancia a conectores como "la" o "de"), el modelo TF-IDF asegura que las palabras técnicas y raras (como homologables, admisión o disciplinaria) tengan un mayor peso en el ranking, mejorando la precisión de la búsqueda.

Integración con RAG (LLMs)
Este motor puede servir como el componente de Recuperación (Retrieval) en un flujo RAG. En lugar de enviar todo el reglamento a un modelo como Gemini o GPT, este algoritmo selecciona solo los fragmentos más importantes, reduciendo costos y evitando que el modelo de lenguaje se confunda con información irrelevante.
