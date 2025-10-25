# Ejercicio 1: Calculadora básica con funciones y menú
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

def show_menu():
    print("\nMenú de opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    while True:
        show_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            print(f"La suma es: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"La resta es: {restar(num1, num2)}")
        elif opcion == '3':
            print(f"La multiplicación es: {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"La división es: {dividir(num1, num2)}")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción incorrecta. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()