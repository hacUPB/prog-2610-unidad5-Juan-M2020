nombre_archivo = input("Nombra tu nuevo archivo (ej: diario.txt): ")

# Contexto de escritura
with open(".\\Bitacora\\ArchivosTextos\\nombre_archivo", 'w+') as archivo:
    datos = input("Escribe tu primer secreto: ")
    archivo.write(datos)
    archivo.seek(0) #mover el puntero al inicio del archivo
    print("\n--- Leyendo tu archivo ---")
    print(archivo.read())

# # Contexto de lectura
# with open(".\\Bitacora\\ArchivosTextos\\nombre_archivo", 'r') as archivo:
#     print("\n--- Leyendo tu archivo ---")
#     print(archivo.read())