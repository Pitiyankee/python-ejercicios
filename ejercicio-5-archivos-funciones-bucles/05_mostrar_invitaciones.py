archivo = open("invitaciones.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()

print(contenido)
