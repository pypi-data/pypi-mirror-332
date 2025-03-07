"""
Configuration module for Aitronos package.
"""

import os
from typing import Optional

class AitronosConfig:
    """Configuration class for Aitronos package."""
    
    _is_staging: bool = False
    _base_domain: str = "aitronos.ch" if _is_staging else "aitronos.com"
    
    @classmethod
    def set_staging_mode(cls, enabled: bool = True) -> None:
        """
        Set the staging mode which determines the base domain.
        
        Args:
            enabled (bool): Whether to enable staging mode. Defaults to True.
        """
        cls._is_staging = enabled
        cls._base_domain = "aitronos.ch" if enabled else "aitronos.com"
    
    @classmethod
    def get_base_url(cls, version: Optional[str] = None) -> str:
        """
        Get the base URL for API requests.
        
        Args:
            version (Optional[str]): API version (e.g., 'v1'). If provided, will be included in the URL.
            
        Returns:
            str: The complete base URL
        """
        base = f"https://freddy-api.{cls._base_domain}"
        if version:
            return f"{base}/{version}"
        return base
    
    @classmethod
    def is_staging(cls) -> bool:
        """
        Check if staging mode is enabled.
        
        Returns:
            bool: True if staging mode is enabled, False otherwise.
        """
        return cls._is_staging 