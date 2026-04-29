try:
    with open("archivo_que_no_existe.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: Estás intentando abrir un archivo que no existe.")