# Ejercicio 3 - Cajas completas en un almacén
import math

total = float(input("Cantidad total de producto (kg): "))
capacidad = float(input("Capacidad de cada caja (kg): "))

cajas = math.floor(total / capacidad)
envasado = cajas * capacidad
sobrante = total - envasado

print(f"Cajas completas: {cajas}")
print(f"Producto sobrante: {sobrante:.2f} kg")
