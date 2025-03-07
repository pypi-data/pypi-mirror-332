#!/usr/bin/env python3
"""
A simple script to test PyPI API token validity using the requests library.
"""

import sys
import requests

def test_pypi_token(token):
    """Test if a PyPI token is valid by making a simple API request."""
    print("Testing PyPI token...")
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Make a simple request to the PyPI API
    response = requests.get(
        "https://pypi.org/pypi/twine/json",
        headers=headers
    )
    
    # Check if we got a 200 OK response
    if response.status_code == 200:
        print("✅ Connection to PyPI successful!")
        
        # Try a more specific API endpoint that requires authentication
        user_response = requests.get(
            "https://pypi.org/api/v1/user/",
            headers=headers
        )
        
        if user_response.status_code == 200:
            print("✅ Authentication successful! Your token is valid.")
            return True
        else:
            print(f"❌ Authentication failed with status code: {user_response.status_code}")
            print(f"Response: {user_response.text}")
            return False
    else:
        print(f"❌ Connection failed with status code: {response.status_code}")
        print(f"Response: {response.text}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simple_token_test.py YOUR_PYPI_TOKEN")
        sys.exit(1)
    
    token = sys.argv[1]
    if not token.startswith("pypi-"):
        print("Warning: PyPI tokens typically start with 'pypi-'. Your token may be invalid.")
    
    test_pypi_token(token)
