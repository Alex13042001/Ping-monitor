import os

# Lista de hosts a comprobar
hosts = ["8.8.8.8", "1.1.1.1", "www.google.com", "www.github.com"]

for host in hosts:
    respuesta = os.system(f"ping -c 1 {host}")  # en Windows usa: ping -n 1
    if respuesta == 0:
        print(f"{host} está disponible ✅")
    else:
        print(f"{host} no responde ❌")
