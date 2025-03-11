"""
Tests for the VolyClient class.
"""

import pytest
import numpy as np
from voly import VolyClient


def test_client_initialization():
    """Test that the client initializes correctly."""
    client = VolyClient()
    assert client is not None


def test_bs_pricing():
    """Test Black-Scholes pricing function."""
    client = VolyClient()

    # Test call price
    call_price = client.bs(s=100, k=100, r=0.05, vol=0.2, t=1, option_type='call')
    assert call_price > 0
    assert call_price < 20  # Sanity check

    # Test put price
    put_price = client.bs(s=100, k=100, r=0.05, vol=0.2, t=1, option_type='put')
    assert put_price > 0
    assert put_price < 20  # Sanity check

    # Test put-call parity (approximately)
    parity_diff = abs(call_price - put_price - 100 + 100 * np.exp(-0.05))
    assert parity_diff < 1e-10


def test_greeks_calculation():
    """Test that all Greeks are calculated correctly."""
    client = VolyClient()

    # Calculate all Greeks
    greeks = client.greeks(s=100, k=100, r=0.05, vol=0.2, t=1, option_type='call')

    # Check that all expected Greeks are present
    expected_keys = ['price', 'delta', 'gamma', 'vega', 'theta', 'rho', 'vanna', 'volga', 'charm']
    for key in expected_keys:
        assert key in greeks
        assert isinstance(greeks[key], float)

    # Basic sanity checks
    assert 0 < greeks['delta'] < 1  # Call delta between 0 and 1
    assert greeks['gamma'] > 0  # Gamma always positive
    assert greeks['vega'] > 0  # Vega always positive
    assert greeks['theta'] < 0  # Call theta typically negative
