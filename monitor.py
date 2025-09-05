import os

# Lista de hosts a comprobar
hosts = ["8.8.8.8", "1.1.1.1", "www.google.com", "www.github.com"]

for host in hosts:
    respuesta = os.system(f"ping -c 1 {host}")  # en Windows usa: ping -n 1
    if respuesta == 0:
        print(f"{host} está disponible ✅")
    else:
        print(f"{host} no responde ❌")
with open("resultados.txt", "w") as f:
    for host in hosts:
        respuesta = os.system(f"ping -c 1 {host}")
        estado = "Disponible ✅" if respuesta == 0 else "No responde ❌"
        print(f"{host}: {estado}")
        f.write(f"{host}: {estado}\n")
hosts = input("Introduce los hosts separados por comas: ").split(",")
