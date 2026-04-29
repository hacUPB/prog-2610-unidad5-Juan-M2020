import csv
peso_total=0
with open(".\\Bitacora\\ArchivosCSV\\Libro1.csv", 'r', encoding="utf-8") as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter= ';') #se utiliza el método reader
    encabezados = next(lector) #Lee la primera fila y la guarda en encabezado
    for fila in lector:          #con el for se itera sobre el objeto para leer
        peso_total += int(fila[4])
        print(fila)

print(f"Peso total de los aviones: {peso_total} kg")