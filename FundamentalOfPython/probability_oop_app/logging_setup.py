from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from errors import ConfigurationError

PROJECT_DIR = Path(__file__).resolve().parent


def configure_logging(config: dict[str, Any]) -> Path:
    """Configure console logging and a rotating file inside the logs folder."""

    level = getattr(logging, config["level"], None)
    if not isinstance(level, int):
        raise ConfigurationError(f"Invalid log level: {config['level']}")

    log_path = Path(config["file"])
    if not log_path.is_absolute():
        log_path = PROJECT_DIR / log_path

    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = RotatingFileHandler(
            log_path,
            maxBytes=config["max_bytes"],
            backupCount=config["backup_count"],
            encoding="utf-8",
        )
    except OSError as exc:
        raise ConfigurationError(
            f"Could not create log file {log_path}: {exc}"
        ) from exc

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    for old_handler in root_logger.handlers[:]:
        root_logger.removeHandler(old_handler)
        old_handler.close()

    root_logger.setLevel(level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    return log_path
