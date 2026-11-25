# Ejercicio 5 - Validación de contraseña con while
contrasena = input("Introduce una contraseña: ")

while len(contrasena) < 6:
    print("Contraseña demasiado corta, inténtalo de nuevo")
    contrasena = input("Introduce una contraseña: ")

print("Contraseña aceptada")
