def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b


def restar(a, b):
    """Retorna la resta de dos números."""
    return a - b


def multiplicar(a, b):
    """Retorna la multiplicación de dos números."""
    return a * b


def dividir(a, b):
    """Retorna la división de dos números."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def main():
    print("Hola estudiantes del ITM")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    print(f"Suma: {sumar(a, b)}")
    print(f"Resta: {restar(a, b)}")
    print(f"Multiplicación: {multiplicar(a, b)}")
    try:
        print(f"División: {dividir(a, b)}")
    except ValueError as error:
        print(f"División: {error}")


if __name__ == "__main__":
    main()
