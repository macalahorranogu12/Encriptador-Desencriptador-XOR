import random

def generar_llave(longitud):
    return ''.join(str(random.randint(0, 1)) for _ in range(longitud))

def xor_cifrar(texto, llave):
    return ''.join(chr(ord(c) ^ int(llave[i % len(llave)])) for i, c in enumerate(texto))


texto = input("Ingresa el texto: ")
llave = generar_llave(len(texto))
cifrado = xor_cifrar(texto, llave)
descifrado = xor_cifrar(cifrado, llave)

print("Llave generada:", llave)
print("Texto cifrado:", cifrado)
print("Texto descifrado:", descifrado)