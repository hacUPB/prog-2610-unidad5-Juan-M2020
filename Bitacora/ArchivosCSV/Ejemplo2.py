import csv

# 1. Abrimos el archivo asegurando la codificación correcta
with open(".\\Bitacora\\ArchivosCSV\\Componentes.csv", mode='r', encoding='utf-8') as archivo:

    # 2. Inicializamos el DictReader
    lector = csv.DictReader(archivo,delimiter=';')

    # 3. Iteramos sobre cada fila del archivo
    for fila in lector:
        # ¡Miren qué fácil es acceder a los datos por su nombre!
        item = fila['Item']
        partes = fila['Partes']
        horas_uso = fila['Horas de uso']
   

        print(f"El Avion {item} tiene {horas_uso} horas de uso en {partes}.")