try: 
    valor = int(input("ingrese un valor numerico: "))

except ValueError:  #si se quita el ValueErrorse el reconoce  ualquier error que haya
    print("El valor ingresado no es un numero.")
else:
    resultado = valor / 10
    print(f"Resultado = {resultado}")
finally:
    print("Proceso ejecutado! ")

