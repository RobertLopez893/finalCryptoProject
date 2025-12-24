# Final Project: Toy-Block Cipher
# By: López Reyes José Roberto
#     Hernández Zamora Alejandro
# Group: 6CV4

from Crypto.Util.number import getPrime, GCD, inverse
import random


# RSA Key Generation
def generar_llaves_rsa():
    # Generar p y q
    p = getPrime(64)
    q = getPrime(64)

    while p == q:
        q = getPrime(64)

    # Calcular n y φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Elegir e aleatorio válido
    while True:
        e = random.randrange(2, phi)
        # Verificaciones
        if GCD(e, phi) == 1 and e != 3 and e != 65537 and e % 2 != 0:
            break

    # Calcular d (inverso modular de e)
    d = inverse(e, phi)

    # Mostrar llaves en consola
    print(f"\nLlave pública (e, n):")
    print(f"e = {e}")
    print(f"n = {n}")
    print(f"({e}, {n})\n")

    print("Llave privada (d):")
    print(f"d = {d}")

    archivo = input("\nIngresa el nombre del archivo para guardar tus llaves: ")

    try:
        with open(archivo, "w") as f:
            f.write("--- LLAVE PUBLICA ---\n")
            f.write(f"e = {e}\n")
            f.write(f"n = {n}\n")
            f.write("\n--- LLAVE PRIVADA ---\n")
            f.write(f"d = {d}\n")
        print(f"\nLas llaves se han guardado en el archivo '{archivo}'")
    except IOError:
        print("[ERROR] No se pudo crear el archivo de llaves.")


# RSA Cipher
def cifrar_rsa():
    print("\n--- Cifrado RSA ---\n")

    # Pedir llave pública (e, n)
    try:
        print("Ingrese la llave pública:")
        e = int(input("Valor de e: "))
        n = int(input("Valor de n: "))

        # Pedir el nombre del archivo con la llave
        archivo_k = input("Ingrese el nombre del archivo con la llave a cifrar: ")
    except ValueError:
        print("Error: Datos inválidos.")
        return

    try:
        with open(archivo_k, "r") as f:
            hex_content = f.read().strip()

        # Hexadecimal a decimal
        r = int(hex_content, 16)

        print(f"\nLlave leída (HEX): {hex_content}")
        print(f"Llave convertida (INT): {r}")
    except IOError:
        print("No se pudo abrir el archivo de la llave.")
        return

    # Cifrar
    c = pow(r, e, n)

    print(f"Texto cifrado (c): {c}")

    archivo = input("\nIngresa el nombre del archivo para guardar tu llave cifrada: ")

    # Guardar en archivo
    try:
        with open(archivo, "w") as f:
            f.write(str(c))
        print(f"El valor de 'c' se ha guardado en '{archivo}'.")
    except IOError:
        print("Error al escribir el archivo.")


# RSA Decipher
def descifrar_rsa():
    print("\n--- Descifrado RSA ---\n")

    # Pedir llave privada (d, n)
    try:
        print("Ingrese la llave privada:")
        d = int(input("Valor de d: "))
        n = int(input("Valor de n: "))

        # Pedir el nombre del archivo con la llave
        archivo_k = input("Ingrese el nombre del archivo con la llave a descifrar: ")

        # Abrimos el archivo de la llave cifrada
        with open(archivo_k, "r") as f:
            c = int(f.read().strip())
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return

    # Descifrar
    m = pow(c, d, n)
    print(f"\nLlave recuperada (INT): {m}")

    # Convertimos a hexadecimal
    m_hex = hex(m)[2:].upper()
    print(f"Llave recuperada (HEX): {m_hex}")

    archivo = input("\nIngresa el nombre del archivo para guardar tu llave recuperada: ")

    with open(archivo, "w") as f:
        f.write(m_hex)


def main():
    while True:
        opc = int(input("\nSelecciona la opción, pulsa cualquier otro número para salir:"
                        "\n1. Generar par de llaves RSA\n2. Cifrar RSA\n3. Descifrar RSA\n"))

        if opc == 1:
            generar_llaves_rsa()
            break
        elif opc == 2:
            cifrar_rsa()
            break
        elif opc == 3:
            descifrar_rsa()
            break
        else:
            break


if __name__ == "__main__":
    main()
