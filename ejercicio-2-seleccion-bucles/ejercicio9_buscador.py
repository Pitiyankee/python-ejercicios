# Ejercicio 9 - Buscador con break y pass
nombres = ["Fabián", "Elam", "Kang-in Lee", "Mohamed", "Mauri"]
buscado = input("Introduce el nombre a buscar: ")

for indice, nombre in enumerate(nombres):
    if nombre.lower() == buscado.lower():
        print(f"Encontrado en la posición {indice}")
        break
    else:
        pass
else:
    print("Nombre no encontrado")
