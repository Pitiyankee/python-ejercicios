# Ejercicio 7 - Altura alcanzada por una rampa
import math

longitud = float(input("Longitud de la rampa (m): "))
angulo = float(input("Ángulo con el suelo (entre 0 y 90 grados): "))

radianes = math.radians(angulo)
altura = longitud * math.sin(radianes)

print(f"Altura alcanzada: {altura:.2f} m")
