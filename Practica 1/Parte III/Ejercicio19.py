import subprocess

correctos = []
# Itera sobre cada línea (posible frase de paso)
for i in range(200):
    
    # Comando para desencriptar usando gpg y la frase de paso
    result = subprocess.run(
        ["gpg", "--decrypt", f"firmas/{i}.asc"],
    )

    # Muestra la salida o error
    if result.returncode == 0:
        correctos.append(i)


print(correctos)