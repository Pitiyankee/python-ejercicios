def mostrar_menu():
    print("\nMENÚ DE SIMULACIONES FICTICIAS")
    print("1. Escenario ferroviario")
    print("2. Escenario aéreo")
    print("3. Escenario sanitario")
    print("4. Escenario nuclear")
    print('5. Analizar una afirmación de "falsa bandera"')
    print("0. Salir")


def escenario(titulo, situacion, pasos):
    print(f"\n--- {titulo} (simulación ficticia) ---")
    print(situacion)
    print("Protocolo de respuesta:")
    i = 0
    while i < len(pasos):
        print(f"  {i + 1}. {pasos[i]}")
        i += 1


def analizar_afirmacion():
    afirmacion = input("\nEscribe la afirmación a analizar: ").strip()
    if afirmacion == "":
        print("No has escrito ninguna afirmación.")
        return
    print(f'\nAfirmación: "{afirmacion}"')
    print("Preguntas para analizarla con espíritu crítico:")
    preguntas = [
        "¿Quién la hace y qué interés tiene en que la creas?",
        "¿Cita fuentes verificables y independientes?",
        "¿Hay pruebas o solo se basa en sospechas?",
        "¿Explica los hechos de forma más simple que otras hipótesis?",
        "¿La han confirmado medios o instituciones fiables?",
    ]
    i = 0
    while i < len(preguntas):
        print(f"  {i + 1}. {preguntas[i]}")
        i += 1
    print('Una acusación de "falsa bandera" requiere pruebas extraordinarias.')


opcion = ""
while opcion != "0":
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        escenario(
            "Escenario ferroviario",
            "Un tren de cercanías se detiene entre dos estaciones por una avería eléctrica.",
            ["Avisar al centro de control", "Informar a los pasajeros",
             "Asegurar la vía", "Evacuar o remolcar el tren"],
        )
    elif opcion == "2":
        escenario(
            "Escenario aéreo",
            "Un vuelo debe desviarse a otro aeropuerto por mal tiempo.",
            ["Comunicar la desviación a control aéreo", "Calcular el combustible",
             "Informar a los pasajeros", "Aterrizar en el aeropuerto alternativo"],
        )
    elif opcion == "3":
        escenario(
            "Escenario sanitario",
            "Un hospital recibe muchos pacientes a la vez tras un accidente de autobús.",
            ["Activar el plan de emergencia", "Clasificar a los pacientes (triaje)",
             "Reasignar personal y camas", "Informar a las familias"],
        )
    elif opcion == "4":
        escenario(
            "Escenario nuclear",
            "Una central nuclear ficticia detecta un fallo en el sistema de refrigeración.",
            ["Activar los sistemas de seguridad redundantes", "Reducir la potencia del reactor",
             "Notificar al organismo regulador", "Informar a la población con datos oficiales"],
        )
    elif opcion == "5":
        analizar_afirmacion()
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta pronto!")
    else:
        print("Opción no válida, elige un número del 0 al 5.")
