import win32gui
import win32process
import win32con

# ⚠ MODIFICAR CON EL PID CORRECTO DE TU APLICACIÓN
PID_PROCESO = 5336

def encontrar_hwnd_por_pid():
    """
    Busca el handle (hwnd) de la ventana principal del proceso.
    Retorna el hwnd si lo encuentra, None en caso contrario.
    """
    hwnd_target = None
    
    def enum_window(hwnd, _):
        nonlocal hwnd_target
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            # Buscar ventana visible del proceso objetivo
            if pid == PID_PROCESO and win32gui.IsWindowVisible(hwnd):
                hwnd_target = hwnd
        except:
            pass
    
    win32gui.EnumWindows(enum_window, None)
    return hwnd_target

def activar_ventana_proceso():
    """
    Restaura y activa (pone en primer plano) la ventana del proceso.
    Retorna True si tuvo éxito, False en caso contrario.
    """
    hwnd = encontrar_hwnd_por_pid()
    
    if hwnd:
        try:
            # Restaurar si está minimizada
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            # Activar y poner en primer plano
            win32gui.SetForegroundWindow(hwnd)
            return True
        except Exception as e:
            print(f"❌ Error activando ventana: {e}")
            return False
    else:
        print(f"❌ No se encontró ventana visible para PID: {PID_PROCESO}")
        return False

def minimizar_ventana_proceso():
    """
    Minimiza la ventana del proceso.
    Retorna True si tuvo éxito, False en caso contrario.
    """
    hwnd = encontrar_hwnd_por_pid()
    
    if hwnd:
        try:
            # SW_MINIMIZE minimiza la ventana
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            return True
        except Exception as e:
            print(f"❌ Error minimizando ventana: {e}")
            return False
    else:
        print(f"❌ No se encontró ventana para minimizar (PID: {PID_PROCESO})")
        return False

def obtener_info_ventana():
    """
    Función auxiliar para debug: muestra información de la ventana.
    """
    hwnd = encontrar_hwnd_por_pid()
    
    if hwnd:
        titulo = win32gui.GetWindowText(hwnd)
        print(f"HWND: {hwnd}")
        print(f"Título: {titulo if titulo else '(sin título)'}")
        print(f"PID: {PID_PROCESO}")
        return True
    else:
        print(f"No se encontró ventana para PID: {PID_PROCESO}")
        return False

# Para testing
if __name__ == "__main__":
    print("=== TEST DE FUNCIONES DE VENTANA ===\n")
    
    print("1. Información de la ventana:")
    obtener_info_ventana()
    
    print("\n2. Activando ventana...")
    if activar_ventana_proceso():
        print("✓ Ventana activada")
        
        import time
        time.sleep(2)
        
        print("\n3. Minimizando ventana...")
        if minimizar_ventana_proceso():
            print("✓ Ventana minimizada")
        
        time.sleep(2)
        
        print("\n4. Restaurando ventana...")
        if activar_ventana_proceso():
            print("✓ Ventana restaurada")