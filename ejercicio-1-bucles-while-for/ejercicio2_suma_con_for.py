# Ejercicio 2 - Suma de números con for
numero = int(input("Introduce un número entero positivo: "))

suma = 0
texto = ""
for i in range(1, numero + 1):
    suma = suma + i
    texto = texto + str(i)
    if i < numero:
        texto = texto + " + "

print(f"La suma de los números desde 1 hasta {numero} es: {suma}")
print(f"{texto} = {suma}")
