import subprocess

# Abre el archivo diccionario
with open("diccionario", "r") as diccionario:
    # Itera sobre cada línea (posible frase de paso)
    for contraseña in diccionario:
        contraseña = contraseña.strip()  # Elimina espacios en blanco y saltos de línea

        # Comando para desencriptar usando gpg y la frase de paso
        result = subprocess.run(
            ["gpg", "--decrypt", "--batch", "--yes", "--passphrase-fd", "0", "flag.txt.gpg"],
            input=contraseña.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Muestra la salida o error
        if result.returncode == 0:
            print(f"Frase de paso encontrada: {contraseña}")
            print(result.stdout.decode())  # Muestra el contenido desencriptado
            break  # Detiene el bucle si la desencriptación es exitosa
        else:
            print(f"Frase de paso incorrecta: {contraseña}")