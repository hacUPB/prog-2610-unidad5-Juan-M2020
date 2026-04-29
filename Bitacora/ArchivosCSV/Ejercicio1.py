import csv
Horas_uso = 0
with open(".\\Bitacora\\ArchivosCSV\\Componentes.csv"  , "r" ,encoding="utf-8") as csvfile:
    lector = csv.reader(csvfile, delimiter= ';')
    encabezado = next(lector)

    for fila in lector:
        Horas_uso += int(fila[2])
        print(fila)

print(f"Horas de uso total de los componentes: {Horas_uso}")

