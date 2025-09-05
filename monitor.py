import platform
import subprocess
import re
import csv

# Lista de hosts por defecto
hosts_defecto = ["8.8.8.8", "1.1.1.1", "www.google.com", "www.github.com"]

# Preguntar al usuario si quiere añadir hosts extra
entrada = input("Introduce hosts adicionales separados por comas (o deja vacío para continuar): ").strip()

if entrada:
    hosts_usuario = [h.strip() for h in entrada.split(",") if h.strip()]
    hosts = hosts_defecto + hosts_usuario
else:
    hosts = hosts_defecto

print("\n✅ Comprobando los siguientes hosts:")
for h in hosts:
    print("-", h)

print("\n🔄 Iniciando comprobación...\n")

# Detectar sistema operativo
param = "-n" if platform.system().lower() == "windows" else "-c"

# Crear archivo CSV
with open("resultados.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Host", "Estado", "Tiempo (ms)"])

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
                match = re.search(r"([Tt]iempo[=<]\s*|time[=<])\s*(\d+\.?\d*)\s*ms", texto)

                if match:
                    tiempo = match.group(2)
                    print(f"{host} está disponible ✅ | Tiempo de respuesta: {tiempo} ms")
                    writer.writerow([host, "Disponible", tiempo])
                else:
                    print(f"{host} está disponible ✅ (tiempo no detectado)")
                    writer.writerow([host, "Disponible", "N/D"])
            else:
                print(f"{host} no responde ❌")
                writer.writerow([host, "No responde", "-"])

        except Exception as e:
            print(f"Error comprobando {host}: {e}")
            writer.writerow([host, "Error", "-"])
