import logging
from pathlib import Path

log_path = Path(__file__).parent.parent / "logs"

log_path.mkdir(exist_ok=True)

logger = logging.getLogger("etl_logger")

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    log_path / "etl.log",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)