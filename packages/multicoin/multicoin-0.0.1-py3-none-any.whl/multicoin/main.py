"""Multicoin PyPi Module

This module provides basic utilities for the Multicoin package.
"""

import altcolor
import fancyutil

# Module Metadata
__title__ = "multicoin"
__version__ = "0.0.1"
__author__ = "Taireru LLC"
__license__ = "MIT"

# Global State
_initialized = False

def _ensure_initialized() -> None:
    """Raise an error if the module has not been initialized."""
    if not _initialized:
        raise RuntimeError("The 'multicoin' module must be initialized before use.")

def init(display_credits: bool = True) -> None:
    """Initialize the module. This should be called before using any functionality."""
    global _initialized
    if _initialized:
        return
    _initialized = True
    altcolor.init(show_credits=False)
    
    if display_credits:
        print(f"--++ {__title__.capitalize()} v{__version__} ++--")
        print("Copyright (c) 2025 Taireru LLC")
        print("All rights reserved.")
        print(f"This software is licensed under the {__license__} License.")

def warn(message: str) -> None:
    """Display a warning message."""
    _ensure_initialized()
    altcolor.cPrint(color="YELLOW", text=f"[WARNING]: {message}", style="Fore", objective="controlled")

def clear() -> None:
    """Clear the console screen."""
    _ensure_initialized()
    fancyutil.clear()