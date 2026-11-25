archivo = open("votacion.txt", "r", encoding="utf-8")
registros = archivo.read().splitlines()
archivo.close()

nombres = []
votos = []
i = 0
while i < len(registros):
    if registros[i].strip() != "":
        nombre, cantidad = registros[i].split(";")
        nombres.append(nombre)
        votos.append(int(cantidad))
    i += 1

total = sum(votos)
print("RESULTADOS DE LA VOTACIÓN")
print(f"Total de votos: {total}")

if total == 0:
    print("No se han registrado votos, no se pueden calcular porcentajes.")
else:
    i = 0
    while i < len(nombres):
        porcentaje = votos[i] / total * 100
        print(f"{nombres[i]}: {votos[i]} votos ({porcentaje:.2f}%)")
        i += 1

    maximo = max(votos)
    ganadores = [nombres[j] for j in range(len(nombres)) if votos[j] == maximo]
    if len(ganadores) > 1:
        print("Hay empate entre: " + " y ".join(ganadores))
    else:
        print(f"La opción con más votos es: {ganadores[0]}")
