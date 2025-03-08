import logging
import requests
import subprocess
import functools
from typing import Optional, Dict, Any, Callable
import pkg_resources
import os

# --- Version Checking & Notification ---
logger = logging.getLogger(__name__)

def get_latest_version(package_name: str = "datafoundry") -> Optional[str]:
    """Retrieves the latest version of the package from PyPI."""
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data["info"]["version"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching latest version from PyPI: {e}")
        return None  # Return None if there's an error
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")  # general
        return None


def get_installed_version(package_name: str = "datafoundry") -> str:
    """Gets the currently installed version of the package."""
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return "0.0.0"


def check_for_updates(func, package_name: str = "datafoundry"):
    """Decorator to check for SDK updates and log changes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            latest_version = get_latest_version(package_name)
            installed_version = get_installed_version(package_name)
            
            if latest_version is None:  # Handle cases where version fetch fails
                logger.warning("Could not determine the latest version. Skipping version check.")
                return func(*args, **kwargs)

            if latest_version and installed_version != latest_version:
                logger.warning(
                    f"A new version of the datafoundry SDK is available! "
                    f"You have version {installed_version}, but version {latest_version} is available."
                )
        except Exception as e:
             logger.error(f"An unexpected error occurred version check: {e}")
        
        return func(*args, **kwargs)
    return wrapper