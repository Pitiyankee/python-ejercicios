# Ejercicio 4 - Suma de números pares con while
n = int(input("Introduce un número entero positivo: "))

suma = 0
texto = ""
i = 2
while i <= n:
    suma = suma + i
    if texto == "":
        texto = str(i)
    else:
        texto = texto + " + " + str(i)
    i = i + 2

print(f"La suma de los números pares entre 1 y {n} es: {suma}")
print(f"{texto} = {suma}")
