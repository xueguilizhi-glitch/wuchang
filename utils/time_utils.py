"""Time utility functions."""
import pandas as pd
from datetime import datetime, timedelta
import pytz

def get_trading_dates(start_date, end_date, market='CN'):
    """Get trading dates excluding weekends and holidays."""
    # Create date range
    date_range = pd.date_range(start=start_date, end=end_date, freq='B')  # B = business day
    
    # TODO: Remove holidays based on market
    if market == 'CN':
        # Chinese stock market holidays
        holidays = [
            # Spring Festival
            '2024-02-10', '2024-02-11', '2024-02-12', '2024-02-13', '2024-02-14',
            '2024-02-15', '2024-02-16', '2024-02-17',
            # Qingming Festival
            '2024-04-04', '2024-04-05', '2024-04-06',
            # Dragon Boat Festival
            '2024-06-10',
            # Mid-Autumn Festival
            '2024-09-15', '2024-09-16', '2024-09-17',
            # National Day
            '2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-05', '2024-10-06', '2024-10-07',
        ]
        holidays = pd.to_datetime(holidays)
        date_range = date_range[~date_range.isin(holidays)]
    
    return date_range

def is_trading_time(dt, market='CN'):
    """Check if the given datetime is a trading time."""
    if market == 'CN':
        # Chinese stock market trading hours: 09:30-11:30, 13:00-15:00
        hour = dt.hour
        minute = dt.minute
        
        morning = (9 <= hour < 11) or (hour == 11 and minute < 30)
        afternoon = 13 <= hour < 15
        
        return (morning or afternoon) and dt.weekday() < 5  # Monday to Friday
    
    elif market == 'US':
        # US stock market trading hours: 09:30-16:00 EST
        tz = pytz.timezone('US/Eastern')
        dt_us = dt.astimezone(tz)
        hour = dt_us.hour
        minute = dt_us.minute
        
        return (9 <= hour < 16) or (hour == 9 and minute >= 30) and dt_us.weekday() < 5
    
    return True

def get_market_hours(market='CN'):
    """Get market trading hours."""
    if market == 'CN':
        return {
            'open': '09:30',
            'close': '15:00',
            'break_start': '11:30',
            'break_end': '13:00',
        }
    elif market == 'US':
        return {
            'open': '09:30',
            'close': '16:00',
        }
    return {}

def get_next_trading_day(date, market='CN', skip_days=1):
    """Get next trading day."""
    current = pd.Timestamp(date)
    
    for _ in range(skip_days * 2):  # Max 2 * skip_days iterations
        current += timedelta(days=1)
        
        # Check if it's a business day and not a holiday
        if current.weekday() < 5:  # Monday to Friday
            if market == 'CN':
                # TODO: Check against Chinese holidays
                pass
            return current
    
    return current

def get_previous_trading_day(date, market='CN', skip_days=1):
    """Get previous trading day."""
    current = pd.Timestamp(date)
    
    for _ in range(skip_days * 2):
        current -= timedelta(days=1)
        
        if current.weekday() < 5:
            if market == 'CN':
                # TODO: Check against Chinese holidays
                pass
            return current
    
    return current
