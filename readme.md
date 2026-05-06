# Keep Alive

App en Python que mantiene tu PC activo para evitar el bloqueo automático y que Teams te marque como ausente.

## Qué hace

Cada 30 segundos simula actividad combinando:

- Movimiento de mouse (1px ida y vuelta)
- Presiona la tecla Shift (no escribe nada)
- Scroll mínimo ida y vuelta
- Llama a la API de Windows `SetThreadExecutionState` para prevenir suspensión

## Requisitos

- Python 3.6+
- Windows

## Instalación

```bash
pip install pyautogui
```

## Uso

```bash
python keep_alive.py
```

Para detener: `Ctrl+C`

## Configuración

Puedes ajustar el intervalo editando la variable `INTERVALO_SEGUNDOS` en `keep_alive.py`. Por defecto está en 30 segundos.
