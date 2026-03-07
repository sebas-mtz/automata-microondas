def reemplazar_11_por_00(cadena: str) -> str:
    salida = []
    i = 0

    while i < len(cadena):
        if i < len(cadena) - 1 and cadena[i] == '1' and cadena[i + 1] == '1':
            salida.append('00')
            i += 2
        else:
            salida.append(cadena[i])
            i += 1

    return ''.join(salida)


def main() -> None:
    entrada = input("Ingresa una secuencia de 0 y 1: ").strip()

    if all(c in "01" for c in entrada) and entrada:
        resultado = reemplazar_11_por_00(entrada)
        print("Secuencia de entrada:", entrada)
        print("Secuencia de salida :", resultado)
    else:
        print("Error: solo se permiten cadenas no vacías formadas por 0 y 1.")


if __name__ == "__main__":
    main()
