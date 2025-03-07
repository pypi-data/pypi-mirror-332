#!/usr/bin/env python3
"""
Test script to verify PyPI API token authentication using the same method as twine.
"""

import sys
import base64
import requests

def test_pypi_token(token, repository_url="https://upload.pypi.org/legacy/"):
    """Test if a PyPI token is valid by attempting to authenticate the same way twine does."""
    print(f"Testing PyPI token against {repository_url}")
    
    # Create the authentication header exactly as twine would
    # Twine uses HTTP Basic Auth with "__token__" as username and the token as password
    auth = base64.b64encode(f"__token__:{token}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "pytruststore-token-test/1.0"
    }
    
    try:
        # Make a HEAD request to the repository URL
        # This checks authentication without uploading anything
        response = requests.head(
            repository_url,
            headers=headers,
            timeout=10
        )
        
        # Check response status
        if response.status_code == 200:
            print("✅ Success! Authentication to PyPI was successful.")
            print("Your token is valid and properly formatted.")
            return True
        elif response.status_code == 401 or response.status_code == 403:
            print("❌ Authentication failed. The token is invalid or expired.")
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.reason}")
            return False
        else:
            print(f"⚠️ Unexpected response (status code: {response.status_code})")
            print(f"Response: {response.reason}")
            print("\nThis might not indicate an authentication problem.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_pypi_auth.py YOUR_PYPI_TOKEN")
        sys.exit(1)
    
    token = sys.argv[1]
    
    # Check token format
    if not token.startswith("pypi-"):
        print("⚠️ Warning: PyPI tokens typically start with 'pypi-'. Your token may be invalid.")
    
    # Test against PyPI
    success = test_pypi_token(token)
    
    # Optionally test against TestPyPI
    test_pypi = input("\nWould you like to test against TestPyPI as well? (y/n): ")
    if test_pypi.lower() == 'y':
        test_pypi_token(token, "https://test.pypi.org/legacy/")
    
    if not success:
        print("\nTroubleshooting tips:")
        print("1. Verify the token hasn't expired")
        print("2. Check if the token has the correct scope (it should allow uploads)")
        print("3. Create a new token at https://pypi.org/manage/account/")
        print("4. Make sure the token is correctly set in GitLab CI/CD variables")
        print("   - Variable name should be PYPI_API_TOKEN")
        print("   - Mark it as Protected and Masked")
        sys.exit(1)
