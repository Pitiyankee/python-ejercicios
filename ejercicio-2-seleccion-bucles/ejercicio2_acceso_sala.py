# Ejercicio 2 - Acceso a una sala (condiciones anidadas)
edad = int(input("Introduce tu edad: "))
respuesta = input("¿Estás registrado? (si/no): ")
registrado = respuesta.lower() == "si"

if edad >= 16:
    if registrado:
        print("Acceso permitido")
    else:
        print("Acceso denegado: falta registro")
else:
    print("Acceso denegado: edad insuficiente")
