"""
Tests for the VolyClient class using Python's built-in unittest framework.
"""

import unittest
import numpy as np
from voly import VolyClient


class TestVolyClient(unittest.TestCase):
    """Test cases for the VolyClient class."""

    def setUp(self):
        """Set up test fixtures."""
        self.voly = VolyClient()

    def test_voly_initialization(self):
        """Test that the voly initializes correctly."""
        self.assertIsNotNone(self.voly)

    def test_bs_pricing(self):
        """Test Black-Scholes pricing function."""
        # Test call price
        call_price = self.voly.bs(s=100, k=100, r=0.05, vol=0.2, t=1, option_type='call')
        self.assertGreater(call_price, 0)
        self.assertLess(call_price, 20)  # Sanity check

        # Test put price
        put_price = self.voly.bs(s=100, k=100, r=0.05, vol=0.2, t=1, option_type='put')
        self.assertGreater(put_price, 0)
        self.assertLess(put_price, 20)  # Sanity check

        # Test put-call parity (approximately)
        parity_diff = abs(call_price - put_price - 100 + 100 * np.exp(-0.05))
        self.assertLess(parity_diff, 1e-10)

    def test_greeks_calculation(self):
        """Test that all Greeks are calculated correctly."""
        # Calculate all Greeks
        greeks = self.voly.greeks(s=100, k=100, r=0.05, vol=0.2, t=1, option_type='call')

        # Check that all expected Greeks are present
        expected_keys = ['price', 'delta', 'gamma', 'vega', 'theta', 'rho', 'vanna', 'volga', 'charm']
        for key in expected_keys:
            self.assertIn(key, greeks)
            self.assertIsInstance(greeks[key], float)

        # Basic sanity checks
        self.assertGreater(greeks['delta'], 0)  # Call delta positive
        self.assertLess(greeks['delta'], 1)  # Call delta less than 1
        self.assertGreater(greeks['gamma'], 0)  # Gamma always positive
        self.assertGreater(greeks['vega'], 0)  # Vega always positive
        self.assertLess(greeks['theta'], 0)  # Call theta typically negative

    def test_delta_values(self):
        """Test delta values for different moneyness levels."""
        # Deep ITM call should have delta close to 1
        itm_delta = self.voly.delta(s=100, k=50, r=0.05, vol=0.2, t=1, option_type='call')
        self.assertGreater(itm_delta, 0.95)

        # Deep OTM call should have delta close to 0
        otm_delta = self.voly.delta(s=100, k=200, r=0.05, vol=0.2, t=1, option_type='call')
        self.assertLess(otm_delta, 0.05)

        # Deep ITM put should have delta close to -1
        itm_put_delta = self.voly.delta(s=100, k=200, r=0.05, vol=0.2, t=1, option_type='put')
        self.assertLess(itm_put_delta, -0.95)

        # Deep OTM put should have delta close to 0
        otm_put_delta = self.voly.delta(s=100, k=50, r=0.05, vol=0.2, t=1, option_type='put')
        self.assertGreater(otm_put_delta, -0.05)

    def test_implied_volatility(self):
        """Test implied volatility calculation."""
        # Calculate option price with known volatility
        vol = 0.2
        s = 100
        k = 100
        r = 0.05
        t = 1
        option_price = self.voly.bs(s=s, k=k, r=r, vol=vol, t=t, option_type='call')

        # Calculate implied volatility from the price
        implied_vol = self.voly.iv(option_price=option_price, s=s, k=k, r=r, t=t, option_type='call')

        # Verify that the implied volatility is close to the original volatility
        self.assertAlmostEqual(vol, implied_vol, places=4)


if __name__ == '__main__':
    unittest.main()
