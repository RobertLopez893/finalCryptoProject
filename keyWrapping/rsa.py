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
        # Verificamos requisitos del PDF: gcd(e, phi)=1, e!=3, e!=65537, e impar
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
    print("\n--- Cifrado RSA (Raw) ---\n")

    # Pedir llave pública (e, n)
    try:
        print("Ingrese la llave pública:")
        e = int(input("Valor de e: "))
        n = int(input("Valor de n: "))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return

    # Generar número aleatorio r de 32 bits
    r = random.getrandbits(32)
    print(f"\nMensaje aleatorio generado (r): {r}")

    # Cifrar
    c = pow(r, e, n)

    print(f"Texto cifrado (c): {c}")

    # Guardar en archivo
    try:
        with open("rsa_cipher.txt", "w") as f:
            f.write(str(c))
        print("El valor de 'c' se ha guardado en 'rsa_cipher.txt'.")
    except IOError:
        print("Error al escribir el archivo.")


# RSA Decipher
def descifrar_rsa():
    print("\n--- Descifrado RSA (Raw) ---\n")

    # Pedir llave privada (d, n)
    try:
        print("Ingrese la llave privada:")
        d = int(input("Valor de d: "))
        n = int(input("Valor de n: "))

        # Pedir el valor de c
        c = int(input("Ingrese el valor del texto cifrado (c): "))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return

    # Descifrar
    m = pow(c, d, n)

    print(f"\nMensaje descifrado (m): {m}")
    print("-" * 60)


def main():
    while True:
        opc = int(input("\nSelecciona la opción, pulsa cualquier otro número para salir:"
                        "\n1. Generar par de llaves RSA\n2. Cifrar RSA\n3. Descifrar RSA\n"))

        if opc == 1:
            generar_llaves_rsa()
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
