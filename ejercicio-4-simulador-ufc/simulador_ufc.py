# Simulador de matchmaking y registro UFC

# Cada peleador es un diccionario. (Récords aproximados, sacados de los rankings de la UFC)
peleadores = [
    {"nombre": "Islam Makhachev", "division": "Ligero", "victorias": 27, "derrotas": 1, "estilo": "Grappler"},
    {"nombre": "Ilia Topuria", "division": "Pluma", "victorias": 16, "derrotas": 0, "estilo": "Striker"},
    {"nombre": "Alex Pereira", "division": "Semipesado", "victorias": 13, "derrotas": 3, "estilo": "Striker"},
    {"nombre": "Jon Jones", "division": "Pesado", "victorias": 28, "derrotas": 1, "estilo": "Grappler"},
    {"nombre": "Max Holloway", "division": "Pluma", "victorias": 27, "derrotas": 8, "estilo": "Striker"},
    {"nombre": "Merab Dvalishvili", "division": "Gallo", "victorias": 20, "derrotas": 4, "estilo": "Grappler"},
]


def buscar(nombre):
    # Devuelve el peleador con ese nombre (sin mirar mayúsculas) o None si no existe
    for p in peleadores:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def porcentaje(p):
    total = p["victorias"] + p["derrotas"]
    if total == 0:
        return 0
    return p["victorias"] / total


def listar():
    print("\n--- LISTA DE PELEADORES ---")
    for p in peleadores:
        print(f"{p['nombre']} | {p['division']} | {p['estilo']} | Récord: {p['victorias']}-{p['derrotas']}")


def anadir():
    print("\n--- AÑADIR PELEADOR ---")
    nombre = input("Nombre: ").strip()
    if buscar(nombre) is not None:
        print("Error: ya existe un peleador con ese nombre.")
        return
    division = input("División de peso: ").strip()
    victorias = input("Victorias: ").strip()
    derrotas = input("Derrotas: ").strip()
    if not victorias.isdigit() or not derrotas.isdigit():
        print("Error: las victorias y las derrotas deben ser números enteros no negativos.")
        return
    estilo = input("Estilo (Striker o Grappler): ").strip().capitalize()
    if estilo != "Striker" and estilo != "Grappler":
        print("Error: el estilo solo puede ser Striker o Grappler.")
        return
    peleadores.append({
        "nombre": nombre,
        "division": division,
        "victorias": int(victorias),
        "derrotas": int(derrotas),
        "estilo": estilo,
    })
    print(f"{nombre} se ha añadido correctamente.")


def combate():
    print("\n--- SIMULAR COMBATE ---")
    a = buscar(input("Nombre del primer peleador: ").strip())
    b = buscar(input("Nombre del segundo peleador: ").strip())
    if a is None or b is None:
        print("Error: alguno de los dos peleadores no existe.")
        return
    if a is b:
        print("Error: has elegido dos veces al mismo peleador.")
        return

    if a["estilo"] != b["estilo"]:
        # Uno es Striker y el otro Grappler
        if a["estilo"] == "Grappler":
            grappler, striker = a, b
        else:
            grappler, striker = b, a
        if grappler["victorias"] > striker["victorias"]:
            ganador, perdedor, metodo = grappler, striker, "Sumisión"
        else:
            ganador, perdedor, metodo = striker, grappler, "KO"
    else:
        # Mismo estilo: gana el mejor porcentaje de victorias
        metodo = "Decisión unánime"
        if porcentaje(b) > porcentaje(a):
            ganador, perdedor = b, a
        else:
            ganador, perdedor = a, b  # si empatan gana el primero que se introdujo

    ganador["victorias"] += 1
    perdedor["derrotas"] += 1
    print(f"Ganador: {ganador['nombre']} por {metodo}")
    print(f"{ganador['nombre']}: {ganador['victorias']}-{ganador['derrotas']}")
    print(f"{perdedor['nombre']}: {perdedor['victorias']}-{perdedor['derrotas']}")


def filtrar():
    print("\n--- FILTRAR POR DIVISIÓN ---")
    division = input("División de peso: ").strip()
    encontrado = False
    for p in peleadores:
        if p["division"].lower() == division.lower():
            print(f"{p['nombre']} | {p['estilo']} | Récord: {p['victorias']}-{p['derrotas']}")
            encontrado = True
    if not encontrado:
        print("No hay peleadores en esa división.")


while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Listar peleadores")
    print("2. Añadir peleador")
    print("3. Simular combate")
    print("4. Filtrar por división")
    print("5. Salir")
    opcion = input("Elige una opción: ").strip()

    match opcion:
        case "1":
            listar()
        case "2":
            anadir()
        case "3":
            combate()
        case "4":
            filtrar()
        case "5":
            print("¡Hasta la próxima, matchmaker!")
            break
        case _:
            print("Opción no válida, inténtalo otra vez.")
