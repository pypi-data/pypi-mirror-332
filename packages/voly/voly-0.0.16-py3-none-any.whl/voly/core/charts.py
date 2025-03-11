"""
Visualization module for the Voly package.

This module provides visualization functions for volatility surfaces,
risk-neutral densities, and model fitting results.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional, Union, Any
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from voly.utils.logger import logger, catch_exception
from voly.models import SVIModel

# Set default renderer to browser for interactive plots
pio.renderers.default = "browser"


@catch_exception
def plot_volatility_smile(moneyness: np.ndarray,
                          iv: np.ndarray,
                          market_data: Optional[pd.DataFrame] = None,
                          expiry: Optional[float] = None,
                          title: Optional[str] = None) -> go.Figure:
    """
    Plot volatility smile for a single expiry.

    Parameters:
    - moneyness: Moneyness grid
    - iv: Implied volatility values
    - market_data: Optional market data for comparison
    - expiry: Optional expiry time (in years) for filtering market data
    - title: Optional plot title

    Returns:
    - Plotly figure
    """
    fig = go.Figure()

    # Add model curve
    fig.add_trace(
        go.Scatter(
            x=moneyness,
            y=iv * 100,  # Convert to percentage
            mode='lines',
            name='Model',
            line=dict(color='#00FFC1', width=2)
        )
    )

    # Add market data if provided
    if market_data is not None and expiry is not None:
        # Filter market data for the specific expiry
        expiry_data = market_data[market_data['yte'] == expiry]

        if not expiry_data.empty:
            # Add bid IV
            fig.add_trace(
                go.Scatter(
                    x=expiry_data['log_moneyness'],
                    y=expiry_data['bid_iv'] * 100,  # Convert to percentage
                    mode='markers',
                    name='Bid IV',
                    marker=dict(size=8, symbol='circle', opacity=0.7)
                )
            )

            # Add ask IV
            fig.add_trace(
                go.Scatter(
                    x=expiry_data['log_moneyness'],
                    y=expiry_data['ask_iv'] * 100,  # Convert to percentage
                    mode='markers',
                    name='Ask IV',
                    marker=dict(size=8, symbol='circle', opacity=0.7)
                )
            )

            # Get maturity name and DTE for title if not provided
            if title is None:
                maturity_name = expiry_data['maturity_name'].iloc[0]
                dte_value = expiry_data['dte'].iloc[0]
                title = f'Volatility Smile for {maturity_name} (DTE: {dte_value:.1f}, YTE: {expiry:.4f})'

    # Use default title if not provided
    if title is None:
        title = 'Volatility Smile'

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='Log Moneyness',
        yaxis_title='Implied Volatility (%)',
        template='plotly_dark',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )

    return fig


@catch_exception
def plot_all_smiles(moneyness: np.ndarray,
                    iv_surface: Dict[float, np.ndarray],
                    market_data: Optional[pd.DataFrame] = None) -> List[go.Figure]:
    """
    Plot volatility smiles for all expiries.

    Parameters:
    - moneyness: Moneyness grid
    - iv_surface: Dictionary mapping expiry times to IV arrays
    - market_data: Optional market data for comparison

    Returns:
    - List of Plotly figures
    """
    figures = []

    # Sort expiries in ascending order
    sorted_expiries = sorted(iv_surface.keys())

    # Create a figure for each expiry
    for expiry in sorted_expiries:
        fig = plot_volatility_smile(
            moneyness=moneyness,
            iv=iv_surface[expiry],
            market_data=market_data,
            expiry=expiry
        )
        figures.append(fig)

    return figures


@catch_exception
def plot_parameters(raw_param_matrix: pd.DataFrame,
                    jw_param_matrix: Optional[pd.DataFrame] = None) -> Tuple[go.Figure, Optional[go.Figure]]:
    """
    Plot model parameters across different expiries.

    Parameters:
    - raw_param_matrix: Matrix of raw SVI parameters with maturity names as columns
    - jw_param_matrix: Optional matrix of Jump-Wing parameters

    Returns:
    - Tuple of Plotly figures (raw_params_fig, jw_params_fig)
    """
    # Plot raw SVI parameters
    param_names = raw_param_matrix.index
    raw_fig = make_subplots(rows=3, cols=2, subplot_titles=[f"Parameter {p}: {SVIModel.PARAM_DESCRIPTIONS.get(p, '')}"
                                                            for p in param_names] + [''])

    # Get maturity names (columns) in order
    maturity_names = raw_param_matrix.columns

    # Get YTE and DTE values from attributes
    yte_values = raw_param_matrix.attrs['yte_values']
    dte_values = raw_param_matrix.attrs['dte_values']

    # Create custom x-axis tick labels
    tick_labels = [f"{m} (DTE: {dte_values[m]:.1f}, YTE: {yte_values[m]:.4f})" for m in maturity_names]

    # Plot each parameter
    for i, param in enumerate(param_names):
        row = i // 2 + 1
        col = i % 2 + 1

        raw_fig.add_trace(
            go.Scatter(
                x=list(range(len(maturity_names))),  # Use indices for x-axis positioning
                y=raw_param_matrix.loc[param],
                mode='lines+markers',
                name=param,
                line=dict(width=2),
                marker=dict(size=8),
                text=tick_labels,  # Add hover text
                hovertemplate="%{text}<br>%{y:.4f}"
            ),
            row=row, col=col
        )

        # Update x-axis for this subplot with custom tick labels
        raw_fig.update_xaxes(
            tickvals=list(range(len(maturity_names))),
            ticktext=maturity_names,
            tickangle=45,
            row=row, col=col
        )

    # Update layout for raw parameters
    raw_fig.update_layout(
        title='Raw SVI Parameters Across Expiries',
        template='plotly_dark',
        showlegend=False,
        height=800
    )

    # Plot Jump-Wing parameters if provided
    jw_fig = None
    if jw_param_matrix is not None:
        jw_param_names = jw_param_matrix.index
        jw_fig = make_subplots(rows=3, cols=2,
                               subplot_titles=[f"Parameter {p}: {SVIModel.PARAM_DESCRIPTIONS.get(p, '')}"
                                               for p in jw_param_names] + [''])

        # Plot each JW parameter
        for i, param in enumerate(jw_param_names):
            row = i // 2 + 1
            col = i % 2 + 1

            jw_fig.add_trace(
                go.Scatter(
                    x=list(range(len(maturity_names))),  # Use indices for x-axis positioning
                    y=jw_param_matrix.loc[param],
                    mode='lines+markers',
                    name=param,
                    line=dict(width=2, color='rgb(0, 180, 180)'),
                    marker=dict(size=8),
                    text=tick_labels,  # Add hover text
                    hovertemplate="%{text}<br>%{y:.4f}"
                ),
                row=row, col=col
            )

            # Update x-axis for this subplot with custom tick labels
            jw_fig.update_xaxes(
                tickvals=list(range(len(maturity_names))),
                ticktext=maturity_names,
                tickangle=45,
                row=row, col=col
            )

        # Update layout for JW parameters
        jw_fig.update_layout(
            title='Jump-Wing Parameters Across Expiries',
            template='plotly_dark',
            showlegend=False,
            height=800
        )

    return raw_fig, jw_fig


@catch_exception
def plot_fit_statistics(stats_df: pd.DataFrame) -> go.Figure:
    """
    Plot the fitting accuracy statistics.

    Parameters:
    - stats_df: DataFrame with fitting statistics

    Returns:
    - Plotly figure
    """
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=['RMSE by Expiry', 'MAE by Expiry',
                        'R² by Expiry', 'Max Error by Expiry']
    )

    # Create custom tick labels with maturity name, DTE, and YTE
    tick_labels = [f"{m} (DTE: {d:.1f}, YTE: {y:.4f})" for m, d, y in
                   zip(stats_df['Maturity'], stats_df['DTE'], stats_df['YTE'])]

    # Get x-axis values for plotting (use indices for positioning)
    x_indices = list(range(len(stats_df)))

    # Plot RMSE
    fig.add_trace(
        go.Scatter(
            x=x_indices,
            y=stats_df['RMSE'] * 100,  # Convert to percentage
            mode='lines+markers',
            name='RMSE',
            line=dict(width=2),
            marker=dict(size=8),
            text=tick_labels  # Add hover text
        ),
        row=1, col=1
    )

    # Plot MAE
    fig.add_trace(
        go.Scatter(
            x=x_indices,
            y=stats_df['MAE'] * 100,  # Convert to percentage
            mode='lines+markers',
            name='MAE',
            line=dict(width=2),
            marker=dict(size=8),
            text=tick_labels  # Add hover text
        ),
        row=1, col=2
    )

    # Plot R²
    fig.add_trace(
        go.Scatter(
            x=x_indices,
            y=stats_df['R²'],
            mode='lines+markers',
            name='R²',
            line=dict(width=2),
            marker=dict(size=8),
            text=tick_labels  # Add hover text
        ),
        row=2, col=1
    )

    # Plot Max Error
    fig.add_trace(
        go.Scatter(
            x=x_indices,
            y=stats_df['Max Error'] * 100,  # Convert to percentage
            mode='lines+markers',
            name='Max Error',
            line=dict(width=2),
            marker=dict(size=8),
            text=tick_labels  # Add hover text
        ),
        row=2, col=2
    )

    # Update x-axis for all subplots with maturity names
    for row in range(1, 3):
        for col in range(1, 3):
            fig.update_xaxes(
                tickvals=x_indices,
                ticktext=stats_df['Maturity'],
                tickangle=45,
                row=row, col=col
            )

    # Update y-axis titles
    fig.update_yaxes(title_text='RMSE (%)', row=1, col=1)
    fig.update_yaxes(title_text='MAE (%)', row=1, col=2)
    fig.update_yaxes(title_text='R²', row=2, col=1)
    fig.update_yaxes(title_text='Max Error (%)', row=2, col=2)

    # Update layout
    fig.update_layout(
        title='Model Fitting Accuracy Statistics',
        template='plotly_dark',
        showlegend=False
    )

    return fig


@catch_exception
def plot_3d_surface(moneyness: np.ndarray,
                    expiries: np.ndarray,
                    iv_surface: Dict[float, np.ndarray],
                    interpolate: bool = True,
                    title: str = 'Implied Volatility Surface') -> go.Figure:
    """
    Plot 3D implied volatility surface.

    Parameters:
    - moneyness: Moneyness grid
    - expiries: Expiry times in years
    - iv_surface: Dictionary mapping expiry times to IV arrays
    - interpolate: Whether to interpolate the surface
    - title: Plot title

    Returns:
    - Plotly figure
    """
    # Convert implied volatility surface to array
    z_array = np.array([iv_surface[t] for t in expiries])

    # Create mesh grid
    X, Y = np.meshgrid(moneyness, expiries)
    Z = z_array * 100  # Convert to percentage

    # Create 3D surface plot
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='tealgrn')])

    # Add colorbar
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                      highlightcolor="limegreen", project_z=True))

    # Update layout
    fig.update_layout(
        title=title,
        template='plotly_dark',
        scene=dict(
            xaxis_title='Log Moneyness',
            yaxis_title='Time to Expiry (years)',
            zaxis_title='Implied Volatility (%)'
        ),
        margin=dict(l=65, r=50, b=65, t=90)
    )

    return fig


@catch_exception
def plot_rnd(moneyness_grid: np.ndarray,
             rnd_values: np.ndarray,
             spot_price: float = 1.0,
             title: str = 'Risk-Neutral Density') -> go.Figure:
    """
    Plot risk-neutral density (RND).

    Parameters:
    - moneyness_grid: Grid of log-moneyness values
    - rnd_values: RND values
    - spot_price: Spot price for converting to absolute prices
    - title: Plot title

    Returns:
    - Plotly figure
    """
    # Create figure
    fig = go.Figure()

    # Convert to prices and normalize RND
    prices = spot_price * np.exp(moneyness_grid)

    # Normalize the RND to integrate to 1
    dx = moneyness_grid[1] - moneyness_grid[0]
    total_density = np.sum(rnd_values) * dx
    normalized_rnd = rnd_values / total_density if total_density > 0 else rnd_values

    # Add trace
    fig.add_trace(
        go.Scatter(
            x=prices,
            y=normalized_rnd,
            mode='lines',
            name='RND',
            line=dict(color='#00FFC1', width=2),
            fill='tozeroy',
            fillcolor='rgba(0, 255, 193, 0.2)'
        )
    )

    # Add vertical line at spot price
    fig.add_shape(
        type='line',
        x0=spot_price, y0=0,
        x1=spot_price, y1=max(normalized_rnd) * 1.1,
        line=dict(color='red', width=2, dash='dash')
    )

    # Add annotation for spot price
    fig.add_annotation(
        x=spot_price,
        y=max(normalized_rnd) * 1.15,
        text=f"Spot: {spot_price}",
        showarrow=False,
        font=dict(color='red')
    )

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='Price',
        yaxis_title='Density',
        template='plotly_dark',
        showlegend=False
    )

    return fig


@catch_exception
def plot_rnd_all_expiries(moneyness_grid: np.ndarray,
                          rnd_surface: Dict[str, np.ndarray],
                          param_matrix: pd.DataFrame,
                          spot_price: float = 1.0) -> go.Figure:
    """
    Plot risk-neutral densities for all expiries.

    Parameters:
    - moneyness_grid: Grid of log-moneyness values
    - rnd_surface: Dictionary mapping maturity names to RND arrays
    - param_matrix: Matrix containing model parameters with maturity info
    - spot_price: Spot price for converting to absolute prices

    Returns:
    - Plotly figure
    """
    # Get maturity information
    dte_values = param_matrix.attrs['dte_values']

    # Create figure
    fig = go.Figure()

    # Get maturity names in order by DTE
    maturity_names = sorted(rnd_surface.keys(), key=lambda x: dte_values[x])

    # Create color scale from purple to green
    n_maturities = len(maturity_names)
    colors = [f'rgb({int(255 - i * 255 / n_maturities)}, {int(i * 255 / n_maturities)}, 255)'
              for i in range(n_maturities)]

    # Convert to prices
    prices = spot_price * np.exp(moneyness_grid)

    # Add traces for each expiry
    for i, maturity_name in enumerate(maturity_names):
        rnd = rnd_surface[maturity_name]
        dte = dte_values[maturity_name]

        # Normalize the RND
        dx = moneyness_grid[1] - moneyness_grid[0]
        total_density = np.sum(rnd) * dx
        normalized_rnd = rnd / total_density if total_density > 0 else rnd

        # Add trace
        fig.add_trace(
            go.Scatter(
                x=prices,
                y=normalized_rnd,
                mode='lines',
                name=f"{maturity_name} (DTE: {dte:.1f})",
                line=dict(color=colors[i], width=2),
            )
        )

    # Add vertical line at spot price
    fig.add_shape(
        type='line',
        x0=spot_price, y0=0,
        x1=spot_price, y1=1,  # Will be scaled automatically
        line=dict(color='red', width=2, dash='dash')
    )

    # Update layout
    fig.update_layout(
        title="Risk-Neutral Densities Across Expiries",
        xaxis_title='Price',
        yaxis_title='Density',
        template='plotly_dark',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    return fig


@catch_exception
def plot_rnd_3d(moneyness_grid: np.ndarray,
                rnd_surface: Dict[str, np.ndarray],
                param_matrix: pd.DataFrame,
                spot_price: float = 1.0) -> go.Figure:
    """
    Plot 3D surface of risk-neutral densities.

    Parameters:
    - moneyness_grid: Grid of log-moneyness values
    - rnd_surface: Dictionary mapping maturity names to RND arrays
    - param_matrix: Matrix containing model parameters with maturity info
    - spot_price: Spot price for converting to absolute prices

    Returns:
    - Plotly figure
    """
    # Get maturity information
    dte_values = param_matrix.attrs['dte_values']

    # Get maturity names in order by DTE
    maturity_names = sorted(rnd_surface.keys(), key=lambda x: dte_values[x])

    # Extract DTE values for z-axis
    dte_list = [dte_values[name] for name in maturity_names]

    # Convert to prices
    prices = spot_price * np.exp(moneyness_grid)

    # Create z-data matrix and normalize RNDs
    z_data = np.zeros((len(maturity_names), len(prices)))

    for i, name in enumerate(maturity_names):
        rnd = rnd_surface[name]

        # Normalize the RND
        dx = moneyness_grid[1] - moneyness_grid[0]
        total_density = np.sum(rnd) * dx
        normalized_rnd = rnd / total_density if total_density > 0 else rnd

        z_data[i] = normalized_rnd

    # Create mesh grid
    X, Y = np.meshgrid(prices, dte_list)

    # Create 3D surface
    fig = go.Figure(data=[
        go.Surface(
            z=z_data,
            x=X,
            y=Y,
            colorscale='Viridis',
            showscale=True
        )
    ])

    # Update layout
    fig.update_layout(
        title="3D Risk-Neutral Density Surface",
        scene=dict(
            xaxis_title="Price",
            yaxis_title="Days to Expiry",
            zaxis_title="Density"
        ),
        margin=dict(l=65, r=50, b=65, t=90),
        template="plotly_dark"
    )

    return fig


@catch_exception
def plot_rnd_statistics(rnd_statistics: pd.DataFrame,
                        rnd_probabilities: pd.DataFrame) -> Tuple[go.Figure, go.Figure]:
    """
    Plot RND statistics and probabilities.

    Parameters:
    - rnd_statistics: DataFrame with RND statistics
    - rnd_probabilities: DataFrame with RND probabilities

    Returns:
    - Tuple of (statistics_fig, probabilities_fig)
    """
    # Create subplot figure for key statistics
    stats_fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=("Standard Deviation (%) vs. DTE",
                        "Skewness vs. DTE",
                        "Excess Kurtosis vs. DTE")
    )

    # Add traces for each statistic
    stats_fig.add_trace(
        go.Scatter(
            x=rnd_statistics["dte"],
            y=rnd_statistics["std_dev_pct"],
            mode="lines+markers",
            name="Standard Deviation (%)",
            hovertemplate="DTE: %{x:.1f}<br>Std Dev: %{y:.2f}%"
        ),
        row=1, col=1
    )

    stats_fig.add_trace(
        go.Scatter(
            x=rnd_statistics["dte"],
            y=rnd_statistics["skewness"],
            mode="lines+markers",
            name="Skewness",
            hovertemplate="DTE: %{x:.1f}<br>Skewness: %{y:.4f}"
        ),
        row=1, col=2
    )

    stats_fig.add_trace(
        go.Scatter(
            x=rnd_statistics["dte"],
            y=rnd_statistics["excess_kurtosis"],
            mode="lines+markers",
            name="Excess Kurtosis",
            hovertemplate="DTE: %{x:.1f}<br>Excess Kurtosis: %{y:.4f}"
        ),
        row=1, col=3
    )

    # Update layout
    stats_fig.update_layout(
        title="Risk-Neutral Density Statistics Across Expiries",
        template="plotly_dark",
        height=500,
        showlegend=False
    )

    # Update axes
    stats_fig.update_xaxes(title_text="Days to Expiry", row=1, col=1)
    stats_fig.update_xaxes(title_text="Days to Expiry", row=1, col=2)
    stats_fig.update_xaxes(title_text="Days to Expiry", row=1, col=3)

    stats_fig.update_yaxes(title_text="Standard Deviation (%)", row=1, col=1)
    stats_fig.update_yaxes(title_text="Skewness", row=1, col=2)
    stats_fig.update_yaxes(title_text="Excess Kurtosis", row=1, col=3)

    # Create a second figure for probability thresholds
    prob_fig = go.Figure()

    # Get probability columns (those starting with "p_")
    prob_cols = [col for col in rnd_probabilities.columns if col.startswith("p_")]

    # Sort the columns to ensure they're in order by threshold value
    prob_cols_above = sorted([col for col in prob_cols if "above" in col],
                             key=lambda x: float(x.split("_")[2]))
    prob_cols_below = sorted([col for col in prob_cols if "below" in col],
                             key=lambda x: float(x.split("_")[2]))

    # Color gradients
    green_colors = [
        'rgba(144, 238, 144, 1)',  # Light green
        'rgba(50, 205, 50, 1)',  # Lime green
        'rgba(34, 139, 34, 1)',  # Forest green
        'rgba(0, 100, 0, 1)'  # Dark green
    ]

    red_colors = [
        'rgba(139, 0, 0, 1)',  # Dark red
        'rgba(220, 20, 60, 1)',  # Crimson
        'rgba(240, 128, 128, 1)',  # Light coral
        'rgba(255, 182, 193, 1)'  # Light pink/red
    ]

    # Add lines for upside probabilities (green)
    for i, col in enumerate(prob_cols_above):
        threshold = float(col.split("_")[2])
        label = f"P(X > {threshold})"

        # Select color based on how far OTM
        color_idx = min(i, len(green_colors) - 1)

        prob_fig.add_trace(
            go.Scatter(
                x=rnd_probabilities["dte"],
                y=rnd_probabilities[col] * 100,  # Convert to percentage
                mode="lines+markers",
                name=label,
                line=dict(color=green_colors[color_idx], width=3),
                marker=dict(size=8, color=green_colors[color_idx]),
                hovertemplate="DTE: %{x:.1f}<br>" + label + ": %{y:.2f}%"
            )
        )

    # Add lines for downside probabilities (red)
    for i, col in enumerate(prob_cols_below):
        threshold = float(col.split("_")[2])
        label = f"P(X < {threshold})"

        # Select color based on how far OTM
        color_idx = min(i, len(red_colors) - 1)

        prob_fig.add_trace(
            go.Scatter(
                x=rnd_probabilities["dte"],
                y=rnd_probabilities[col] * 100,  # Convert to percentage
                mode="lines+markers",
                name=label,
                line=dict(color=red_colors[color_idx], width=3),
                marker=dict(size=8, color=red_colors[color_idx]),
                hovertemplate="DTE: %{x:.1f}<br>" + label + ": %{y:.2f}%"
            )
        )

    # Update layout
    prob_fig.update_layout(
        title="Probability Thresholds Across Expiries",
        xaxis_title="Days to Expiry",
        yaxis_title="Probability (%)",
        template="plotly_dark",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        )
    )

    return stats_fig, prob_fig


@catch_exception
def plot_cdf(moneyness_grid: np.ndarray,
             rnd_values: np.ndarray,
             spot_price: float = 1.0,
             title: str = 'Cumulative Distribution Function') -> go.Figure:
    """
    Plot the cumulative distribution function (CDF) from RND values.

    Parameters:
    - moneyness_grid: Grid of log-moneyness values
    - rnd_values: RND values
    - spot_price: Spot price for converting to absolute prices
    - title: Plot title

    Returns:
    - Plotly figure
    """
    # Convert to prices and normalize RND
    prices = spot_price * np.exp(moneyness_grid)

    # Normalize the RND
    dx = moneyness_grid[1] - moneyness_grid[0]
    total_density = np.sum(rnd_values) * dx
    normalized_rnd = rnd_values / total_density if total_density > 0 else rnd_values

    # Calculate CDF
    cdf = np.cumsum(normalized_rnd) * dx

    # Create figure
    fig = go.Figure()

    # Add CDF trace
    fig.add_trace(
        go.Scatter(
            x=prices,
            y=cdf,
            mode='lines',
            name='CDF',
            line=dict(color='#00FFC1', width=2)
        )
    )

    # Add vertical line at spot price
    fig.add_shape(
        type='line',
        x0=spot_price, y0=0,
        x1=spot_price, y1=1,
        line=dict(color='red', width=2, dash='dash')
    )

    # Add horizontal line at CDF=0.5 (median)
    fig.add_shape(
        type='line',
        x0=prices[0], y0=0.5,
        x1=prices[-1], y1=0.5,
        line=dict(color='orange', width=2, dash='dash')
    )

    # Add annotation for spot price
    fig.add_annotation(
        x=spot_price,
        y=1.05,
        text=f"Spot: {spot_price}",
        showarrow=False,
        font=dict(color='red')
    )

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='Price',
        yaxis_title='Cumulative Probability',
        template='plotly_dark',
        yaxis=dict(range=[0, 1.1]),
        showlegend=False
    )

    return fig


@catch_exception
def plot_pdf(moneyness_grid: np.ndarray,
             rnd_values: np.ndarray,
             spot_price: float = 1.0,
             title: str = 'Probability Density Function') -> go.Figure:
    """
    Plot the probability density function (PDF) from RND values.

    Parameters:
    - moneyness_grid: Grid of log-moneyness values
    - rnd_values: RND values
    - spot_price: Spot price for converting to absolute prices
    - title: Plot title

    Returns:
    - Plotly figure
    """
    # This is essentially the same as plot_rnd but with a different title
    return plot_rnd(moneyness_grid, rnd_values, spot_price, title)


@catch_exception
def plot_interpolated_surface(
        interp_results: Dict[str, Any],
        title: str = 'Interpolated Implied Volatility Surface'
) -> go.Figure:
    """
    Plot interpolated implied volatility surface.

    Parameters:
    - interp_results: Dictionary with interpolation results
    - title: Plot title

    Returns:
    - Plotly figure
    """
    # Extract data from interpolation results
    moneyness_grid = interp_results['moneyness_grid']
    target_expiries_years = interp_results['target_expiries_years']
    iv_surface = interp_results['iv_surface']

    # Create a 3D surface plot
    fig = plot_3d_surface(
        moneyness=moneyness_grid,
        expiries=target_expiries_years,
        iv_surface=iv_surface,
        title=title
    )

    return fig


@catch_exception
def generate_all_plots(fit_results: Dict[str, Any],
                       rnd_results: Optional[Dict[str, Any]] = None,
                       market_data: Optional[pd.DataFrame] = None) -> Dict[str, go.Figure]:
    """
    Generate all plots for the fitted model and RND results.

    Parameters:
    - fit_results: Dictionary with fitting results from fit_model()
    - rnd_results: Optional dictionary with RND results from calculate_rnd()
    - market_data: Optional market data for comparison

    Returns:
    - Dictionary of plot figures
    """
    plots = {}

    # Extract data from fit results
    moneyness_grid = fit_results['moneyness_grid']
    iv_surface = fit_results['iv_surface']
    raw_param_matrix = fit_results['raw_param_matrix']
    jw_param_matrix = fit_results.get('jw_param_matrix')
    stats_df = fit_results.get('stats_df')
    unique_expiries = fit_results['unique_expiries']

    # Plot volatility smiles
    logger.info("Generating volatility smile plots...")
    plots['smiles'] = plot_all_smiles(moneyness_grid, iv_surface, market_data)

    # Plot 3D surface
    logger.info("Generating 3D volatility surface plot...")
    plots['surface_3d'] = plot_3d_surface(moneyness_grid, unique_expiries, iv_surface)

    # Plot parameters
    logger.info("Generating parameter plots...")
    plots['raw_params'], plots['jw_params'] = plot_parameters(raw_param_matrix, jw_param_matrix)

    # Plot fit statistics if available
    if stats_df is not None:
        logger.info("Generating fit statistics plot...")
        plots['fit_stats'] = plot_fit_statistics(stats_df)

    # Plot RND results if available
    if rnd_results is not None:
        logger.info("Generating RND plots...")

        # Extract RND data
        rnd_surface = rnd_results['rnd_surface']
        rnd_statistics = rnd_results['rnd_statistics']
        rnd_probabilities = rnd_results['rnd_probabilities']
        spot_price = rnd_results['spot_price']

        # Plot RND for each expiry
        plots['rnd'] = {}
        for maturity_name, rnd_values in rnd_surface.items():
            plots['rnd'][maturity_name] = plot_rnd(
                moneyness_grid, rnd_values, spot_price,
                title=f"Risk-Neutral Density - {maturity_name}"
            )

        # Plot all RNDs in one figure
        plots['rnd_all'] = plot_rnd_all_expiries(moneyness_grid, rnd_surface, raw_param_matrix, spot_price)

        # Plot 3D RND surface
        plots['rnd_3d'] = plot_rnd_3d(moneyness_grid, rnd_surface, raw_param_matrix, spot_price)

        # Plot RND statistics
        plots['rnd_stats'], plots['rnd_probs'] = plot_rnd_statistics(rnd_statistics, rnd_probabilities)

        # Plot PDF and CDF for the first expiry
        first_maturity = list(rnd_surface.keys())[0]
        first_rnd = rnd_surface[first_maturity]

        plots['pdf'] = plot_pdf(moneyness_grid, first_rnd, spot_price)
        plots['cdf'] = plot_cdf(moneyness_grid, first_rnd, spot_price)

    return plots
