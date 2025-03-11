import os
import logging
import platform
from datetime import datetime
from colorama import init, Fore, Style

class ColorPaws:
    """Copyright (C) 2025 Ikmal Said. All rights reserved."""
    class ColorFormatter(logging.Formatter):
        """Custom formatter that adds colors to log levels"""
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            # Initialize colorama for Windows support
            if platform.system() == 'Windows':
                init()
            
        colors = {
            'DEBUG': Fore.LIGHTCYAN_EX,
            'INFO': Fore.LIGHTGREEN_EX,
            'WARNING': Fore.LIGHTYELLOW_EX,
            'ERROR': Fore.LIGHTRED_EX,
            'CRITICAL': Fore.LIGHTMAGENTA_EX,
            'RESET': Style.RESET_ALL,
        }
        
        def format(self, record):
            """Format the log record with colors"""
            original_levelname = record.levelname
            record.levelname = f"{self.colors.get(record.levelname, self.colors['RESET'])}{record.levelname}{self.colors['RESET']}"
            formatted_message = super().format(record)
            record.levelname = original_levelname
            return formatted_message

    def __init__(self, name: str, log_on: bool = True, log_to: str = None):
        """
        Initialize a new ColorPaws logger instance.

        Parameters:
        - name (str): Name for the logger instance
        - log_on (bool): Enable logging
        - log_to (str): Directory to save logs
        """
        self.logger = logging.getLogger(name)
        
        if not self.logger.handlers:  # Only add handlers if they don't exist
            formatter = self.ColorFormatter(
                fmt="%(asctime)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            
            if log_on:
                # Add console handler
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(formatter)
                self.logger.addHandler(console_handler)
                
                # Add file handler if log_dir is provided
                if log_to:
                    dated_log_dir = os.path.join(log_to, datetime.now().strftime('%Y-%m-%d'))
                    time_prefix = datetime.now().strftime("%Y%m%d_%H%M%S%f")[:17]
                    os.makedirs(dated_log_dir, exist_ok=True)
                    
                    file_handler = logging.FileHandler(
                        f"{dated_log_dir}/{time_prefix}_{name}.log",
                        mode="a"
                    )
                    file_handler.setFormatter(formatter)
                    self.logger.addHandler(file_handler)
                
                self.logger.setLevel(logging.DEBUG)

    def __getattr__(self, name):
        """Delegate any unknown attributes/methods to the logger instance"""
        return getattr(self.logger, name)