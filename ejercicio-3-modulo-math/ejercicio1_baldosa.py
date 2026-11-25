# Ejercicio 1 - El lado de una baldosa cuadrada
import math

area = float(input("Área de la baldosa (cm²): "))

lado = math.sqrt(area)
perimetro = 4 * lado

print(f"Lado de la baldosa: {lado:.2f} cm")
print(f"Perímetro de la baldosa: {perimetro:.2f} cm")
