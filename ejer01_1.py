# Ejercicio 1.1: Calculadora básica con funciones y menú
# Autor: Alfonso Luque Sánchez

"""
Programa que pide dos valores y a continuación muestra un menú con las siguientes opciones:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
Si se introduce una opción incorrecta, se mostrará un mensaje de error.
El programa se repetirá a menos que se elija la opción de salir.
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

a = 0
b = 0

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
