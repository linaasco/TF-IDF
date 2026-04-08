import numpy as np
import math

# PASO 1: Dataset con tus artículos
documents = [
    "La Institución podrá desarrollar programas de educación informal, los cuales no conducirán a la obtención de títulos profesionales ni a certificaciones de aptitud ocupacional. Estos programas serán denominados programas de educación o formación continuada.",
    "El número de créditos de un programa académico y de los espacios formativos que lo integren será el definido por el Consejo Superior en consideración a las recomendaciones hechas por el Consejo Académico.",
    "El número de créditos académicos de una actividad en el plan de estudios será el resultado de dividir entre 48 el total de horas que el estudiante debe emplear",
    "Una vez culminado el proceso de admisión, la Institución informará al aspirante, los resultados correspondientes.",
    "La documentación allegada por los aspirantes no admitidos, o aquellos que habiendo sido admitidos a un programa no se matriculen, serán suprimidos de los sistemas de información institucionales.",
    "Los resultados del proceso de admisión en cada una de las pruebas y procedimientos desarrollados, son de reserva institucional y en ningún caso se comunican a terceras personas, salvo las excepciones contenidas en la ley.",
    "El porcentaje máximo de créditos homologables para el programa académico será del 60%.",
    "Los estudiantes transferentes deben cumplir con los prerrequisitos de las asignaturas como condición indispensable para poder inscribir y cursar las asignaturas del plan de estudios.",
    "Los estudiantes de la Institución se clasifican en estudiantes regulares y estudiantes de extensión.",
    "Se denomina estudiante regular a aquel que se ha matriculado en cualquiera de los programas académicos que conduzcan a un título académico formal, previo el cumplimiento de los requisitos exigidos por los mandatos legales, los Estatutos y los Reglamentos de la Institución."
]

def calcular_tf(termino, documento):
    palabras = documento.lower().replace(",", "").replace(".", "").split()
    if len(palabras) == 0: return 0
    return palabras.count(termino.lower()) / len(palabras)

def calcular_idf(termino, corpus):
    n = len(corpus)
    # Contamos en cuántos documentos aparece la palabra
    df = sum(1 for doc in corpus if termino.lower() in doc.lower())
    if df == 0: return 0
    return math.log(n / df)

def motor_busqueda(consulta, corpus):
    palabras_consulta = consulta.lower().split()
    resultados = []
    
    for i, doc in enumerate(corpus):
        score_total = 0
        for palabra in palabras_consulta:
            tf = calcular_tf(palabra, doc)
            idf = calcular_idf(palabra, corpus)
            score_total += (tf * idf)
        
        resultados.append({"id": i + 1, "doc": doc, "score": score_total})
    
    return sorted(resultados, key=lambda x: x["score"], reverse=True)

# --- EJECUCIÓN DE PRUEBAS (ESTILO PROFE) ---
consultas_ejemplo = ["créditos", "admisión", "estudiantes"]

for consulta in consultas_ejemplo:
    # Como el ejemplo del profe es para un término, calculamos el IDF de ese término principal
    palabras = consulta.lower().split()
    termino_principal = palabras[0]
    idf_valor = calcular_idf(termino_principal, documents)
    
    print(f"\nIDF para el término '{termino_principal}': {idf_valor:.4f}")
    
    ranking = motor_busqueda(consulta, documents)
    
    for i, res in enumerate(ranking, 1):
        # Mostramos el ranking, el texto del documento y su score final
        # Limitamos el texto a 70 caracteres para que se vea ordenado como en la imagen
        texto_corto = (res['doc'][:70] + '..') if len(res['doc']) > 70 else res['doc']
        print(f" {i} - Documento: {texto_corto}: TF-IDF = {res['score']:.4f}")

# 1. Obtener todas las palabras únicas del reglamento
todas_las_palabras = set()
for doc in documents:
    palabras = doc.lower().replace(",", "").replace(".", "").split()
    todas_las_palabras.update(palabras)

# 2. Calcular el IDF de cada palabra única
lista_idf = []
for palabra in todas_las_palabras:
    valor_idf = calcular_idf(palabra, documents)
    lista_idf.append((palabra, valor_idf))

# 3. Ordenar para obtener los extremos
lista_idf.sort(key=lambda x: x[1], reverse=True)

print("\n⬆ TOP 5 - IDF MÁS ALTO (Palabras más específicas):")
for palabra, score in lista_idf[:5]:
    print(f"- {palabra}: {score:.4f}")

print("\n⬇ TOP 5 - IDF MÁS BAJO (Palabras más comunes):")
# Filtramos las que tienen los scores más bajos al final de la lista
for palabra, score in lista_idf[-5:]:
    print(f"- {palabra}: {score:.4f}")