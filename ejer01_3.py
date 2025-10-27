# Autor: Alfonso Luque Sánchez
# Punto 3 del Ejercicio 1
"""
Funcion para gestionar menus: recibe una lista de opciones, las muestra numeradas,
pide una opcion (por su número) y devuelve la opcion escogida.
"""


# Función para mostrar un menú y devolver la opción elegida
def mostrar_menu(opciones):
    print("\nMenú de opciones:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

    while True:
        eleccion = input("Elige una opción (1-" + str(len(opciones)) + "): ")
        if eleccion.isdigit():  # comprobamos que sea un número
            eleccion = int(eleccion)
            if 1 <= eleccion <= len(opciones):
                return eleccion
            else:
                print("Opción fuera de rango. Intenta de nuevo.")
        else:
            print("Debes escribir un número válido.")


# Funciones para operaciones matemáticas
def sumar(a, b):
    print("Resultado:", a + b)


def restar(a, b):
    print("Resultado:", a - b)


def multiplicar(a, b):
    print("Resultado:", a * b)


def dividir(a, b):
    if b == 0:
        print("Error: no se puede dividir entre cero.")
    else:
        print("Resultado:", a / b)


# Programa principal
def main():
    a = 0
    b = 0
    valores_introducidos = False  # Para saber si ya se introdujeron los valores

    opciones = [
        "Introducir valores",
        "Sumar",
        "Restar",
        "Multiplicar",
        "Dividir",
        "Terminar"
    ]

    while True:
        opcion = mostrar_menu(opciones)

        if opcion == 1:
            # Pedir los valores
            while True:
                try:
                    a = float(input("Introduce el valor de a: "))
                    b = float(input("Introduce el valor de b: "))
                    valores_introducidos = True
                    break
                except ValueError:
                    print("Error: debes introducir números válidos.")

        elif opcion in (2, 3, 4, 5):
            if not valores_introducidos:
                print("Primero debes introducir los valores desde la opción 1.")
            else:
                if opcion == 2:
                    sumar(a, b)
                elif opcion == 3:
                    restar(a, b)
                elif opcion == 4:
                    multiplicar(a, b)
                elif opcion == 5:
                    dividir(a, b)

        elif opcion == 6:
            print("Fin del programa.")
            break


# Llamamos a la función principal
main()