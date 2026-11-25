archivo = open("notas.txt", "r", encoding="utf-8")
registros = archivo.read().splitlines()
archivo.close()

print("NOTAS DEL EXAMEN")
i = 0
while i < len(registros):
    if registros[i].strip() != "":
        nombre, nota = registros[i].split(";")
        print(f"{nombre}: {nota}")
    i += 1
