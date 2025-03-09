import subprocess
import sys
import importlib
import logging
import requests
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


def update_and_reload(package_name):
    # Update the package using pip
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--upgrade", package_name]
    )
    importlib.invalidate_caches()  # Invalidate cache before reloading
    package = importlib.import_module(package_name)
    importlib.reload(package)
    print(f"Package '{package_name}' has been updated and reloaded.")

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
     
                logger.info(
                    f"Updating datafoundry SDK from version {installed_version} to version {latest_version}..."
                )
                update_and_reload("datafoundry")
        except Exception as e:
             logger.error(f"An unexpected error occurred version check: {e}")
        
        return func(*args, **kwargs)
    return wrapper