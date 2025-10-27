# Autor: Alfonso Luque Sánchez
# Ejercicio 2
"""
Biblioteca de funciones numericas
"""

def digits(n):
    """Devuelve el número de dígitos de un número entero."""
    if n == 0:
        return 1
    n = abs(n)
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def reverse(n):
    """Devuelve el número al revés."""
    neg = n < 0
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return -rev if neg else rev


def is_palindromic(n):
    """Devuelve True si el número es capicúa."""
    return n == reverse(n)


def is_prime(n):
    """Devuelve True si el número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    """Devuelve el menor número primo mayor que n."""
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def digit_n(n, pos):
    """Devuelve el dígito en la posición 'pos' (de izquierda a derecha)."""
    n = abs(n)
    num_digits = digits(n)
    if pos < 0 or pos >= num_digits:
        return -1  # fuera de rango
    divisor = 10 ** (num_digits - pos - 1)
    return (n // divisor) % 10


def digit_position(n, digit):
    """Devuelve la posición de la primera ocurrencia de un dígito (de izquierda a derecha)."""
    n = abs(n)
    num_digits = digits(n)
    for i in range(num_digits):
        if digit_n(n, i) == digit:
            return i
    return -1


def remove_behind(n, count):
    """Elimina 'count' dígitos por detrás (por la derecha)."""
    return n // (10 ** count)


def remove_ahead(n, count):
    """Elimina 'count' dígitos por delante (por la izquierda)."""
    num_digits = digits(n)
    return n % (10 ** (num_digits - count))


def paste_behind(n, digit):
    """Añade un dígito por detrás."""
    return n * 10 + digit


def paste_ahead(n, digit):
    """Añade un dígito por delante."""
    num_digits = digits(n)
    return digit * (10 ** num_digits) + n


def piece_of_number(n, start, end):
    """Devuelve el trozo del número entre las posiciones 'start' y 'end' (inclusive)."""
    num_digits = digits(n)
    if start < 0 or end >= num_digits or start > end:
        return -1
    n = remove_behind(n, num_digits - end - 1)
    n = remove_ahead(n, start)
    return n


def concatenate(n1, n2):
    """Pega dos números para formar uno."""
    return n1 * (10 ** digits(n2)) + n2



def main():
    print("Pruebas de funciones numéricas:\n")

    print("digits(12345) =", digits(12345))
    print("reverse(1234) =", reverse(1234))
    print("is_palindromic(1221) =", is_palindromic(1221))
    print("is_prime(7) =", is_prime(7))
    print("next_prime(10) =", next_prime(10))
    print("digit_n(98765, 2) =", digit_n(98765, 2))
    print("digit_position(987654, 7) =", digit_position(987654, 7))
    print("remove_behind(12345, 2) =", remove_behind(12345, 2))
    print("remove_ahead(12345, 2) =", remove_ahead(12345, 2))
    print("paste_behind(123, 4) =", paste_behind(123, 4))
    print("paste_ahead(123, 9) =", paste_ahead(123, 9))
    print("piece_of_number(987654, 1, 3) =", piece_of_number(987654, 1, 3))
    print("concatenate(123, 456) =", concatenate(123, 456))


main()