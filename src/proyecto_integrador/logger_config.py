# logger_config.py
import logging
import os
from datetime import datetime

# Crear carpeta logs si no existe
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Nombre del archivo con fecha y hora
LOG_FILE = os.path.join(
    LOGS_DIR,
    f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

# Configuración básica del logging (una sola vez)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)

def get_logger(name: str) -> logging.Logger:
    """
    Devuelve un logger para el nombre indicado.
    Todos escriben en el mismo archivo LOG_FILE.
    """
    return logging.getLogger(name)
