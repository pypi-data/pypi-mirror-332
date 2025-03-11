"""
Unit tests for retry policy implementations.

This module tests the retry policy classes in openagents_json.job.retry,
including FixedDelayRetryPolicy and ExponentialBackoffRetryPolicy.
"""

import json
import unittest
from typing import Any, Dict

from openagents_json.job.retry import (
    ExponentialBackoffRetryPolicy,
    FixedDelayRetryPolicy,
    RetryPolicy,
)


class TestFixedDelayRetryPolicy(unittest.TestCase):
    """Tests for the FixedDelayRetryPolicy class."""

    def test_default_parameters(self):
        """Test that default parameters are set correctly."""
        policy = FixedDelayRetryPolicy()
        self.assertEqual(policy.delay, 30)
        self.assertEqual(policy.jitter, 0)

    def test_custom_parameters(self):
        """Test that custom parameters are set correctly."""
        policy = FixedDelayRetryPolicy(delay=10, jitter=0.2)
        self.assertEqual(policy.delay, 10)
        self.assertEqual(policy.jitter, 0.2)

    def test_get_retry_delay_no_jitter(self):
        """Test that retry delay is calculated correctly without jitter."""
        policy = FixedDelayRetryPolicy(delay=15, jitter=0)
        for attempt in range(1, 6):
            delay = policy.get_retry_delay(attempt, 5)
            self.assertEqual(delay, 15)

    def test_get_retry_delay_with_jitter(self):
        """Test that retry delay with jitter falls within expected range."""
        policy = FixedDelayRetryPolicy(delay=10, jitter=0.5)
        for attempt in range(1, 6):
            delay = policy.get_retry_delay(attempt, 5)
            # With 50% jitter, delay should be between 5 and 15
            self.assertTrue(5 <= delay <= 15)

    def test_to_dict(self):
        """Test serialization to dictionary."""
        policy = FixedDelayRetryPolicy(delay=20, jitter=0.3)
        data = policy.to_dict()

        self.assertEqual(data["type"], "fixed_delay")
        self.assertEqual(data["delay"], 20)
        self.assertEqual(data["jitter"], 0.3)

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        data = {"type": "fixed_delay", "delay": 25, "jitter": 0.4}

        policy = RetryPolicy.from_dict(data)

        self.assertIsInstance(policy, FixedDelayRetryPolicy)
        self.assertEqual(policy.delay, 25)
        self.assertEqual(policy.jitter, 0.4)

    def test_json_serialization(self):
        """Test that the policy can be properly serialized to JSON."""
        policy = FixedDelayRetryPolicy(delay=12, jitter=0.25)
        json_str = json.dumps(policy.to_dict())
        data = json.loads(json_str)

        reconstructed_policy = RetryPolicy.from_dict(data)

        self.assertIsInstance(reconstructed_policy, FixedDelayRetryPolicy)
        self.assertEqual(reconstructed_policy.delay, 12)
        self.assertEqual(reconstructed_policy.jitter, 0.25)


class TestExponentialBackoffRetryPolicy(unittest.TestCase):
    """Tests for the ExponentialBackoffRetryPolicy class."""

    def test_default_parameters(self):
        """Test that default parameters are set correctly."""
        policy = ExponentialBackoffRetryPolicy()
        self.assertEqual(policy.initial_delay, 5)
        self.assertEqual(policy.max_delay, 300)
        self.assertEqual(policy.multiplier, 2)
        self.assertEqual(policy.jitter, 0)

    def test_custom_parameters(self):
        """Test that custom parameters are set correctly."""
        policy = ExponentialBackoffRetryPolicy(
            initial_delay=2, max_delay=60, multiplier=3, jitter=0.1
        )
        self.assertEqual(policy.initial_delay, 2)
        self.assertEqual(policy.max_delay, 60)
        self.assertEqual(policy.multiplier, 3)
        self.assertEqual(policy.jitter, 0.1)

    def test_get_retry_delay_no_jitter(self):
        """Test that retry delay is calculated correctly without jitter."""
        policy = ExponentialBackoffRetryPolicy(
            initial_delay=1, max_delay=100, multiplier=2, jitter=0
        )

        # Expected delays:
        # attempt 1: 1s
        # attempt 2: 2s (1 * 2^1)
        # attempt 3: 4s (1 * 2^2)
        # attempt 4: 8s (1 * 2^3)
        # attempt 5: 16s (1 * 2^4)
        expected_delays = [1, 2, 4, 8, 16]

        for attempt, expected in enumerate(expected_delays, 1):
            delay = policy.get_retry_delay(attempt, 5)
            self.assertEqual(delay, expected)

    def test_max_delay_cap(self):
        """Test that delay is capped at max_delay."""
        policy = ExponentialBackoffRetryPolicy(
            initial_delay=10, max_delay=50, multiplier=4, jitter=0
        )

        # Expected delays:
        # attempt 1: 10s
        # attempt 2: 40s (10 * 4^1)
        # attempt 3: 50s (capped at max_delay)
        expected_delays = [10, 40, 50, 50, 50]

        for attempt, expected in enumerate(expected_delays, 1):
            delay = policy.get_retry_delay(attempt, 5)
            self.assertEqual(delay, expected)

    def test_get_retry_delay_with_jitter(self):
        """Test that retry delay with jitter falls within expected range."""
        policy = ExponentialBackoffRetryPolicy(
            initial_delay=5, max_delay=100, multiplier=2, jitter=0.5
        )

        # Expected delay ranges with 50% jitter:
        # attempt 1: 2.5-7.5s (5 ± 50%)
        # attempt 2: 5-15s (10 ± 50%)
        # attempt 3: 10-30s (20 ± 50%)
        delay_ranges = [
            (2.5, 7.5),
            (5, 15),
            (10, 30),
            (20, 60),
            (40, 100),  # Will be capped at max_delay for the upper bound
        ]

        for attempt, (min_delay, max_delay) in enumerate(delay_ranges, 1):
            delay = policy.get_retry_delay(attempt, 5)
            self.assertTrue(
                min_delay <= delay <= max_delay,
                f"Attempt {attempt}: {delay} not in range [{min_delay}, {max_delay}]",
            )

    def test_to_dict(self):
        """Test serialization to dictionary."""
        policy = ExponentialBackoffRetryPolicy(
            initial_delay=3, max_delay=120, multiplier=2.5, jitter=0.2
        )
        data = policy.to_dict()

        self.assertEqual(data["type"], "exponential_backoff")
        self.assertEqual(data["initial_delay"], 3)
        self.assertEqual(data["max_delay"], 120)
        self.assertEqual(data["multiplier"], 2.5)
        self.assertEqual(data["jitter"], 0.2)

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        data = {
            "type": "exponential_backoff",
            "initial_delay": 2,
            "max_delay": 180,
            "multiplier": 3,
            "jitter": 0.3,
        }

        policy = RetryPolicy.from_dict(data)

        self.assertIsInstance(policy, ExponentialBackoffRetryPolicy)
        self.assertEqual(policy.initial_delay, 2)
        self.assertEqual(policy.max_delay, 180)
        self.assertEqual(policy.multiplier, 3)
        self.assertEqual(policy.jitter, 0.3)

    def test_json_serialization(self):
        """Test that the policy can be properly serialized to JSON."""
        policy = ExponentialBackoffRetryPolicy(
            initial_delay=4, max_delay=240, multiplier=2, jitter=0.25
        )
        json_str = json.dumps(policy.to_dict())
        data = json.loads(json_str)

        reconstructed_policy = RetryPolicy.from_dict(data)

        self.assertIsInstance(reconstructed_policy, ExponentialBackoffRetryPolicy)
        self.assertEqual(reconstructed_policy.initial_delay, 4)
        self.assertEqual(reconstructed_policy.max_delay, 240)
        self.assertEqual(reconstructed_policy.multiplier, 2)
        self.assertEqual(reconstructed_policy.jitter, 0.25)


class TestRetryPolicyFactory(unittest.TestCase):
    """Tests for the RetryPolicy.from_dict factory method."""

    def test_unknown_policy_type(self):
        """Test that unknown policy type raises ValueError."""
        data = {"type": "unknown_policy"}
        with self.assertRaises(ValueError):
            RetryPolicy.from_dict(data)

    def test_missing_type(self):
        """Test that missing type raises ValueError."""
        data = {"delay": 10}
        with self.assertRaises(ValueError):
            RetryPolicy.from_dict(data)


if __name__ == "__main__":
    unittest.main()
