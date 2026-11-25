# Ejercicio 2 - Autobuses para una excursión
import math

participantes = int(input("Número de participantes: "))
plazas = int(input("Plazas de cada autobús: "))

autobuses = math.ceil(participantes / plazas)

print(f"Autobuses necesarios: {autobuses}")
