# Ejercicio 6 - Números primos hasta un límite con for anidado
n = int(input("Introduce un número entero mayor o igual que 2: "))

print(f"Los números primos entre 2 y {n} son:")
primos = ""
for numero in range(2, n + 1):
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
    if es_primo:
        primos = primos + str(numero) + " "

print(primos)
