"""
Retry policy implementations for the OpenAgents JSON framework.

This module provides different retry strategies for failed jobs, including:
- Fixed delay: Retry with a constant delay between attempts
- Exponential backoff: Retry with increasing delays between attempts
- Jitter: Add randomness to retry delays to avoid thundering herd problems

These policies can be used to configure resilient job execution with
appropriate error handling for different types of failures.
"""

import abc
import math
import random
import secrets
from typing import Any, Dict, List, Optional, Type, Union

# Create a secure random number generator
secure_random = secrets.SystemRandom()


class RetryPolicy(abc.ABC):
    """
    Abstract base class for job retry policies.

    Retry policies define how and when failed jobs should be retried,
    with configurable delays between attempts.
    """

    @abc.abstractmethod
    def get_retry_delay(self, attempt: int, max_retries: int) -> float:
        """
        Calculate the delay in seconds before the next retry attempt.

        Args:
            attempt: The current retry attempt number (1-based)
            max_retries: The maximum number of retry attempts

        Returns:
            Delay in seconds before the next retry
        """
        pass

    @abc.abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the retry policy to a dictionary representation.

        Returns:
            Dictionary representation of the retry policy
        """
        pass

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RetryPolicy":
        """
        Create a retry policy from a dictionary representation.

        Args:
            data: Dictionary representation of the retry policy

        Returns:
            RetryPolicy instance
        """
        policy_type = data.get("type")

        if policy_type == "fixed_delay":
            return FixedDelayRetryPolicy(
                delay=data.get("delay", 30), jitter=data.get("jitter", 0)
            )
        elif policy_type == "exponential_backoff":
            return ExponentialBackoffRetryPolicy(
                initial_delay=data.get("initial_delay", 5),
                max_delay=data.get("max_delay", 300),
                multiplier=data.get("multiplier", 2),
                jitter=data.get("jitter", 0),
            )
        else:
            # Default to fixed delay
            return FixedDelayRetryPolicy()


class FixedDelayRetryPolicy(RetryPolicy):
    """
    Fixed delay retry policy.

    Retries failed jobs with a constant delay between attempts,
    optionally with jitter to avoid thundering herd problems.
    """

    def __init__(self, delay: float = 30, jitter: float = 0):
        """
        Initialize fixed delay retry policy.

        Args:
            delay: Delay in seconds between retry attempts (default: 30)
            jitter: Random jitter factor as a proportion of delay (0-1)
        """
        self.delay = delay
        self.jitter = max(0, min(1, jitter))  # Clamp jitter to [0,1]

    def get_retry_delay(self, attempt: int, max_retries: int) -> float:
        """
        Calculate the delay in seconds before the next retry attempt.

        For fixed delay, the delay is constant regardless of attempt number,
        but may include jitter if configured.

        Args:
            attempt: The current retry attempt number (1-based)
            max_retries: The maximum number of retry attempts

        Returns:
            Delay in seconds before the next retry
        """
        if self.jitter == 0:
            return self.delay

        # Apply jitter - adjust delay by random percentage between 0 and jitter
        jitter_factor = 1 + (secure_random.random() * self.jitter * 2 - self.jitter)
        return max(1, self.delay * jitter_factor)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the retry policy to a dictionary representation.

        Returns:
            Dictionary representation of the retry policy
        """
        return {"type": "fixed_delay", "delay": self.delay, "jitter": self.jitter}


class ExponentialBackoffRetryPolicy(RetryPolicy):
    """
    Exponential backoff retry policy.

    Retries failed jobs with exponentially increasing delays between attempts,
    optionally with jitter to avoid thundering herd problems.
    """

    def __init__(
        self,
        initial_delay: float = 5,
        max_delay: float = 300,
        multiplier: float = 2,
        jitter: float = 0,
    ):
        """
        Initialize exponential backoff retry policy.

        Args:
            initial_delay: Initial delay in seconds for first retry (default: 5)
            max_delay: Maximum delay in seconds between retries (default: 300)
            multiplier: Factor by which delay increases for each attempt (default: 2)
            jitter: Random jitter factor as a proportion of delay (0-1)
        """
        self.initial_delay = initial_delay
        self.max_delay = max_delay
        self.multiplier = multiplier
        self.jitter = max(0, min(1, jitter))  # Clamp jitter to [0,1]

    def get_retry_delay(self, attempt: int, max_retries: int) -> float:
        """
        Calculate the delay in seconds before the next retry attempt.

        For exponential backoff, the delay increases exponentially with each attempt,
        but may include jitter if configured.

        Args:
            attempt: The current retry attempt number (1-based)
            max_retries: The maximum number of retry attempts

        Returns:
            Delay in seconds before the next retry
        """
        # Calculate exponential backoff
        delay = min(
            self.max_delay, self.initial_delay * (self.multiplier ** (attempt - 1))
        )

        if self.jitter == 0:
            return delay

        # Apply jitter - adjust delay by random percentage between 0 and jitter
        jitter_factor = 1 + (secure_random.random() * self.jitter * 2 - self.jitter)
        return max(1, delay * jitter_factor)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the retry policy to a dictionary representation.

        Returns:
            Dictionary representation of the retry policy
        """
        return {
            "type": "exponential_backoff",
            "initial_delay": self.initial_delay,
            "max_delay": self.max_delay,
            "multiplier": self.multiplier,
            "jitter": self.jitter,
        }
