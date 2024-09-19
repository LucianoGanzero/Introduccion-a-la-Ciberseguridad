import subprocess

# Abre el archivo diccionario
with open("rockyou.txt", "r") as diccionario:
    # Itera sobre cada línea (posible frase de paso)
    for contraseña in diccionario:
        contraseña = contraseña.strip()  # Elimina espacios en blanco y saltos de línea
        contraseña = f"pass:{contraseña}"
        # Comando para desencriptar usando keepassxc-cli y la frase de paso
        result = subprocess.run(
            ["openssl", "pkeyutl", "-decrypt", "-passin", "-inkey", "private.pem", "-in", "encrypted.txt", "-out", "archivo_descifrado.txt"],
            input=contraseña.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )   

        # Muestra la salida o error
        if "Error" not in result.stderr.decode() and result.stderr.decode().strip() == "":
            print(f"Frase de paso encontrada: {contraseña}")
            print(result.stdout.decode())  # Muestra el contenido desencriptado (si es aplicable)
            break  # Detiene el bucle si la desencriptación es exitosa
        else:
            print(f"Frase de paso incorrecta: {contraseña}")