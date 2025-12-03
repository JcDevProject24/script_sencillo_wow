import pyautogui
import time
import random
import threading
import keyboard
from ventana_proceso import activar_ventana_proceso, minimizar_ventana_proceso

stop_flag = False

# --- TIEMPOS RANDOM ---
def esperar_interruptible(min_s, max_s):
    global stop_flag
    total = random.uniform(min_s, max_s)
    paso = 0.2 if total > 60 else 0.1
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
    
    # Verificar que la ventana existe al inicio
    if not activar_ventana_proceso():
        print("❌ No se pudo activar el proceso. Verifica el PID.")
        return
    
    print("✓ Macro iniciada. Tienes 2s para prepararte...")
    esperar_interruptible(2, 2)
    print("⚠ Macro en ejecución. Pulsa '.' para detener.")
    
    ciclo = 1
    intentos_fallidos = 0
    MAX_INTENTOS_FALLIDOS = 3  # Número de intentos antes de detener
    
    while not stop_flag:
        print(f"\n--- Ciclo {ciclo} ---")
        
        # 1. Restaurar y activar ventana
        if not activar_ventana_proceso():
            intentos_fallidos += 1
            print(f"⚠ No se pudo activar la ventana. Intento {intentos_fallidos}/{MAX_INTENTOS_FALLIDOS}")
            
            if intentos_fallidos >= MAX_INTENTOS_FALLIDOS:
                print(f"❌ CRÍTICO: No se pudo encontrar la ventana tras {MAX_INTENTOS_FALLIDOS} intentos.")
                print("❌ Deteniendo el script por seguridad...")
                stop_flag = True
                break
            
            print("Esperando 5s antes de reintentar...")
            esperar_interruptible(5, 5)
            continue
        
        # Resetear contador si la activación fue exitosa
        intentos_fallidos = 0
        
        print("✓ Ventana activada")
        esperar_interruptible(0.8, 1)  # Pequeña pausa para asegurar el foco
        
        # 2. Pulsar el botón 8
        mantener_tecla("8", 0.05, 0.15)
        print("✓ Botón 8 pulsado")
        
        # 3. Minimizar la ventana
        esperar_interruptible(0.5, 0.7)  # Pausa antes de minimizar
        if minimizar_ventana_proceso():
            print("✓ Ventana minimizada")
        else:
            print("⚠ No se pudo minimizar (continuando...)")
        
        # 4. Esperar 10 minutos
        print("⏳ Esperando ~10 minutos (601-604s)...")
        esperar_interruptible(10, 11)
        
        if not stop_flag:
            print(f"✓ Ciclo {ciclo} completado")
            ciclo += 1
    
    print("\n🛑 Macro detenida.")

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
            print("\n⏸ Detención solicitada por el usuario...")
            stop_flag = True
            break
        time.sleep(0.1)

# --- ARRANQUE ---
if __name__ == "__main__":
    print("=" * 50)
    print("  MACRO DE AUTOMATIZACIÓN")
    print("=" * 50)
    
    start_macro()
    threading.Thread(target=escucha_tecla, daemon=True).start()
    
    # Mantener vivo el programa
    try:
        while not stop_flag:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n⚠ Interrupción de teclado detectada")
        stop_flag = True
    
    print("\n✓ Programa finalizado.")