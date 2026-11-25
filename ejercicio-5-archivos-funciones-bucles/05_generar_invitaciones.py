def crear_invitacion(nombre, fecha, lugar):
    return (
        f"Querido/a {nombre},\n"
        f"Te invitamos a la fiesta de fin de curso el {fecha}.\n"
        f"Lugar: {lugar}.\n"
        "¡Te esperamos!\n"
    )


invitados = ["Jensen Huang", "Alice Huang", "Linus Torvalds"]
fecha = "19 de junio de 2026 a las 20:00"
lugar = "Sala Polivalente del centro"

archivo = open("invitaciones.txt", "w", encoding="utf-8")

i = 0
while i < len(invitados):
    archivo.write(crear_invitacion(invitados[i], fecha, lugar))
    archivo.write("\n" + "=" * 40 + "\n\n")
    i += 1

archivo.close()

print(f"Se han creado {len(invitados)} invitaciones en invitaciones.txt")
