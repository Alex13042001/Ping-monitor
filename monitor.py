import platform
import subprocess
import re

# Lista de hosts a comprobar
hosts = ["8.8.8.8", "1.1.1.1", "www.google.com", "www.github.com"]

# Detectar sistema operativo
param = "-n" if platform.system().lower() == "windows" else "-c"

for host in hosts:
    try:
        salida = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if salida.returncode == 0:
            texto = salida.stdout

            # Buscar tiempo en ms (funciona en español e inglés, Windows/Linux/MacOS)
            match = re.search(r"([Tt]iempo[=<]\s*|time[=<])\s*(\d+\.?\d*)\s*ms", texto)

            if match:
                tiempo = match.group(2)
                print(f"{host} está disponible ✅ | Tiempo de respuesta: {tiempo} ms")
            else:
                print(f"{host} está disponible ✅ (tiempo no detectado)")
                # Depuración: muestra la salida completa para ver el formato exacto
                # print(texto)
        else:
            print(f"{host} no responde ❌")

    except Exception as e:
        print(f"Error comprobando {host}: {e}")
