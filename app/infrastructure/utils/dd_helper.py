from fastapi import HTTPException
import json

def dd(value):
    """Helper similar a dd() en Laravel. Detiene la ejecución y retorna el valor."""
    try:
        # Intentamos serializar el valor antes de lanzarlo en la excepción
        serialized_value = json.dumps(value)
    except TypeError:
        serialized_value = f"Non-serializable value: {value}"

    raise HTTPException(status_code = 500, detail= serialized_value)