# Script Sencillo

Este proyecto contiene un **script en Python** para automatizar de manera sencilla la pulsación de la tecla `8` cada 10 minutos en el juego.

> ⚠️ Este script está destinado **solo para fines educativos**.  
> El uso de automatizaciones en juegos puede estar **prohibido por los términos de servicio** y puede causar sanciones en el juego. Usa bajo tu responsabilidad.

---

## Estructura del proyecto

- script_sencillo_wow/
  - ventana_proceso.py   # Función para activar la ventana
  - main.py              # Macro principal que pulsa la tecla 8
  - README.md            # Este archivo
  - .gitignore           # Ignora __pycache__ y archivos temporales


---

## Requisitos

Instala las librerías necesarias usando `pip`:

```bash
pip install pyautogui keyboard pywin32
```

## Uso
- Abre la aplicación Ascension WoW en tu ordenador.
- Ejecuta el script principal:


## Personalización
- Puedes cambiar la tecla o el intervalo de tiempo en main.py.
- La función esperar_interruptible(min_s, max_s) permite añadir un pequeño retraso aleatorio para simular un comportamiento más natural.