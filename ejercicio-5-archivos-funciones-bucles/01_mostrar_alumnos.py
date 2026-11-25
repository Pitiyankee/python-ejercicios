archivo = open("alumnos.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()

print("LISTADO DE ALUMNOS")
print(contenido)
