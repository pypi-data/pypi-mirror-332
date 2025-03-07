"""Tests for the keystore module."""

import os
import tempfile
from pathlib import Path
from unittest import TestCase, mock

import jks
import pytest
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from pytruststore.keystore import KeystoreError, KeystoreManager


class TestKeystoreManager(TestCase):
    """Test the KeystoreManager class."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary keystore file
        self.keystore_fd, self.keystore_file = tempfile.mkstemp(suffix=".jks")
        self.password = "password"
        
        # Create a keystore manager
        self.keystore_manager = KeystoreManager(self.keystore_file, self.password)
        
        # Create an empty keystore
        self.keystore_manager.create_empty_keystore(self.keystore_file, self.password)

    def tearDown(self):
        """Tear down test fixtures."""
        # Close and remove the temporary keystore file
        os.close(self.keystore_fd)
        os.unlink(self.keystore_file)

    def test_create_empty_keystore(self):
        """Test creating an empty keystore."""
        # Create a new temporary file
        fd, keystore_file = tempfile.mkstemp(suffix=".jks")
        os.close(fd)
        
        try:
            # Create an empty keystore
            keystore_manager = KeystoreManager()
            keystore_manager.create_empty_keystore(keystore_file, self.password)
            
            # Check that the keystore was created
            assert os.path.exists(keystore_file)
            
            # Load the keystore
            keystore_manager.load_keystore(keystore_file, self.password)
            
            # Check that the keystore is empty
            assert len(keystore_manager.list_aliases()) == 0
        finally:
            # Remove the temporary file
            os.unlink(keystore_file)

    def test_load_keystore(self):
        """Test loading a keystore."""
        # Load the keystore
        self.keystore_manager.load_keystore()
        
        # Check that the keystore was loaded
        assert self.keystore_manager._keystore is not None

    def test_load_keystore_invalid_password(self):
        """Test loading a keystore with an invalid password."""
        # Try to load the keystore with an invalid password
        with pytest.raises(KeystoreError, match="Invalid keystore password"):
            self.keystore_manager.load_keystore(password="invalid")

    def test_load_keystore_nonexistent_file(self):
        """Test loading a nonexistent keystore file."""
        # Try to load a nonexistent keystore file
        with pytest.raises(KeystoreError, match="Keystore file not found"):
            self.keystore_manager.load_keystore("nonexistent.jks", self.password)

    def test_list_aliases(self):
        """Test listing aliases."""
        # Load the keystore
        self.keystore_manager.load_keystore()
        
        # Check that the keystore is empty
        assert len(self.keystore_manager.list_aliases()) == 0

    @mock.patch("pytruststore.keystore.jks.TrustedCertEntry.new")
    @mock.patch("pytruststore.keystore.load_pem_x509_certificate")
    @mock.patch("pytruststore.keystore.KeystoreManager.save_keystore")
    def test_add_certificate(self, mock_save, mock_load_pem, mock_new):
        """Test adding a certificate."""
        # Mock the TrustedCertEntry.new method
        mock_entry = mock.MagicMock()
        mock_new.return_value = mock_entry
        
        # Mock the load_pem_x509_certificate function
        mock_cert = mock.MagicMock()
        mock_cert.public_bytes.return_value = b"dummy_der"
        mock_load_pem.return_value = mock_cert
        
        # Load the keystore
        self.keystore_manager.load_keystore()
        
        # Add a certificate
        self.keystore_manager.add_certificate(
            "test",
            """-----BEGIN CERTIFICATE-----
            MIIDazCCAlOgAwIBAgIUEMGnwEnxf9rL0cDFHxbHimkzA9AwDQYJKoZIhvcNAQEL
            BQAwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM
            GEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDAeFw0yMzA1MDExMjAwMDBaFw0yNDA1
            MDExMjAwMDBaMEUxCzAJBgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEw
            HwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQwggEiMA0GCSqGSIb3DQEB
            AQUAA4IBDwAwggEKAoIBAQDCpLX2WXs2mUJiCxQhDUzqQVYP1jM4dMkEmvLNiwWs
            BnUQdCw+QSSJJAlaF8F+LmvjYnK5+3Jd5VQZS/RQIqVvuAMNh8XuFO9+9R3JLXCg
            SmFvkr5HGWrP9jVQttSuWlLUdpyRvSJrE2M/FsJQRFYkJ9w0ztUZQgEJKJXcJbft
            +kQUOvUOLtY0a0w+xT9GZmk5RYSl1UiKLKdPcIzZ6LWAQmQxYIA9qXEL1UWEMaL3
            f5qgvGDF9WwXYFrZQQdUw3TC/sjuYNTCBT/J+cIRFvJHAzKIR9RRIUSH/MxQoYKz
            KJCJy4LR6eYeAPvvJAK2BsIK7YRd+H5qKygYbE0/AgMBAAGjUzBRMB0GA1UdDgQW
            BBQtMwQbJ3+uMh7E91X4RqT6nkGQQjAfBgNVHSMEGDAWgBQtMwQbJ3+uMh7E91X4
            RqT6nkGQQjAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQCrjXxd
            3ao/jV2PpLzJvQ8jGTZv/ZNrEAGQdXGUraHsaP5bZvkR9ZU6K8enUUv8bPm5CwcL
            UBaw8cP0XmOxiBdFsWVVd5rvAVuIJqfJH/Z7aGdEGjGcVUHEpw2E7UeL/LTEyD9C
            vXXLJYfEYlFGNdNrUPFzNqzKEwA5JuRKE+PnRpH5X9OZdTOPfQ9jqOTjkN7T9C5z
            QQe6Ydqt3J6VdU0RZkVjW5Yz57WnpUuZQYoQyE/08IJLUCyWrKuSBhgE7uhWGgMm
            U37e7YVgJjJvbZCv6bLCUZCfKUQlWmQKmL5DcE+1iUVRFJWnqAQgCBCYRlA4MtDR
            UdFkQMZ0YHa5jkZW
            -----END CERTIFICATE-----"""
        )
        
        # Check that the certificate was added
        assert mock_load_pem.called
        assert mock_new.called
        assert mock_save.called
        assert "test" in self.keystore_manager._keystore.entries

    def test_rename_alias(self):
        """Test renaming an alias."""
        # Load the keystore
        self.keystore_manager.load_keystore()
        
        # Add a certificate
        with mock.patch("pytruststore.keystore.jks.TrustedCertEntry.new") as mock_new, \
             mock.patch("pytruststore.keystore.load_pem_x509_certificate") as mock_load_pem, \
             mock.patch("pytruststore.keystore.KeystoreManager.save_keystore"):
            mock_entry = mock.MagicMock()
            mock_new.return_value = mock_entry
            
            mock_cert = mock.MagicMock()
            mock_cert.public_bytes.return_value = b"dummy_der"
            mock_load_pem.return_value = mock_cert
            
            self.keystore_manager.add_certificate("test", "dummy")
        
        # Rename the alias
        with mock.patch("pytruststore.keystore.KeystoreManager.save_keystore"):
            self.keystore_manager.rename_alias("test", "new_test")
        
        # Check that the alias was renamed
        assert "new_test" in self.keystore_manager._keystore.entries
        assert "test" not in self.keystore_manager._keystore.entries

    def test_rename_alias_nonexistent(self):
        """Test renaming a nonexistent alias."""
        # Load the keystore
        self.keystore_manager.load_keystore()
        
        # Try to rename a nonexistent alias
        with pytest.raises(KeystoreError, match="Certificate not found"):
            self.keystore_manager.rename_alias("nonexistent", "new_test")

    def test_rename_alias_exists(self):
        """Test renaming an alias to an existing alias."""
        # Load the keystore
        self.keystore_manager.load_keystore()
        
        # Add certificates
        with mock.patch("pytruststore.keystore.jks.TrustedCertEntry.new") as mock_new, \
             mock.patch("pytruststore.keystore.load_pem_x509_certificate") as mock_load_pem, \
             mock.patch("pytruststore.keystore.KeystoreManager.save_keystore"):
            mock_entry = mock.MagicMock()
            mock_new.return_value = mock_entry
            
            mock_cert = mock.MagicMock()
            mock_cert.public_bytes.return_value = b"dummy_der"
            mock_load_pem.return_value = mock_cert
            
            self.keystore_manager.add_certificate("test1", "dummy1")
            self.keystore_manager.add_certificate("test2", "dummy2")
        
        # Try to rename to an existing alias
        with pytest.raises(KeystoreError, match="Certificate already exists"):
            self.keystore_manager.rename_alias("test1", "test2")
