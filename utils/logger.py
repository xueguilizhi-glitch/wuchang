"""Logging configuration."""
import logging
import logging.handlers
import json
from datetime import datetime
from pathlib import Path

# Create logs directory
LOGS_DIR = Path('logs')
LOGS_DIR.mkdir(exist_ok=True)

class JsonFormatter(logging.Formatter):
    """JSON formatter for logging."""
    
    def format(self, record):
        log_dict = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        if record.exc_info:
            log_dict['exception'] = self.formatException(record.exc_info)
        return json.dumps(log_dict)

def setup_logger(name, level=logging.INFO):
    """Setup logger with file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        LOGS_DIR / f'{name}.log',
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(JsonFormatter())
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Create main logger
logger = setup_logger('stock_quant')
