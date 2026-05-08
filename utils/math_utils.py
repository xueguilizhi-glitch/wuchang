"""Mathematical utility functions."""
import numpy as np
from typing import Union, List

def calculate_compound_return(returns: Union[List, np.ndarray]) -> float:
    """Calculate compound return rate."""
    returns = np.array(returns)
    return np.prod(1 + returns) - 1

def calculate_log_return(prices: Union[List, np.ndarray]) -> np.ndarray:
    """Calculate log returns."""
    prices = np.array(prices)
    return np.diff(np.log(prices))

def calculate_drawdown(returns: Union[List, np.ndarray]) -> tuple:
    """Calculate drawdown metrics.
    
    Returns:
        (max_drawdown, drawdown_duration, drawdown_series)
    """
    cumulative_returns = np.cumprod(1 + np.array(returns)) - 1
    cummax = np.maximum.accumulate(cumulative_returns)
    drawdown = (cumulative_returns - cummax) / (1 + cummax)
    
    max_drawdown = np.min(drawdown)
    
    # Calculate drawdown duration
    drawdown_array = drawdown < -0.0001  # Threshold to avoid floating point errors
    drawdown_groups = np.diff(np.concatenate(([0], drawdown_array.astype(int), [0])))
    group_starts = np.where(drawdown_groups == 1)[0]
    group_ends = np.where(drawdown_groups == -1)[0]
    
    if len(group_starts) > 0:
        drawdown_durations = group_ends - group_starts
        max_drawdown_duration = np.max(drawdown_durations)
    else:
        max_drawdown_duration = 0
    
    return max_drawdown, max_drawdown_duration, drawdown

def calculate_volatility(returns: Union[List, np.ndarray], periods=252) -> float:
    """Calculate annualized volatility."""
    returns = np.array(returns)
    daily_volatility = np.std(returns)
    return daily_volatility * np.sqrt(periods)

def calculate_sharpe_ratio(returns: Union[List, np.ndarray], 
                          risk_free_rate: float = 0.02, 
                          periods: int = 252) -> float:
    """Calculate Sharpe ratio."""
    returns = np.array(returns)
    excess_returns = returns - risk_free_rate / periods
    if np.std(excess_returns) == 0:
        return 0
    return np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(periods)

def calculate_sortino_ratio(returns: Union[List, np.ndarray],
                           risk_free_rate: float = 0.02,
                           periods: int = 252) -> float:
    """Calculate Sortino ratio (only consider downside risk)."""
    returns = np.array(returns)
    excess_returns = returns - risk_free_rate / periods
    downside_returns = excess_returns[excess_returns < 0]
    
    if len(downside_returns) == 0:
        return 0
    
    downside_std = np.std(downside_returns)
    if downside_std == 0:
        return 0
    
    return np.mean(excess_returns) / downside_std * np.sqrt(periods)

def calculate_calmar_ratio(returns: Union[List, np.ndarray],
                          periods: int = 252) -> float:
    """Calculate Calmar ratio."""
    returns = np.array(returns)
    annual_return = np.mean(returns) * periods
    max_dd, _, _ = calculate_drawdown(returns)
    
    if abs(max_dd) == 0:
        return 0
    
    return annual_return / abs(max_dd)

def calculate_information_ratio(returns: Union[List, np.ndarray],
                               benchmark_returns: Union[List, np.ndarray],
                               periods: int = 252) -> float:
    """Calculate Information ratio."""
    returns = np.array(returns)
    benchmark_returns = np.array(benchmark_returns)
    
    excess_returns = returns - benchmark_returns
    if np.std(excess_returns) == 0:
        return 0
    return np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(periods)

def calculate_var(returns: Union[List, np.ndarray], confidence: float = 0.95) -> float:
    """Calculate Value at Risk."""
    returns = np.array(returns)
    return np.percentile(returns, (1 - confidence) * 100)

def calculate_cvar(returns: Union[List, np.ndarray], confidence: float = 0.95) -> float:
    """Calculate Conditional Value at Risk (Expected Shortfall)."""
    returns = np.array(returns)
    var = calculate_var(returns, confidence)
    return returns[returns <= var].mean()

def kelly_criterion(win_rate: float, avg_win: float, avg_loss: float) -> float:
    """Calculate optimal position size using Kelly Criterion.
    
    Args:
        win_rate: Win rate (0-1)
        avg_win: Average winning trade
        avg_loss: Average losing trade (as positive value)
    
    Returns:
        Optimal allocation percentage
    """
    loss_rate = 1 - win_rate
    
    if avg_loss == 0 or (win_rate * avg_win + loss_rate * (-avg_loss)) <= 0:
        return 0
    
    f = (win_rate * avg_win - loss_rate * avg_loss) / avg_win
    return max(0, min(f, 0.25))  # Cap at 25% for safety

def calculate_omega_ratio(returns: Union[List, np.ndarray],
                         threshold: float = 0.0) -> float:
    """Calculate Omega ratio."""
    returns = np.array(returns)
    excess_returns = returns - threshold
    
    positive = np.sum(excess_returns[excess_returns > 0])
    negative = -np.sum(excess_returns[excess_returns < 0])
    
    if negative == 0:
        return 0
    
    return positive / negative
