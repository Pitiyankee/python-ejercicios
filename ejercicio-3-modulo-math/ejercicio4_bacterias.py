# Ejercicio 4 - Crecimiento de una población de bacterias
import math

inicial = int(input("Número inicial de bacterias: "))
horas = int(input("Número de horas transcurridas: "))

final = inicial * math.pow(2, horas)

print(f"Población final: {final:.0f} bacterias")
