# Ejercicio 1 - Clasificador de IMC
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / altura ** 2

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Tu IMC es {imc:.2f} -> {categoria}")
