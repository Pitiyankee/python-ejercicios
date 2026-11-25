# Ejercicio 4 - Menú de opciones con match-case
opcion = int(input("Elige una opción del 1 al 4: "))

match opcion:
    case 1:
        print("Café: 1.20€")
    case 2:
        print("Té: 1.10€")
    case 3:
        print("Zumo: 1.80€")
    case 4:
        print("Agua: 0.90€")
    case _:
        print("Opción no disponible")

# Segundo match, aquí uso el | para agrupar las opciones 1 y 2
match opcion:
    case 1 | 2:
        print("Bebida caliente/fría estándar")
