# Script Sencillo WoW Ascension

Este proyecto contiene un **script en Python** para automatizar de manera sencilla la pulsación de la tecla `8` cada 10 minutos en el juego **Ascension WoW**.

> ⚠️ Este script está destinado **solo para fines educativos**.  
> El uso de automatizaciones en juegos puede estar **prohibido por los términos de servicio** y puede causar sanciones en el juego. Usa bajo tu responsabilidad.

---

## Estructura del proyecto
script_sencillo_wow/
│
├─ ventana_proceso.py # Función para activar la ventana.
├─ main.py # Macro principal que pulsa la tecla 8
├─ README.md # Este archivo
└─ .gitignore # Ignora pycache y archivos temporales

---

## Requisitos

Instala las librerías necesarias usando `pip`:

```bash
pip install pyautogui keyboard pywin32


## Uso
> Coloca la aplicacion abierto en tu ordenador.

Personalización
Puedes cambiar la tecla o el intervalo de tiempo en main.py.
La función esperar_interruptible(min_s, max_s) permite añadir un pequeño retraso aleatorio si quieres simular un comportamiento más natural.