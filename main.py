#La tecla que he utilizado para parar el script es el punto (.)
# Asegúrate de tener instalado el módulo 'keyboard' (pip install keyboard)
# Asegúrate de tener instalado el módulo 'pywin32' (pip install pywin32)
# Asegúrate de tener instalado el módulo 'pyautogui' (pip install pyautogui)
# Es un script basico pero con funcionalidad de aleatoriedad en los tiempos y posibilidad de interrupción.
import pyautogui
import time
import random
import threading
import keyboard

# Código para activar ventana por PID
from ventana_proceso import activar_ventana_proceso

stop_flag = False


# --- TIEMPOS RANDOM ---
def esperar_interruptible(min_s, max_s):
    global stop_flag
    total = random.uniform(min_s, max_s)
    paso = 0.05
    transcurrido = 0

    while transcurrido < total:
        if stop_flag:
            return
        time.sleep(paso)
        transcurrido += paso


# --- PULSAR TECLA CON TIEMPO ---
def mantener_tecla(tecla, duracion_min, duracion_max):
    pyautogui.keyDown(tecla)
    esperar_interruptible(duracion_min, duracion_max)
    pyautogui.keyUp(tecla)


# --- MACRO PRINCIPAL ---
def macro():
    global stop_flag

    if not activar_ventana_proceso():
        print("No se pudo activar proceso.")
        return

    print("Macro iniciada. Pulsará '8' cada 10 minutos.")
    print("Pulsa '.' para detener.")

    while not stop_flag:
        # Activar ventana antes de pulsar
        activar_ventana_proceso()

        # PULSAR EL BOTÓN 8 (duración random de 0.05–0.15s)
        mantener_tecla("8", 0.05, 0.15)

        print("8 pulsado. Esperando 10 minutos...")

        # Esperar 10 minutos (600 segundos) con interrupción
        esperar_interruptible(5, 5)

    print("Macro detenida.")


# --- INICIAR MACRO EN HILO ---
def start_macro():
    global stop_flag
    stop_flag = False
    threading.Thread(target=macro, daemon=True).start()


# --- ESCUCHAR TECLA PARA PARAR ---
def escucha_tecla():
    global stop_flag
    while not stop_flag:
        if keyboard.is_pressed("."):
            print("Detención solicitada.")
            stop_flag = True
            break
        time.sleep(0.05)


# --- ARRANQUE ---
start_macro()
threading.Thread(target=escucha_tecla, daemon=True).start()

# Mantener vivo el programa
while not stop_flag:
    time.sleep(0.1)

print("Programa finalizado.")
