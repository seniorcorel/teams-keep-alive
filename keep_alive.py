"""
Keep Alive - Simula actividad para evitar que el PC se bloquee
y que Teams marque como ausente.

Combina: movimiento de mouse + tecla + scroll

Uso: python keep_alive.py
Para detener: Ctrl+C
"""

import pyautogui
import time
import sys
import ctypes

pyautogui.FAILSAFE = False

INTERVALO_SEGUNDOS = 30  # más frecuente para mayor seguridad

# Constantes de Windows para evitar suspensión
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002


def prevent_sleep():
    """Usa la API de Windows para indicar que el sistema está en uso."""
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )


def simulate_activity():
    """Simula actividad con mouse, teclado y scroll."""
    # Mover mouse 1px ida y vuelta
    pyautogui.moveRel(1, 0, duration=0.05)
    pyautogui.moveRel(-1, 0, duration=0.05)

    # Presionar y soltar Shift (no escribe nada)
    pyautogui.press("shift")

    # Scroll mínimo ida y vuelta
    pyautogui.scroll(1)
    pyautogui.scroll(-1)


def main():
    print("🟢 Keep Alive activo. Presiona Ctrl+C para detener.")
    print(f"   Intervalo: cada {INTERVALO_SEGUNDOS} segundos\n")

    try:
        while True:
            prevent_sleep()
            simulate_activity()
            print(f"   ✓ Actividad simulada - {time.strftime('%H:%M:%S')}", end="\r")
            time.sleep(INTERVALO_SEGUNDOS)
    except KeyboardInterrupt:
        # Restaurar estado normal de suspensión
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        print("\n🔴 Keep Alive detenido.")
        sys.exit(0)


if __name__ == "__main__":
    main()
