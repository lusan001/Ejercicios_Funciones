# Ejercicio 1: Calculadora básica con funciones y menú
# Autor: Alfonso Luque Sánchez

def menu(opciones):
    while True:
        print("\nMenú:")
        for i, opc in enumerate(opciones, 1):
            print(f"{i}. {opc}")
        try:
            elec = int(input("Elige una opción (número): "))
            if 1 <= elec <= len(opciones):
                return elec
            print("Opción incorrecta. Introduce un número válido.")
        except ValueError:
            print("Entrada no válida. Introduce un número.")

def introducir_variables():
    while True:
        try:
            a = float(input("Introduce a: "))
            b = float(input("Introduce b: "))
            print(f"Variables introducidas: a = {a}, b = {b}")
            return a, b
        except ValueError:
            print("Entrada no válida. Introduce números.")

def sumar(a, b):
    print(f"Resultado de {a} + {b} = {a + b}")

def restar(a, b):
    print(f"Resultado de {a} - {b} = {a - b}")

def multiplicar(a, b):
    print(f"Resultado de {a} * {b} = {a * b}")

def dividir(a, b):
    if b == 0:
        print("Error: división por cero.")
    else:
        print(f"Resultado de {a} / {b} = {a / b}")

def main():
    opciones = [
        "Introducir variables",
        "Sumar",
        "Restar",
        "Multiplicar",
        "Dividir",
        "Terminar"
    ]
    a, b = 0.0, 0.0
    variables_introducidas = False

    while True:
        elec = menu(opciones)

        if elec == 1:
            a, b = introducir_variables()
            variables_introducidas = True
        elif elec == 2:
            if not variables_introducidas:
                print("Primero debes introducir las variables (opción 1).")
            else:
                sumar(a, b)
        elif elec == 3:
            if not variables_introducidas:
                print("Primero debes introducir las variables (opción 1).")
            else:
                restar(a, b)
        elif elec == 4:
            if not variables_introducidas:
                print("Primero debes introducir las variables (opción 1).")
            else:
                multiplicar(a, b)
        elif elec == 5:
            if not variables_introducidas:
                print("Primero debes introducir las variables (opción 1).")
            else:
                dividir(a, b)
        elif elec == 6:
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()