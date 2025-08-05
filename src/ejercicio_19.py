frase = "programacion es divertida"
contador = 0
for letra in frase:
    if letra.lower() in "aeiou":
        contador += 1
print("Cantidad de vocales:", contador)