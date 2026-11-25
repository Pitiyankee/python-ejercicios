def crear_resumen(contenido):
    registros = contenido.splitlines()

    total = 0
    suma = 0.0
    aprobados = 0
    suspensos = 0

    i = 0
    while i < len(registros):
        if registros[i].strip() != "":
            nota = float(registros[i].split(";")[1])
            total += 1
            suma += nota
            if nota >= 5:
                aprobados += 1
            else:
                suspensos += 1
        i += 1

    if total == 0:
        return "No existen notas disponibles."

    media = suma / total
    return (
        "RESUMEN DEL CURSO\n"
        f"Número de estudiantes: {total}\n"
        f"Nota media: {media:.2f}\n"
        f"Aprobados: {aprobados}\n"
        f"Suspensos: {suspensos}\n"
    )


archivo = open("notas.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()

resumen = crear_resumen(contenido)

salida = open("resumen_notas.txt", "w", encoding="utf-8")
salida.write(resumen)
salida.close()

print("Resumen guardado en resumen_notas.txt")
