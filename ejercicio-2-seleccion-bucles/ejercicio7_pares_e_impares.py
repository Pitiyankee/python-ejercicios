# Ejercicio 7 - Pares, impares y múltiplos de 5 (for y continue)
for n in range(1, 51):
    if n % 5 == 0:
        print(n, "→ múltiplo de 5")
    elif n % 2 != 0:
        continue
    else:
        print(n, "→ par")
