from __future__ import annotations

import logging
import sys

from config_loader import load_config
from distributions import Binomial, DiscreteDistribution, Poisson
from errors import ConfigurationError, DistributionError
from logging_setup import configure_logging

logger = logging.getLogger(__name__)


def print_report(distribution: DiscreteDistribution, k: int) -> None:
    name = type(distribution).__name__
    print(f"\n{name}")
    print(f"P(X = {k}): {distribution.pmf(k):.4f}")
    print(f"Mean: {distribution.mean():.2f}")
    print(f"Variance: {distribution.variance():.2f}")


def run(config: dict) -> None:
    k = config["calculation"]["k"]

    models = [
        Binomial(**config["binomial"]),
        Poisson(**config["poisson"]),
    ]

    for model in models:
        print_report(model, k)


def main() -> int:
    config_type = sys.argv[1].lower() if len(sys.argv) > 1 else "json"

    # Configuration and logging setup may fail before file logging is available.
    try:
        config = load_config(config_type)
        log_path = configure_logging(config["logging"])
    except ConfigurationError as exc:
        print(f"Configuration error: {exc}")
        return 1

    logger.info("Application started with %s configuration", config_type)
    logger.info("Writing logs to %s", log_path)

    try:
        run(config)
    except DistributionError as exc:
        # logger.exception records the error message and traceback once,
        # at the application boundary where the error is handled.
        logger.exception("Invalid probability model: %s", exc)
        print(f"Calculation failed: {exc}")
        return 1
    except OSError as exc:
        logger.exception("Operating-system failure: %s", exc)
        print(f"Application failed: {exc}")
        return 1

    logger.info("Application completed successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
