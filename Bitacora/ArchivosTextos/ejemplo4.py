# Forma antigua
f = open("datos.txt", "r")
contenido = f.read()
f.close()

# Forma moderna (Recomendada)
with open("datos.txt", "r") as f:
    contenido = f.read()
# ¡Ya está cerrado automáticamente aquí!