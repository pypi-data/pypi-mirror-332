"""
Standalone tests that don't import from tests.utils.

These tests verify that our testing approach works correctly.
"""

import pytest


def test_simple_assertion():
    """A simple test to verify that pytest is working."""
    assert 1 + 1 == 2
