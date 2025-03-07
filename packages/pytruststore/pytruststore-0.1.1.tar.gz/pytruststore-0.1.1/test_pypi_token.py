#!/usr/bin/env python3
"""
Test script to verify if a PyPI API token is valid.
This script attempts to authenticate with PyPI using the provided token
without actually uploading any packages.
"""

import os
import sys
from urllib.parse import urlparse

try:
    from twine.auth import BasicAuth
    from twine.settings import Settings
    from twine.exceptions import TwineException
    from twine.repository import Repository
except ImportError:
    print("Error: twine package is required. Install it with 'pip install twine'")
    sys.exit(1)

def test_pypi_token(token, repository_url="https://upload.pypi.org/legacy/"):
    """Test if a PyPI token is valid by attempting to authenticate."""
    print(f"Testing PyPI token against {repository_url}")
    
    # Create settings with the token
    settings = Settings(
        username="__token__",
        password=token,
        repository_url=repository_url
    )
    
    try:
        # Parse the repository URL
        parsed = urlparse(repository_url)
        repository = Repository(
            settings,
            parsed.netloc,
            parsed.path,
        )
        
        # Test authentication
        # This doesn't upload anything, just checks if we can authenticate
        repository.verify_package_exists("twine")
        
        print("✅ Success! The token is valid and authentication was successful.")
        return True
    except TwineException as e:
        print(f"❌ Error: Authentication failed. The token may be invalid.")
        print(f"Error details: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error: An unexpected error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    # Get token from environment variable or command line
    token = None
    
    if len(sys.argv) > 1:
        token = sys.argv[1]
    elif "PYPI_API_TOKEN" in os.environ:
        token = os.environ["PYPI_API_TOKEN"]
    
    if not token:
        print("Please provide your PyPI API token either:")
        print("1. As a command line argument: python test_pypi_token.py YOUR_TOKEN")
        print("2. As an environment variable: export PYPI_API_TOKEN=YOUR_TOKEN")
        sys.exit(1)
    
    # Test against PyPI
    success = test_pypi_token(token)
    
    # Optionally test against TestPyPI as well
    test_pypi = input("\nWould you like to test against TestPyPI as well? (y/n): ")
    if test_pypi.lower() == 'y':
        test_pypi_token(token, "https://test.pypi.org/legacy/")
    
    if not success:
        sys.exit(1)
