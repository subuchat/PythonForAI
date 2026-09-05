from __future__ import annotations

from abc import ABC, abstractmethod
import logging
import math

from errors import DistributionError

logger = logging.getLogger(__name__)


class DiscreteDistribution(ABC):
    """Common interface for discrete probability distributions."""

    @abstractmethod
    def pmf(self, k: int) -> float:
        """Return P(X = k)."""

    @abstractmethod
    def mean(self) -> float:
        """Return the expected value."""

    @abstractmethod
    def variance(self) -> float:
        """Return the variance."""

    @staticmethod
    def _validate_k(k: int) -> None:
        if isinstance(k, bool) or not isinstance(k, int):
            raise DistributionError("k must be an integer")


class Binomial(DiscreteDistribution):
    def __init__(self, n: int, p: float) -> None:
        if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
            raise DistributionError("n must be a positive integer")

        if (
            isinstance(p, bool)
            or not isinstance(p, (int, float))
            or not math.isfinite(p)
            or not 0 <= p <= 1
        ):
            raise DistributionError("p must be a finite number between 0 and 1")

        self.n = n
        self.p = float(p)
        logger.info("Created Binomial model: n=%d, p=%s", self.n, self.p)

    def pmf(self, k: int) -> float:
        self._validate_k(k)

        if k < 0 or k > self.n:
            probability = 0.0
        else:
            probability = (
                math.comb(self.n, k)
                * self.p**k
                * (1 - self.p) ** (self.n - k)
            )

        logger.debug("Binomial P(X=%d)=%s", k, probability)
        return probability

    def mean(self) -> float:
        return self.n * self.p

    def variance(self) -> float:
        return self.n * self.p * (1 - self.p)


class Poisson(DiscreteDistribution):
    def __init__(self, rate: float) -> None:
        if (
            isinstance(rate, bool)
            or not isinstance(rate, (int, float))
            or not math.isfinite(rate)
            or rate <= 0
        ):
            raise DistributionError("rate must be a finite number greater than 0")

        self.rate = float(rate)
        logger.info("Created Poisson model: rate=%s", self.rate)

    def pmf(self, k: int) -> float:
        self._validate_k(k)

        if k < 0:
            probability = 0.0
        else:
            probability = (
                math.exp(-self.rate)
                * self.rate**k
                / math.factorial(k)
            )

        logger.debug("Poisson P(X=%d)=%s", k, probability)
        return probability

    def mean(self) -> float:
        return self.rate

    def variance(self) -> float:
        return self.rate
