# Ejercicio 8 - Tablas de multiplicar con bucles anidados y enumerate
numeros = [3, 6, 9]

for indice, numero in enumerate(numeros):
    print(f"Posición {indice} → Tabla del {numero}:")
    for i in range(1, 6):
        print(f"{numero} x {i} = {numero * i}")
    print()
