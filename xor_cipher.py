import random

def generar_llave(longitud):
    return ''.join(str(random.randint(0, 1)) for _ in range(longitud))

def xor_cifrar(texto, llave):
    cifrado = []
    for i in range(len(texto)):
        llave_int = int(llave[i % len(llave)])
        cifrado_char = chr(ord(texto[i]) ^ llave_int)
        cifrado.append(cifrado_char)
    return ''.join(cifrado)

texto = input("Ingresa el texto: ")
llave = generar_llave(len(texto))
cifrado = xor_cifrar(texto, llave)
descifrado = xor_cifrar(cifrado, llave)

print("Llave generada:", llave)
print("Texto cifrado:", cifrado)
print("Texto descifrado:", descifrado)
