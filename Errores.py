def main():
    try:
        num_str = input("Introduce un número: ")
        num = int(num_str)  # Convertir el valor ingresado a entero

        if num == 0:
            raise ValueError("¡Error! No puedes dividir entre cero.")

        resultado = 10 / num
        print(f"El resultado de la división es: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("¡Error! No puedes dividir entre cero.")
    finally:
        print("Fin del proceso")


if __name__ == "__main__":
    main()
