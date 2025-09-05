# 🚀 Ping Monitor

**Ping Monitor** es una herramienta sencilla en **Python** que permite comprobar la conectividad de múltiples hosts mediante `ping`.  
Los resultados se muestran en pantalla y se guardan automáticamente en un archivo **CSV**, incluyendo hosts personalizados añadidos por el usuario.

---

## ✨ Características

- ✅ Verifica la disponibilidad de hosts y direcciones IP.  
- ⏱ Muestra el tiempo de respuesta (ms) de cada host.  
- 🖊 Permite añadir hosts personalizados además de los predeterminados.  
- 💾 Guarda automáticamente los resultados en `resultados.csv` para análisis posterior.

---

## 🛠 Requisitos

- Python 3.x  
- Sistema operativo: Windows, Linux o MacOS  
- Librerías estándar: `subprocess`, `re`, `csv`, `platform`  

---

## 💻 Cómo usar

1. **Clona el repositorio:**

```bash
git clone https://github.com/Alex13042001/Ping-monitor
```

2. **Accede a la carpeta del proyecto:**
cd ping-monitor

3. **Ejecuta el script:**
python monitor.py

4. **Opcional: añade hosts personalizados separados por comas cuando se te pida:**
Introduce hosts adicionales separados por comas (o deja vacío para continuar): www.openai.com, 192.168.1.1...

5. **Salida ejemplo en consola:**
8.8.8.8 está disponible ✅ | Tiempo de respuesta: 20 ms
1.1.1.1 está disponible ✅ | Tiempo de respuesta: 18 ms
www.google.com está disponible ✅ | Tiempo de respuesta: 25.3 ms
www.github.com está disponible ✅ | Tiempo de respuesta: 42.1 ms
www.openai.com está disponible ✅ | Tiempo de respuesta: 30 ms
192.168.1.1 no responde ❌ <!-- No responde ya que es una IP privada -->

6. **Resultados en resultados.csv:**
Host,Estado,Tiempo (ms)
8.8.8.8,Disponible,20
1.1.1.1,Disponible,18
www.google.com,Disponible,25
www.github.com,Disponible,42
www.openai.com,Disponible,30
192.168.1.1,No responde,-
