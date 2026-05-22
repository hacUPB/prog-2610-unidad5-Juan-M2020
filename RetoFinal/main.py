while True:
    print("\n=== Explorador CLI ===")
    print("1. Explorar Directorios")
    print("2. Textos Reales (.txt)")
    print("3. Datos Abiertos (.csv)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    #Explorador de directorios
    if opcion == "1":
        print(f"\narchivos disponibles")

        from pathlib import Path
        ruta = Path(".\\RetoFinal\\Datos")
        print("-------------")
        for file in ruta.iterdir(): 
           print(f"📝 {file.name}")
        print("-------------")

        print(f"cual quieres ver?")

        n_archivo = input("Ingrese el nombre del archivo: ")
        ruta = ".\\RetoFinal\\Datos\\" + n_archivo

        with open(ruta, 'r', encoding="utf-8") as archivo:
            print("\n--- Leyendo tu archivo ---")
            print(archivo.read())
            print("-------------------------------------------------")

     

    #Textos Reales (.txt)
    elif opcion == "2":            
        while True:
            print("\n=== Textos Reales (.txt) ===")
            print("1. Resumen Estadístico del Texto")
            print("2. Extracción de Patrones (Logs)")
            print("3. Frecuencia de palbras claves")
            print("4. Distribución de Longitud de Líneas")
            print("5. Regresar")

            opcion = input("Seleccione una opción: ")

            # Resumen estadistico
            if opcion == "1":
                with open(".\\RetoFinal\\Datos\\Operaciones.txt", 'r', encoding="utf-8" ) as operaciones:
                    
                    contenido = operaciones.read()

                    #lineas
                    linea = contenido.split('\n')
                    cantidad_lineas = len(linea)

                    #cantidad palabras
                    palabras = contenido.split()
                    can_palabras = len(palabras)

                    #cantidad caracteres
                    carac = len(contenido) #con espacios
                    carac_sin = len(contenido.replace(" ", "").replace("\n", ""))

                    #Top 5
                    from collections import Counter

                    # Conectores que no quieres contar
                    conectores = [
                        "de", "la", "el", "los", "las",
                        "y", "o", "a", "en", "por",
                        "para", "con", "del", "al",
                        "no"
                    ]

                    # Filtrar palabras
                    palabras_filtradas = []

                    for palabra in palabras:
                        if palabra not in conectores:
                            palabras_filtradas.append(palabra)

                    # Contar repeticiones
                    contador = Counter(palabras_filtradas)

                    top_5 = contador.most_common(5)
                    print("-------------------------------")
                    print("Top 5 palabras más repetidas:\n")

                    for palabra, cantidad in top_5:
                        print(palabra, ":", cantidad)

                    print(f"\n      📊 Estadisticas 📊     ")
                    print(f"el archivo tiene {cantidad_lineas} lineas")
                    print(f"el archivo tiene {can_palabras} palabras")
                    print(f"el archivo tiene {carac} caracteres")
                    print(f"el archivo tiene {carac_sin} caracteries sin espacios")
                    print("------------------------------------------------")
                    

            # Extracción de Patrones (Logs)   
            elif opcion == "2":
                from collections import Counter

                with open(".\\RetoFinal\\Datos\\Operaciones.txt", 'r', encoding="utf-8") as operaciones:

                    texto = operaciones.read()

                # Separar palabras
                palabras = texto.split()

                # Patrones que quieres buscar
                patrones = ["ERROR", "404"]
                fechas = ["2025-01-10", "2025-01-11", "2025-01-12", "2025-01-13", "2025-01-14"]

                # Filtrar palabras
                palabras_pa = []
                for palabra in palabras:
                    if palabra in patrones:
                        palabras_pa.append(palabra)

                fecha_pa = []
                for palabra in palabras:
                    if palabra in fechas:
                        fecha_pa.append(palabra)        

                # Contar repeticiones
                contador = Counter(palabras_pa)
                contador_fechas = Counter(fecha_pa)
                
                print("----------- ♟️  ​ Patrones ♟️ -------------​")
                # Mostrar resultados
                for palabra, cantidad in contador.items():
                    print(f"La palabra {palabra} se repite {cantidad} veces")
                
                for palabra, cantidad in contador_fechas.items():
                    print(f"La Fecha {palabra} se repite {cantidad} veces")
                print("------------------------------------------")

            # Frecuencia de palbras claves
            if opcion == "3":
                import matplotlib.pyplot as plt
                from collections import Counter

                with open(".\\RetoFinal\\Datos\\Operaciones.txt", 'r', encoding="utf-8") as operaciones:

                    texto = operaciones.read()

                # Separar palabras
                palabras = texto.split()

                # Conectores que no quieres contar
                conectores = [
                    "de", "la", "el", "los", "las",
                    "y", "o", "a", "en", "por",
                    "para", "con", "del", "al",
                    "no"
                ]

                # Filtrar palabras
                palabras_filtradas = []

                for palabra in palabras:
                    if palabra not in conectores:
                        palabras_filtradas.append(palabra)

                # Contar repeticiones
                contador = Counter(palabras_filtradas)

                # Top 10
                top_10 = contador.most_common(10)

                # Separar palabras y cantidades
                categorias = []
                valores = []

                for palabra, cantidad in top_10:
                    categorias.append(palabra)
                    valores.append(cantidad)

                # Crear gráfica
                plt.bar(categorias, valores)

                # Título y etiquetas
                plt.title('Palabras Más Frecuentes')
                plt.xlabel('Palabras')
                plt.ylabel('Repeticiones')

                # Mostrar gráfica
                plt.show()
                
                

            #Histograma
            elif opcion == "4":
                import matplotlib.pyplot as plt
                import numpy as np

                with open(".\\RetoFinal\\Datos\\Operaciones.txt", "r", encoding="utf-8") as archivo:
                    lineas = archivo.readlines()

                # Datos
                data = [len(line.strip()) for line in lineas]

                # Crear el histograma
                plt.hist(data, bins=30, edgecolor='black')

                # Agregar título y etiquetas
                plt.title('Histograma')
                plt.xlabel('Caracteres')
                plt.ylabel('Lineas')

                # Mostrar la gráfica
                plt.show()
                
        
            # Atras
            elif opcion == "5":
                print("Regresando...")
                break

            else:
                print("Opción inválida.")
                


    # Datos Abiertos (.csv)
    elif opcion == "3":
        while True:
            print("\n=== Datos Abiertos (.csv) ===")
            print("1. Vista Previa de Datos")
            print("2. Cálculo de Estadísticas Descriptivas")
            print("3. Evolución Temporal / Tendencia")
            print("4. Comparación Categórica")
            print("5. Correlación de Variables")
            print("6. Regresar")

            opcion = input("Seleccione una opción: ")

            # Vista previa
            if opcion == "1":
                
                import csv
                with open(".\\RetoFinal\\Datos\\airports.csv  ", 'r', encoding="utf-8") as air:
                    lector = csv.reader(air, delimiter= ',')
                    encabezados = next(lector)
                    for fila in lector: 
                        print(fila)

                print(f"===== Las primeras 10 lineas de texto son las siguientes =====")
                print()
                with open(".\\RetoFinal\\Datos\\airports.csv", 'r', encoding="utf-8" ) as air:
                    for i in range(10):
                        contenidos = air.readline()
                        print(contenidos)
                    
                    print(f"================================================")
                
                print(f"===== Las ultimas 5 lineas de texto son las siguientes =====")
                print()
                with open(".\\RetoFinal\\Datos\\airports.csv", 'r', encoding="utf-8" ) as air:
                    for i in range(15,20):
                        contenidos = air.readline()
                        print(contenidos)
                
                    print(f"================================================")
                    

                        

            #Cálculo de Estadísticas Descriptivas
            elif opcion == "2":
                import csv
                with open(".\\RetoFinal\\Datos\\airports.csv", "r", encoding="utf-8") as archivo:
                    lector = csv.reader(archivo)

                    encabezados = next(lector)

                    print("\nColumnas disponibles:")
                    for i in range(len(encabezados)):
                        print(i, "-", encabezados[i])

                    columna = int(input("\nSeleccione la columna numérica: "))

                    valores = []

                    for fila in lector:

                        if columna < len(fila):

                            try:
                                valor = float(fila[columna])
                                valores.append(valor)
                            except:
                                pass


                total = len(valores)

                if total > 0:
                    
                    promedio = sum(valores) / total
                    minimo = valores[0]
                    maximo = valores[-1]

                    mid = total // 2

                    if total % 2 == 0:
                        mediana = (valores[mid - 1] + valores[mid]) / 2
                    else:
                        mediana = valores[mid]

                else:
                    promedio = 0
                    minimo = 0
                    maximo = 0
                    mediana = 0


                # RESULTADOS
                print("\n===== ESTADÍSTICAS =====")
                print("Registros válidos:", total)
                print("Promedio:", promedio)
                print("Mediana:", mediana)
                print("Máximo:", maximo)
                print("Mínimo:", minimo)


            #Evolución Temporal / Tendencia
            elif opcion == "3":
                import csv
                import matplotlib.pyplot as plt
                with open(".\\RetoFinal\\Datos\\airports.csv", "r", encoding="utf-8") as archivo:
                    lector = csv.reader(archivo)

                    encabezados = next(lector)

                    print("\nColumnas disponibles:")
                    for i in range(len(encabezados)):
                        print(i, "-", encabezados[i])

                    col_x = int(input("\nSeleccione la columna X: "))
                    col_y = int(input("Seleccione la columna Y : "))

                    x = []
                    y = []

                    for fila in lector:

                        if col_x < len(fila) and col_y < len(fila):

                            valor_x = fila[col_x]
                            valor_y = fila[col_y]

                            try:
                                y.append(float(valor_y))
                                x.append(valor_x)
                            except:
                                pass


                plt.plot(x, y)

                plt.title("Gráfico de líneas")
                plt.xlabel(encabezados[col_x])
                plt.ylabel(encabezados[col_y])

                plt.show()
    
            #Comparacion categorica
            elif opcion == "4":
                import csv
                import matplotlib.pyplot as plt
                from collections import Counter
                with open(".\\RetoFinal\\Datos\\airports.csv", "r", encoding="utf-8") as archivo:
                    lector = csv.reader(archivo)

                    encabezados = next(lector)

                    print("\nColumnas disponibles:")
                    for i in range(len(encabezados)):
                        print(i, "-", encabezados[i])

                    columna = int(input("\nSeleccione la columna categórica: "))

                    categorias = []

                    for fila in lector:

                        if columna < len(fila):
                            valor = fila[columna]

                            if valor != "":
                                categorias.append(valor)


                contador = Counter(categorias)

                labels = []
                values = []

                for item in contador:
                    labels.append(item)
                    values.append(contador[item])


                plt.pie(values, labels=labels, autopct="%1.1f%%")

                plt.title("Distribución de categorías")

                plt.show()
                

            #Correlación de Variables
            elif opcion == "5":
                import csv
                import matplotlib.pyplot as plt

                with open(".\\RetoFinal\\Datos\\airports.csv", "r", encoding="utf-8") as archivo:
                    lector = csv.reader(archivo)

                    encabezados = next(lector)

                    print("\nColumnas disponibles:")
                    for i in range(len(encabezados)):
                        print(i, "-", encabezados[i])

                    col_x = int(input("\nSeleccione la columna X (numérica): "))
                    col_y = int(input("Seleccione la columna Y (numérica): "))

                    x = []
                    y = []

                    for fila in lector:

                        if col_x < len(fila) and col_y < len(fila):

                            try:
                                valor_x = float(fila[col_x])
                                valor_y = float(fila[col_y])

                                x.append(valor_x)
                                y.append(valor_y)

                            except:
                                pass



                plt.scatter(x, y)

                plt.title("Gráfico de dispersión")
                plt.xlabel(encabezados[col_x])
                plt.ylabel(encabezados[col_y])

                plt.show()

            # Atras
            elif opcion == "6":
                print("Regresando...")
                break

            else:
                print("Opción inválida.")

    # SALIR
    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")

