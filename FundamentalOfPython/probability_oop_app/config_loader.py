from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from dotenv import dotenv_values
import yaml

from errors import ConfigurationError

PROJECT_DIR = Path(__file__).resolve().parent
CONFIG_DIR = PROJECT_DIR / "config"


def _read_env(path: Path) -> dict[str, Any]:
    values = dotenv_values(path)

    return {
        "binomial": {
            "n": values.get("BINOMIAL_N"),
            "p": values.get("BINOMIAL_P"),
        },
        "poisson": {
            "rate": values.get("POISSON_RATE"),
        },
        "calculation": {
            "k": values.get("K"),
        },
        "logging": {
            "level": values.get("LOG_LEVEL", "INFO"),
            "file": values.get("LOG_FILE", "logs/distributions.log"),
            "max_bytes": values.get("LOG_MAX_BYTES", "1000000"),
            "backup_count": values.get("LOG_BACKUP_COUNT", "3"),
        },
    }


def _read_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ConfigurationError(
            f"Invalid JSON in {path.name}, line {exc.lineno}"
        ) from exc

    if not isinstance(data, dict):
        raise ConfigurationError(f"{path.name} must contain a JSON object")

    return data


def _read_yaml(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        raise ConfigurationError(f"Invalid YAML in {path.name}: {exc}") from exc

    if not isinstance(data, dict):
        raise ConfigurationError(f"{path.name} must contain a YAML mapping")

    return data


def _normalise(raw: dict[str, Any]) -> dict[str, Any]:
    try:
        config = {
            "binomial": {
                "n": int(raw["binomial"]["n"]),
                "p": float(raw["binomial"]["p"]),
            },
            "poisson": {
                "rate": float(raw["poisson"]["rate"]),
            },
            "calculation": {
                "k": int(raw["calculation"]["k"]),
            },
            "logging": {
                "level": str(raw["logging"].get("level", "INFO")).upper(),
                "file": str(
                    raw["logging"].get("file", "logs/distributions.log")
                ).strip(),
                "max_bytes": int(raw["logging"].get("max_bytes", 1_000_000)),
                "backup_count": int(raw["logging"].get("backup_count", 3)),
            },
        }
    except KeyError as exc:
        raise ConfigurationError(
            f"Missing configuration key: {exc.args[0]}"
        ) from exc
    except (TypeError, ValueError, AttributeError) as exc:
        raise ConfigurationError(
            "Configuration values have incorrect types"
        ) from exc

    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
    if config["logging"]["level"] not in valid_levels:
        raise ConfigurationError(
            "LOG_LEVEL must be DEBUG, INFO, WARNING, ERROR, or CRITICAL"
        )

    if not config["logging"]["file"]:
        raise ConfigurationError("Log file path cannot be empty")

    if config["logging"]["max_bytes"] <= 0:
        raise ConfigurationError("max_bytes must be greater than 0")

    if config["logging"]["backup_count"] < 1:
        raise ConfigurationError("backup_count must be at least 1")

    return config


def load_config(config_type: str) -> dict[str, Any]:
    """Load one of the three demonstration configuration formats."""

    choices: dict[str, tuple[str, Callable[[Path], dict[str, Any]]]] = {
        "env": (".env", _read_env),
        "json": ("settings.json", _read_json),
        "yaml": ("settings.yaml", _read_yaml),
    }

    try:
        filename, loader = choices[config_type.lower()]
    except KeyError as exc:
        raise ConfigurationError(
            "Configuration type must be env, json, or yaml"
        ) from exc

    path = CONFIG_DIR / filename

    try:
        raw = loader(path)
    except FileNotFoundError as exc:
        raise ConfigurationError(f"Configuration file not found: {path}") from exc
    except OSError as exc:
        raise ConfigurationError(f"Could not read {path}: {exc}") from exc

    return _normalise(raw)
