def leer_nota(nombre):
    while True:
        texto = input(f"Nota de {nombre} (0-10): ").strip().replace(",", ".")
        try:
            nota = float(texto)
        except ValueError:
            print("Dato no válido: introduce un número (por ejemplo 7.5 o 7,5).")
            continue
        if 0 <= nota <= 10:
            return nota
        print("La nota debe estar entre 0 y 10.")


archivo = open("alumnos.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()

nombres = contenido.splitlines()

salida = open("notas.txt", "w", encoding="utf-8")
i = 0
while i < len(nombres):
    if nombres[i].strip() != "":
        nota = leer_nota(nombres[i])
        salida.write(f"{nombres[i]};{nota}\n")
    i += 1
salida.close()

print("Notas guardadas en notas.txt")
