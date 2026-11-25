# Ejercicio 6 - Menú interactivo con while True
total = 0

while True:
    opcion = input('Opciones: "sumar", "restar", "salir": ')

    if opcion == "sumar":
        numero = float(input("Número a sumar: "))
        total = total + numero
    elif opcion == "restar":
        numero = float(input("Número a restar: "))
        total = total - numero
    elif opcion == "salir":
        print(f"Total final: {total}")
        break
    else:
        print("Opción no reconocida")
