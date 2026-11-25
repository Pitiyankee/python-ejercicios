# Ejercicio 3 - Tabla de multiplicar con for
numero = int(input("Introduce un número: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
