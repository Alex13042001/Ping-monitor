import platform
import subprocess

# Lista de hosts a comprobar
hosts = ["8.8.8.8", "1.1.1.1", "www.google.com", "www.github.com"]

# Detectar sistema operativo
param = "-n" if platform.system().lower() == "windows" else "-c"

for host in hosts:
    try:
        salida = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if salida.returncode == 0:
            print(f"{host} está disponible ✅")
        else:
            print(f"{host} no responde ❌")
    except Exception as e:
        print(f"Error comprobando {host}: {e}")
