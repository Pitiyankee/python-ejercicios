archivo = open("resumen_notas.txt", "r", encoding="utf-8")
informe = archivo.read()
archivo.close()

print(informe)
