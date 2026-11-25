def leer_votos(partido):
    while True:
        texto = input(f"Votos de {partido}: ").strip()
        if texto.isdigit():
            return int(texto)
        print("Dato no válido: introduce un número entero no negativo.")


opciones = ["Coalición Canaria", "Nueva Canarias"]

archivo = open("votacion.txt", "w", encoding="utf-8")
i = 0
while i < len(opciones):
    votos = leer_votos(opciones[i])
    archivo.write(f"{opciones[i]};{votos}\n")
    i += 1
archivo.close()

print("Votos guardados en votacion.txt")
