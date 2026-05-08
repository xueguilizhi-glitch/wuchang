"""Configuration management."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Base configuration."""
    
    # Application
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    TESTING = False
    
    # Data sources
    YAHOO_FINANCE_ENABLED = os.getenv('YAHOO_FINANCE_ENABLED', 'True') == 'True'
    AKSHARE_ENABLED = os.getenv('AKSHARE_ENABLED', 'True') == 'True'
    WIND_API_ENABLED = os.getenv('WIND_API_ENABLED', 'False') == 'True'
    WIND_API_KEY = os.getenv('WIND_API_KEY', '')
    
    # Trading
    INITIAL_CAPITAL = float(os.getenv('INITIAL_CAPITAL', '100000'))
    COMMISSION = float(os.getenv('COMMISSION', '0.001'))
    SLIPPAGE = float(os.getenv('SLIPPAGE', '0.0001'))
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///quant_trading.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Redis
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # Broker
    FUTU_ENABLED = os.getenv('FUTU_ENABLED', 'False') == 'True'
    FUTU_ACCOUNT_ID = os.getenv('FUTU_ACCOUNT_ID', '')
    FUTU_PASSWORD = os.getenv('FUTU_PASSWORD', '')
    
    BINANCE_ENABLED = os.getenv('BINANCE_ENABLED', 'False') == 'True'
    BINANCE_API_KEY = os.getenv('BINANCE_API_KEY', '')
    BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET', '')
    
    # Risk Management
    MAX_POSITION_SIZE = float(os.getenv('MAX_POSITION_SIZE', '0.1'))  # 10% of capital
    MAX_LEVERAGE = float(os.getenv('MAX_LEVERAGE', '1.0'))
    STOP_LOSS_PCT = float(os.getenv('STOP_LOSS_PCT', '0.05'))  # 5%
    TAKE_PROFIT_PCT = float(os.getenv('TAKE_PROFIT_PCT', '0.1'))  # 10%
    
    # Backtesting
    BACKTEST_START_DATE = os.getenv('BACKTEST_START_DATE', '2020-01-01')
    BACKTEST_END_DATE = os.getenv('BACKTEST_END_DATE', '2024-12-31')
    BACKTEST_MODE = os.getenv('BACKTEST_MODE', 'daily')  # daily, hourly, minute
    
    # Optimization
    OPTIMIZATION_METHOD = os.getenv('OPTIMIZATION_METHOD', 'bayes')  # bayes, grid, random
    OPTIMIZATION_JOBS = int(os.getenv('OPTIMIZATION_JOBS', '-1'))
    
    # API
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('API_PORT', '5000'))
    API_DEBUG = os.getenv('API_DEBUG', 'False') == 'True'

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    
class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'

# Get configuration based on environment
config_name = os.getenv('FLASK_ENV', 'development')
if config_name == 'production':
    config = ProductionConfig()
elif config_name == 'testing':
    config = TestingConfig()
else:
    config = DevelopmentConfig()
