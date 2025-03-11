import logging
import sys

# Configure logging for file (DEBUG and above)
logging.basicConfig(
    filename="radiens.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
    level=logging.DEBUG,  # Logs all levels to file
)

# Configure stdout handler (INFO and above)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)  # Only log INFO and above to stdout

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(module)s - %(message)s")
console_handler.setFormatter(formatter)

# Attach the console handler to the root logger
logging.getLogger().addHandler(console_handler)

logger = logging.getLogger(__name__)
