alumnos = [
    "Pedro Efraín José Bandes Durán",
    "Javier Blas Velasco",
    "Jorge Caballero Diez",
    "Rodrigo Cuesta Cáceres",
    "Nicolás Escolano García",
    "Héctor Junior Farfan Pacheco",
    "Fabricio del Piero García López",
    "Gustavo Izaguirre Serna",
    "Juan Pablo Lima Albornoz",
    "David López Ruíz",
    "Aitor Mateos Gamazo",
    "Pablo Acedo Lucas",
    "Carlos Augusto Zuleta Zapata",
]

# encoding utf-8 para conservar tildes y la ñ
archivo = open("alumnos.txt", "w", encoding="utf-8")

i = 0
while i < len(alumnos):
    archivo.write(alumnos[i] + "\n")
    i += 1

archivo.close()

print(f"Se han guardado {len(alumnos)} estudiantes en alumnos.txt")
