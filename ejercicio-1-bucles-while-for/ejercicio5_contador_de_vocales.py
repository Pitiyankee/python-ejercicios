# Ejercicio 5 - Contador de vocales con for
frase = input("Introduce una frase: ")

vocales = "aeiouáéíóúü"
contador = 0
for letra in frase.lower():
    if letra in vocales:
        contador = contador + 1

print(f"El texto contiene {contador} vocales.")
