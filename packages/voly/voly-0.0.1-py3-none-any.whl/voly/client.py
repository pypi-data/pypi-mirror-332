"""
Main client interface for the Voly package.

This module provides the VolyClient class, which serves as the main
entry point for users to interact with the package functionality.
"""

import asyncio
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional, Union, Any, Callable
import plotly.graph_objects as go

from voly.utils.logger import logger, catch_exception, setup_file_logging
from voly.exceptions import VolyError, ValidationError, DataError
from voly.models import SVIModel
from voly.formulas import (
    bs, delta, gamma, vega, theta, rho, vanna, volga, charm, greeks, iv, implied_underlying
)
from voly.core.data import fetch_option_chain, process_option_chain
from voly.core.fit import fit_model
from voly.core.rnd import calculate_rnd, calculate_pdf, calculate_cdf, calculate_strike_probability
from voly.core.interpolate import interpolate_model
from voly.core.charts import (
    plot_volatility_smile, plot_3d_surface, plot_parameters, plot_fit_statistics,
    plot_rnd, plot_pdf, plot_cdf, plot_rnd_all_expiries, plot_rnd_3d,
    plot_rnd_statistics, generate_all_plots, plot_interpolated_surface
)


class VolyClient:
    def __init__(self, enable_file_logging: bool = False, logs_dir: str = "logs/"):
        """
        Initialize the Voly client.

        Parameters:
        - enable_file_logging: Whether to enable file-based logging
        - logs_dir: Directory for log files if file logging is enabled
        """
        if enable_file_logging:
            setup_file_logging(logs_dir)

        logger.info("VolyClient initialized")
        self._loop = None  # For async operations

    def _get_event_loop(self):
        """Get or create an event loop for async operations"""
        try:
            self._loop = asyncio.get_event_loop()
        except RuntimeError:
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)
        return self._loop

    # -------------------------------------------------------------------------
    # Data Fetching and Processing
    # -------------------------------------------------------------------------

    def get_option_chain(self, exchange: str = 'deribit',
                         currency: str = 'BTC',
                         depth: bool = False) -> pd.DataFrame:
        """
        Fetch option chain data from the specified exchange.

        Parameters:
        - exchange: Exchange to fetch data from (currently only 'deribit' is supported)
        - currency: Currency to fetch options for (e.g., 'BTC', 'ETH')
        - depth: Whether to include full order book depth

        Returns:
        - Processed option chain data as a pandas DataFrame
        """
        logger.info(f"Fetching option chain data from {exchange} for {currency}")

        loop = self._get_event_loop()

        try:
            option_chain = loop.run_until_complete(
                fetch_option_chain(exchange, currency, depth)
            )
            return option_chain
        except VolyError as e:
            logger.error(f"Error fetching option chain: {str(e)}")
            raise

    # -------------------------------------------------------------------------
    # Black-Scholes and Greeks Calculations
    # -------------------------------------------------------------------------

    @staticmethod
    def bs(s: float, k: float, r: float, vol: float, t: float,
           option_type: str = 'call') -> float:
        """
        Calculate Black-Scholes option price.

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years
        - option_type: 'call' or 'put'

        Returns:
        - Option price
        """
        return bs(s, k, r, vol, t, option_type)

    @staticmethod
    def delta(s: float, k: float, r: float, vol: float, t: float,
              option_type: str = 'call') -> float:
        """
        Calculate option delta.

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years
        - option_type: 'call' or 'put'

        Returns:
        - Delta value
        """
        return delta(s, k, r, vol, t, option_type)

    @staticmethod
    def gamma(s: float, k: float, r: float, vol: float, t: float) -> float:
        """
        Calculate option gamma.

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years

        Returns:
        - Gamma value
        """
        return gamma(s, k, r, vol, t)

    @staticmethod
    def vega(s: float, k: float, r: float, vol: float, t: float) -> float:
        """
        Calculate option vega.

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years

        Returns:
        - Vega value (for 1% change in volatility)
        """
        return vega(s, k, r, vol, t)

    @staticmethod
    def theta(s: float, k: float, r: float, vol: float, t: float,
              option_type: str = 'call') -> float:
        """
        Calculate option theta.

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years
        - option_type: 'call' or 'put'

        Returns:
        - Theta value (per day)
        """
        return theta(s, k, r, vol, t, option_type)

    @staticmethod
    def rho(s: float, k: float, r: float, vol: float, t: float,
            option_type: str = 'call') -> float:
        """
        Calculate option rho.

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years
        - option_type: 'call' or 'put'

        Returns:
        - Rho value (for 1% change in interest rate)
        """
        return rho(s, k, r, vol, t, option_type)

    @staticmethod
    def vanna(s: float, k: float, r: float, vol: float, t: float) -> float:
        """
        Calculate option vanna.

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years

        Returns:
        - Vanna value
        """
        return vanna(s, k, r, vol, t)

    @staticmethod
    def volga(s: float, k: float, r: float, vol: float, t: float) -> float:
        """
        Calculate option volga (vomma).

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years

        Returns:
        - Volga value
        """
        return volga(s, k, r, vol, t)

    @staticmethod
    def charm(s: float, k: float, r: float, vol: float, t: float,
              option_type: str = 'call') -> float:
        """
        Calculate option charm (delta decay).

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years
        - option_type: 'call' or 'put'

        Returns:
        - Charm value (per day)
        """
        return charm(s, k, r, vol, t, option_type)

    @staticmethod
    def greeks(s: float, k: float, r: float, vol: float, t: float,
               option_type: str = 'call') -> Dict[str, float]:
        """
        Calculate all option Greeks.

        Parameters:
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - vol: Volatility
        - t: Time to expiry in years
        - option_type: 'call' or 'put'

        Returns:
        - Dictionary with all Greeks (price, delta, gamma, vega, theta, rho, vanna, volga, charm)
        """
        return greeks(s, k, r, vol, t, option_type)

    @staticmethod
    def iv(option_price: float, s: float, k: float, r: float, t: float,
           option_type: str = 'call') -> float:
        """
        Calculate implied volatility.

        Parameters:
        - option_price: Market price of the option
        - s: Underlying price
        - k: Strike price
        - r: Risk-free rate
        - t: Time to expiry in years
        - option_type: 'call' or 'put'

        Returns:
        - Implied volatility
        """
        return iv(option_price, s, k, r, vol=None, t=t, option_type=option_type)

    # -------------------------------------------------------------------------
    # Model Fitting
    # -------------------------------------------------------------------------

    @staticmethod
    def fit_model(market_data: pd.DataFrame,
                  model_type: str = 'svi',
                  moneyness_range: Tuple[float, float] = (-2, 2),
                  num_points: int = 500,
                  plot: bool = False) -> Dict[str, Any]:
        """
        Fit a volatility model to market data.

        Parameters:
        - market_data: DataFrame with market data
        - model_type: Type of model to fit (default: 'svi')
        - moneyness_range: (min, max) range for moneyness grid
        - num_points: Number of points for moneyness grid
        - plot: Whether to generate and return plots

        Returns:
        - Dictionary with fitting results and optional plots
        """
        logger.info(f"Fitting {model_type.upper()} model to market data")

        # Fit the model
        fit_results = fit_model(
            market_data=market_data,
            model_type=model_type,
            moneyness_range=moneyness_range,
            num_points=num_points
        )

        # Generate plots if requested
        if plot:
            logger.info("Generating model fitting plots")
            plots = generate_all_plots(fit_results, market_data=market_data)
            fit_results['plots'] = plots

        return fit_results

    # -------------------------------------------------------------------------
    # Risk-Neutral Density (RND)
    # -------------------------------------------------------------------------

    @staticmethod
    def rnd(fit_results: Dict[str, Any],
            maturity: Optional[str] = None,
            spot_price: float = 1.0,
            plot: bool = False) -> Dict[str, Any]:
        """
        Calculate risk-neutral density from fitted model.

        Parameters:
        - fit_results: Dictionary with fitting results from fit_model()
        - maturity: Optional maturity name to calculate RND for a specific expiry
        - spot_price: Current spot price
        - plot: Whether to generate and return plots

        Returns:
        - Dictionary with RND results and optional plots
        """
        logger.info("Calculating risk-neutral density")

        # Calculate RND
        rnd_results = calculate_rnd(fit_results, maturity, spot_price)

        # Generate plots if requested
        if plot:
            logger.info("Generating RND plots")
            plots = generate_all_plots(fit_results, rnd_results)
            rnd_results['plots'] = plots

        return rnd_results

    @staticmethod
    def pdf(rnd_results: Dict[str, Any],
            maturity: Optional[str] = None,
            plot: bool = False) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate probability density function (PDF) from RND results.

        Parameters:
        - rnd_results: Dictionary with RND results from rnd()
        - maturity: Optional maturity name for a specific expiry
        - plot: Whether to generate and return a plot

        Returns:
        - Tuple of (prices, pdf_values) and optional plot
        """
        logger.info("Calculating PDF from RND")

        # Extract required data
        moneyness_grid = rnd_results['moneyness_grid']
        rnd_surface = rnd_results['rnd_surface']
        spot_price = rnd_results['spot_price']

        # Select maturity
        if maturity is None:
            # Use first maturity if not specified
            maturity = list(rnd_surface.keys())[0]
        elif maturity not in rnd_surface:
            raise ValidationError(f"Maturity '{maturity}' not found in RND results")

        # Get RND values for the selected maturity
        rnd_values = rnd_surface[maturity]

        # Calculate PDF
        prices, pdf_values = calculate_pdf(moneyness_grid, rnd_values, spot_price)

        result = (prices, pdf_values)

        # Generate plot if requested
        if plot:
            logger.info(f"Generating PDF plot for {maturity}")
            pdf_plot = plot_pdf(
                moneyness_grid, rnd_values, spot_price,
                title=f"Probability Density Function - {maturity}"
            )
            result = (prices, pdf_values, pdf_plot)

        return result

    @staticmethod
    def cdf(rnd_results: Dict[str, Any],
            maturity: Optional[str] = None,
            plot: bool = False) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate cumulative distribution function (CDF) from RND results.

        Parameters:
        - rnd_results: Dictionary with RND results from rnd()
        - maturity: Optional maturity name for a specific expiry
        - plot: Whether to generate and return a plot

        Returns:
        - Tuple of (prices, cdf_values) and optional plot
        """
        logger.info("Calculating CDF from RND")

        # Extract required data
        moneyness_grid = rnd_results['moneyness_grid']
        rnd_surface = rnd_results['rnd_surface']
        spot_price = rnd_results['spot_price']

        # Select maturity
        if maturity is None:
            # Use first maturity if not specified
            maturity = list(rnd_surface.keys())[0]
        elif maturity not in rnd_surface:
            raise ValidationError(f"Maturity '{maturity}' not found in RND results")

        # Get RND values for the selected maturity
        rnd_values = rnd_surface[maturity]

        # Calculate CDF
        prices, cdf_values = calculate_cdf(moneyness_grid, rnd_values, spot_price)

        result = (prices, cdf_values)

        # Generate plot if requested
        if plot:
            logger.info(f"Generating CDF plot for {maturity}")
            cdf_plot = plot_cdf(
                moneyness_grid, rnd_values, spot_price,
                title=f"Cumulative Distribution Function - {maturity}"
            )
            result = (prices, cdf_values, cdf_plot)

        return result

    @staticmethod
    def probability(rnd_results: Dict[str, Any],
                    target_price: float,
                    maturity: Optional[str] = None,
                    direction: str = 'above') -> float:
        """
        Calculate the probability of price being above or below a target price.

        Parameters:
        - rnd_results: Dictionary with RND results from rnd()
        - target_price: Target price level
        - maturity: Optional maturity name for a specific expiry
        - direction: 'above' or 'below'

        Returns:
        - Probability (0 to 1)
        """
        if direction not in ['above', 'below']:
            raise ValidationError("Direction must be 'above' or 'below'")

        # Extract required data
        moneyness_grid = rnd_results['moneyness_grid']
        rnd_surface = rnd_results['rnd_surface']
        spot_price = rnd_results['spot_price']

        # Select maturity
        if maturity is None:
            # Use first maturity if not specified
            maturity = list(rnd_surface.keys())[0]
        elif maturity not in rnd_surface:
            raise ValidationError(f"Maturity '{maturity}' not found in RND results")

        # Get RND values for the selected maturity
        rnd_values = rnd_surface[maturity]

        # Calculate probability
        prob = calculate_strike_probability(
            target_price, moneyness_grid, rnd_values, spot_price, direction
        )

        return prob

    # -------------------------------------------------------------------------
    # Interpolation
    # -------------------------------------------------------------------------

    @staticmethod
    def interpolate(fit_results: Dict[str, Any],
                    specific_days: Optional[List[int]] = None,
                    num_points: int = 10,
                    method: str = 'cubic',
                    plot: bool = False) -> Dict[str, Any]:
        """
        Interpolate a fitted model to specific days to expiry.

        Parameters:
        - fit_results: Dictionary with fitting results from fit_model()
        - specific_days: Optional list of specific days to include (e.g., [7, 30, 90, 180])
        - num_points: Number of points for regular grid if specific_days is None
        - method: Interpolation method ('linear', 'cubic', 'pchip', etc.)
        - plot: Whether to generate and return a plot

        Returns:
        - Dictionary with interpolation results and optional plot
        """
        logger.info(f"Interpolating model with {method} method")

        # Interpolate the model
        interp_results = interpolate_model(
            fit_results, specific_days, num_points, method
        )

        # Generate plot if requested
        if plot:
            logger.info("Generating interpolated surface plot")
            interp_plot = plot_interpolated_surface(interp_results)
            interp_results['plot'] = interp_plot

        return interp_results
