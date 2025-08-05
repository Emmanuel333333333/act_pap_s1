contador = 0
palabra = input("Escribe una palabra ('fin' para terminar): ")
while palabra != "fin":
    contador += 1
    palabra = input("Escribe otra palabra ('fin' para terminar): ")
print("Cantidad de palabras ingresadas:", contador)