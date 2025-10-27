# Autor: Alfonso Luque Sánchez
# Punto 2 del Ejercicio 1
"""
Programa para que si no se introducen las dos variables desde la opcion  correspondiente no se pueden ejecutar el resto de las opciones.
"""

def sumar(a, b):
    print("El resultado de la suma es:", a + b)

def restar(a, b):
    print("El resultado de la resta es:", a - b)

def multiplicar(a, b):
    print("El resultado de la multiplicación es:", a * b)

def dividir(a, b):
    if b != 0:
        print("El resultado de la división es:", a / b)
    else:
        print("Error: No se puede dividir entre cero.")

# Programa principal
a = 0
b = 0
values_set = False

while True:
    print("\nMenú de opciones:")
    print("1. Introducir valores")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Salir")

    opcion = input("Elige una opción (1-6): ")

    if opcion == "1":
        a = float(input("Introduce el primer valor: "))
        b = float(input("Introduce el segundo valor: "))
        values_set = True
    elif opcion in ["2", "3", "4", "5"] and not values_set:
        print("Error: Debes introducir los valores primero (opción 1).")
    elif opcion == "2":
        sumar(a, b)
    elif opcion == "3":
        restar(a, b)
    elif opcion == "4":
        multiplicar(a, b)
    elif opcion == "5":
        dividir(a, b)
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción incorrecta. Por favor, elige una opción válida.")
