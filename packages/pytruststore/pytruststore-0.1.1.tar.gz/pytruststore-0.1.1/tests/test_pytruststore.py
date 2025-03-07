"""Tests for the PyTrustStore package."""

import os
import tempfile
from pathlib import Path

import pytest
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.x509 import load_pem_x509_certificate

from pytruststore.keystore import KeystoreManager
from pytruststore.utils import parse_url


def test_keystore_creation():
    """Test creating a new keystore."""
    with tempfile.NamedTemporaryFile(suffix=".jks") as temp_file:
        # Create keystore manager
        keystore_manager = KeystoreManager()
        
        # Create empty keystore
        keystore_manager.create_empty_keystore(temp_file.name, "password")
        
        # Check if keystore was created
        assert os.path.exists(temp_file.name)
        
        # Check if keystore can be loaded
        keystore_manager.load_keystore(temp_file.name, "password")
        
        # Check if keystore is empty
        assert len(keystore_manager.list_aliases()) == 0


def test_parse_url():
    """Test URL parsing."""
    # Test with HTTPS URL
    hostname, port = parse_url("https://example.com")
    assert hostname == "example.com"
    assert port == 443
    
    # Test with HTTP URL and port
    hostname, port = parse_url("http://example.com:8080")
    assert hostname == "example.com"
    assert port == 8080
    
    # Test with just hostname (should default to HTTPS and port 443)
    hostname, port = parse_url("example.com")
    assert hostname == "example.com"
    assert port == 443
    
    # Test with invalid URL
    with pytest.raises(ValueError):
        parse_url("not a url")


def test_keystore_operations():
    """Test keystore operations."""
    with tempfile.NamedTemporaryFile(suffix=".jks") as temp_file:
        # Create keystore manager
        keystore_manager = KeystoreManager()
        
        # Create empty keystore
        keystore_manager.create_empty_keystore(temp_file.name, "password")
        
        # Create a self-signed certificate (mock)
        cert_pem = """-----BEGIN CERTIFICATE-----
MIIDazCCAlOgAwIBAgIUJFdUbtc5gXmR7Y27PQjCMGMIa+swDQYJKoZIhvcNAQEL
BQAwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM
GEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDAeFw0yMzA0MDEwMDAwMDBaFw0yNDA0
MDEwMDAwMDBaMEUxCzAJBgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEw
HwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQDK/FdIp8kJ/OIE/L2lTu1qVxvMJmIFG9PUzZ8CQXTx
6jQBXpSI0OaFHnMHQVuai65Mo3Fz7J2QUmv8YBKbW9KiXPy9yCnlGGqJJzK5MZia
CjhRJzWC1mcNkKKEFJ7Gu3ZK+GcYKqSMvHH1lITJaHsrF+5QHsOIy9hHvYtlbOZ4
UyZGJaC0BN6JTpggOM5IXO6IPJYr7w8jTVFo5UzSPKW9/vYwJA5bIJhpXNlPQ9NF
/Jt3/0Y8Kj3OV0UwLsN8WWe3WBGzAUWxnSxVh44tI1DQfcYFAQDPE0FuFRnJr6vS
JQKoR2TjRrE/8VJxv9IFdwQcWE5+kYuJ4Xn0QQEJAgMBAAGjUzBRMB0GA1UdDgQW
BBQjA/FwQAtdPyaVGQgEJFgLHYM6uDAfBgNVHSMEGDAWgBQjA/FwQAtdPyaVGQgE
JFgLHYM6uDAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBM4wPu
7P5GzLNGkZrPOTq+2jV+h7TYVtKlOB3Kh8jcHIRXyLzP3S5uVwXZwRUHQHrWOGXx
u1awuNlFK5JzUzGJLyzU8UA4GQwfVKqfJnfJyJtZIJFk6NSqYZ7HBu3HFbKtKLjC
GXBL5TlGkCPnFuQUBzpaVsKyc1LbTVKdOSQAKOKLJA8K9xmLm2MKLj2ygH0KxnPJ
8UJKJY1GJKfILz4Tu1xgQYO/H31/Qxj1vECTNDFLmEwAyLbY0Jh/1tUjXnVdqIcP
iL3QUwJUQJTgJlnlXwn2aCGnXs5HQWj9U4RZ0YJiXCLGJ+wYZbj6zMJwZpXcFiPg
HJnLuY0NQhvMxVUR
-----END CERTIFICATE-----"""
        
        # Add certificate to keystore
        keystore_manager.add_certificate("test_cert", cert_pem)
        
        # Check if certificate was added
        assert "test_cert" in keystore_manager.list_aliases()
        
        # Get certificate from keystore
        cert = keystore_manager.get_certificate("test_cert")
        
        # Check certificate properties
        assert isinstance(cert, x509.Certificate)
        assert cert.subject.get_attributes_for_oid(x509.NameOID.COUNTRY_NAME)[0].value == "AU"
        
        # Rename certificate
        keystore_manager.rename_alias("test_cert", "renamed_cert")
        
        # Check if certificate was renamed
        assert "renamed_cert" in keystore_manager.list_aliases()
        assert "test_cert" not in keystore_manager.list_aliases()
        
        # Delete certificate
        keystore_manager.delete_certificate("renamed_cert")
        
        # Check if certificate was deleted
        assert "renamed_cert" not in keystore_manager.list_aliases()
