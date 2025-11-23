# para interactuar con las ventanas de Windows (activarlas, moverlas, ver si son visibles,
import win32gui

# permite saber qué proceso pertenece a una ventana, usando el PID.
import win32process

# contiene constantes de Windows, como SW_RESTORE que sirve para restaurar una ventana minimizada.
import win32con

PID_PROCESO = 23880  # Modificar con el PID correcto


# HWND significa “handle to a window” → básicamente, es un número único que Windows usa para referirse a cada ventana abierta.
def activar_ventana_proceso():
    hwnd_target = None

    # EnumWindows → recorre todas las ventanas abiertas en Windows.
    def enum_window(hwnd, _):
        nonlocal hwnd_target
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            # si la ventana pertenece al PID que buscamos y está visible, guardamos su hwnd en hwnd_target.
            if pid == PID_PROCESO and win32gui.IsWindowVisible(hwnd):
                hwnd_target = hwnd
        except:
            pass

    win32gui.EnumWindows(enum_window, None)

    if hwnd_target:
        try:
            #ShowWindow(hwnd_target, SW_RESTORE) → si la ventana estaba minimizada, la restaura.
            win32gui.ShowWindow(hwnd_target, win32con.SW_RESTORE)
            #SetForegroundWindow(hwnd_target) → pone la ventana delante de todo lo demás, la activa.
            win32gui.SetForegroundWindow(hwnd_target)
            return True
        except Exception as e:
            print("Error activando ventana:", e)
            return False
    else:
        print("No se encontró ventana para el PID:", PID_PROCESO)
        return False
