"""
Model fitting and calibration module for the Voly package.

This module handles fitting volatility models to market data and
calculating fitting statistics.
"""

import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Optional, Union, Any
from scipy.optimize import least_squares
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from voly.utils.logger import logger, catch_exception
from voly.exceptions import ModelError, ValidationError
from voly.models import SVIModel


@catch_exception
def calculate_residuals(params: List[float],
                        time_to_expiry: float,
                        market_data: pd.DataFrame,
                        model: Any = SVIModel) -> np.ndarray:
    """
    Calculate the residuals between market and model implied volatilities.

    Parameters:
    - params: Model parameters (e.g., SVI parameters [a, b, sigma, rho, m])
    - time_to_expiry: The time to expiry in years
    - market_data: DataFrame with market data
    - model: Model class to use (default: SVIModel)

    Returns:
    - Array of residuals
    """
    # Filter market data for the specific time to expiry
    specific_expiry_data = market_data[market_data['yte'] == time_to_expiry]

    # Calculate the total implied variance using the model for filtered data
    w_model = np.array([model.svi(x, *params) for x in specific_expiry_data['log_moneyness']])

    # Extract the actual market implied volatilities
    iv_actual = specific_expiry_data['mark_iv'].values

    # Calculate residuals between market implied volatilities and model predictions
    residuals = iv_actual - np.sqrt(w_model / time_to_expiry)

    return residuals


@catch_exception
def optimize_svi_parameters(market_data: pd.DataFrame,
                            initial_params: Optional[List[float]] = None,
                            param_bounds: Optional[Tuple] = None) -> Dict[str, Dict[str, Any]]:
    """
    Optimize SVI parameters for all unique expiries in the market data.

    Parameters:
    - market_data: DataFrame with market data
    - initial_params: Initial guess for SVI parameters (default: from SVIModel)
    - param_bounds: Bounds for parameters (default: from SVIModel)

    Returns:
    - Dictionary of optimization results by maturity name
    """
    results = {}
    unique_expiries = sorted(market_data['yte'].unique())

    # Use defaults if not provided
    if initial_params is None:
        initial_params = SVIModel.DEFAULT_INITIAL_PARAMS

    if param_bounds is None:
        param_bounds = SVIModel.DEFAULT_PARAM_BOUNDS

    for t_dte in unique_expiries:
        # Get maturity name for reporting
        expiry_data = market_data[market_data['yte'] == t_dte]
        maturity_name = expiry_data['maturity_name'].iloc[0]
        dte_value = expiry_data['dte'].iloc[0]

        logger.info(f"Optimizing for {maturity_name} (DTE: {dte_value:.1f}, YTE: {t_dte:.4f})...")

        # Optimize SVI parameters
        try:
            result = least_squares(
                calculate_residuals,
                initial_params,
                args=(t_dte, market_data, SVIModel),
                bounds=param_bounds,
                max_nfev=1000
            )
        except Exception as e:
            raise ModelError(f"Optimization failed for {maturity_name}: {str(e)}")

        # Store results with maturity name as key
        results[maturity_name] = {
            'params': result.x,
            'success': result.success,
            'cost': result.cost,
            'optimality': result.optimality,
            'message': result.message,
            'yte': t_dte,
            'dte': dte_value
        }

        if result.success:
            logger.info(f'Optimization for {maturity_name} (DTE: {dte_value:.1f}): SUCCESS')
        else:
            logger.warning(f'Optimization for {maturity_name} (DTE: {dte_value:.1f}): FAILED')

        logger.info('------------------------------------------')

    return results


@catch_exception
def create_parameters_matrix(optimization_results: Dict[str, Dict[str, Any]]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Create matrices of optimized parameters for each expiry.
    Uses maturity names as column names.

    Parameters:
    - optimization_results: Dictionary of optimization results by maturity name

    Returns:
    - Tuple of DataFrames with optimized parameters:
      1. Raw SVI parameters (a, b, sigma, rho, m)
      2. Jump-Wing parameters (nu, psi, p, c, nu_tilde)
    """
    # Get maturity names in order by DTE
    maturity_names = sorted(optimization_results.keys(),
                            key=lambda x: optimization_results[x]['dte'])

    # Create DataFrame for raw parameters with maturity names as columns
    raw_param_matrix = pd.DataFrame(
        columns=maturity_names,
        index=SVIModel.PARAM_NAMES
    )

    # Create DataFrame for JW parameters
    jw_param_matrix = pd.DataFrame(
        columns=maturity_names,
        index=SVIModel.JW_PARAM_NAMES
    )

    # Store YTE and DTE values for reference
    yte_values = {}
    dte_values = {}

    # Fill the matrices with optimized parameters
    for maturity_name in maturity_names:
        result = optimization_results[maturity_name]

        # Extract raw SVI parameters
        a, b, sigma, rho, m = result['params']
        raw_param_matrix[maturity_name] = [a, b, sigma, rho, m]

        # Get time to expiry
        yte = result['yte']
        yte_values[maturity_name] = yte
        dte_values[maturity_name] = result['dte']

        # Calculate JW parameters
        nu, psi, p, c, nu_tilde = SVIModel.svi_jw_params(a, b, sigma, rho, m, yte)
        jw_param_matrix[maturity_name] = [nu, psi, p, c, nu_tilde]

    # Store YTE and DTE as attributes in all DataFrames for reference
    attrs = {
        'yte_values': yte_values,
        'dte_values': dte_values
    }

    raw_param_matrix.attrs.update(attrs)
    jw_param_matrix.attrs.update(attrs)

    return raw_param_matrix, jw_param_matrix


@catch_exception
def generate_implied_volatility_surface(
        param_matrix: pd.DataFrame,
        moneyness_range: Tuple[float, float] = (-2, 2),
        num_points: int = 500
) -> Tuple[np.ndarray, Dict[float, np.ndarray]]:
    """
    Generate implied volatility surface using optimized SVI parameters.

    Parameters:
    - param_matrix: Matrix of optimized SVI parameters with maturity names as columns
    - moneyness_range: (min, max) range for moneyness grid
    - num_points: Number of points for moneyness grid

    Returns:
    - Moneyness grid and implied volatility surface
    """
    # Generate moneyness grid
    min_m, max_m = moneyness_range
    moneyness_values = np.linspace(min_m, max_m, num=num_points)
    implied_volatility_surface = {}

    # Get YTE values from the parameter matrix attributes
    yte_values = param_matrix.attrs['yte_values']

    # Generate implied volatility for each expiry
    for maturity_name, yte in yte_values.items():
        svi_params = param_matrix[maturity_name].values
        w_svi = [SVIModel.svi(x, *svi_params) for x in moneyness_values]
        implied_volatility_surface[yte] = np.sqrt(np.array(w_svi) / yte)

    return moneyness_values, implied_volatility_surface


@catch_exception
def calculate_fit_statistics(market_data: pd.DataFrame, param_matrix: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate fitting accuracy statistics for each expiry.

    Parameters:
    - market_data: DataFrame with market data
    - param_matrix: Matrix of optimized SVI parameters with maturity names as columns

    Returns:
    - DataFrame with fitting statistics
    """
    # Get YTE values from the parameter matrix attributes
    yte_values = param_matrix.attrs['yte_values']
    dte_values = param_matrix.attrs['dte_values']

    # Initialize lists for statistics
    maturity_name_list = []
    dte_list = []
    yte_list = []
    rmse_list = []
    mae_list = []
    r2_list = []
    max_error_list = []
    num_points_list = []

    # Calculate statistics for each expiry
    for maturity_name, yte in yte_values.items():
        # Filter market data for the specific expiry
        expiry_data = market_data[market_data['yte'] == yte]
        dte_value = dte_values[maturity_name]

        # Calculate SVI model predictions
        svi_params = param_matrix[maturity_name].values
        w_svi = np.array([SVIModel.svi(x, *svi_params) for x in expiry_data['log_moneyness']])
        iv_model = np.sqrt(w_svi / yte)

        # Get actual market implied volatilities
        iv_market = expiry_data['mark_iv'].values

        # Calculate statistics
        rmse = np.sqrt(mean_squared_error(iv_market, iv_model))
        mae = mean_absolute_error(iv_market, iv_model)
        r2 = r2_score(iv_market, iv_model)
        max_error = np.max(np.abs(iv_market - iv_model))
        num_points = len(expiry_data)

        # Append to lists
        maturity_name_list.append(maturity_name)
        dte_list.append(dte_value)
        yte_list.append(yte)
        rmse_list.append(rmse)
        mae_list.append(mae)
        r2_list.append(r2)
        max_error_list.append(max_error)
        num_points_list.append(num_points)

    # Create DataFrame with statistics
    stats_df = pd.DataFrame({
        'Maturity': maturity_name_list,
        'DTE': dte_list,
        'YTE': yte_list,
        'RMSE': rmse_list,
        'MAE': mae_list,
        'R²': r2_list,
        'Max Error': max_error_list,
        'Number of Points': num_points_list
    })

    return stats_df


@catch_exception
def fit_model(market_data: pd.DataFrame,
              model_name: str = 'svi',
              moneyness_range: Tuple[float, float] = (-2, 2),
              num_points: int = 500) -> Dict[str, Any]:
    """
    Fit a volatility model to market data.

    Parameters:
    - market_data: DataFrame with market data
    - model_name: Type of model to fit (default: 'svi')
    - moneyness_range: (min, max) range for moneyness grid
    - num_points: Number of points for moneyness grid

    Returns:
    - Dictionary with fitting results
    """
    if model_name.lower() != 'svi':
        raise ValidationError(f"Model type '{model_name}' is not supported. Currently only 'svi' is available.")

    # Step 1: Optimize model parameters
    optimization_results = optimize_svi_parameters(market_data)

    # Step 2: Create parameter matrices
    raw_param_matrix, jw_param_matrix = create_parameters_matrix(optimization_results)

    # Step 3: Generate implied volatility surface
    moneyness_grid, iv_surface = generate_implied_volatility_surface(
        raw_param_matrix, moneyness_range, num_points
    )

    # Step 4: Calculate fitting statistics
    stats_df = calculate_fit_statistics(market_data, raw_param_matrix)

    # Step 5: Get unique expiries in sorted order (in years)
    unique_expiries_years = np.array(sorted(market_data['yte'].unique()))

    # Return all results in a dictionary
    return {
        'optimization_results': optimization_results,
        'raw_param_matrix': raw_param_matrix,
        'jw_param_matrix': jw_param_matrix,
        'moneyness_grid': moneyness_grid,
        'iv_surface': iv_surface,
        'stats_df': stats_df,
        'unique_expiries': unique_expiries_years,
    }
