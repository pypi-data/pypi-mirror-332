"""Core keystore operations for PyTrustStore."""

import os
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import jks
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.x509 import load_pem_x509_certificate

from pytruststore.cli_wrapper import KeytoolWrapper, OpenSSLWrapper
from pytruststore.logging_config import (
    get_logger,
    log_certificate_operation,
    log_keystore_operation,
    log_operation_start,
    log_operation_end,
)

# Initialize logger
logger = get_logger(__name__)


class KeystoreError(Exception):
    """Exception raised for errors in keystore operations."""

    pass


class KeystoreManager:
    """Manager for Java keystore operations."""

    def __init__(
        self,
        keystore_file: Optional[str] = None,
        password: Optional[str] = None,
        keytool_path: str = "keytool",
        openssl_path: str = "openssl",
    ):
        """Initialize KeystoreManager.

        Args:
            keystore_file: Path to the keystore file
            password: Keystore password
            keytool_path: Path to keytool executable
            openssl_path: Path to openssl executable
        """
        self.keystore_file = keystore_file
        self.password = password
        self.keytool = KeytoolWrapper(keytool_path)
        self.openssl = OpenSSLWrapper(openssl_path)
        self.logger = get_logger(__name__)
        self._keystore = None

    def load_keystore(self, keystore_file: Optional[str] = None, password: Optional[str] = None) -> jks.KeyStore:
        """Load a keystore from a file.

        Args:
            keystore_file: Path to the keystore file (overrides instance attribute)
            password: Keystore password (overrides instance attribute)

        Returns:
            Loaded keystore

        Raises:
            KeystoreError: If the keystore cannot be loaded
        """
        keystore_file = keystore_file or self.keystore_file
        password = password or self.password

        if not keystore_file:
            raise KeystoreError("Keystore file not specified")
        if not password:
            raise KeystoreError("Keystore password not specified")

        log_operation_start(
            self.logger, "load_keystore", keystore_file=keystore_file
        )

        try:
            # Check if file exists
            if not os.path.isfile(keystore_file):
                raise KeystoreError(f"Keystore file not found: {keystore_file}")

            # Load keystore
            keystore = jks.KeyStore.load(keystore_file, password)

            self._keystore = keystore
            self.keystore_file = keystore_file
            self.password = password

            log_operation_end(
                self.logger,
                "load_keystore",
                success=True,
                keystore_file=keystore_file,
                entries=len(keystore.entries),
            )

            return keystore
        except jks.KeystoreSignatureException:
            log_operation_end(
                self.logger,
                "load_keystore",
                success=False,
                keystore_file=keystore_file,
                error="Invalid keystore password",
            )
            raise KeystoreError("Invalid keystore password")
        except jks.BadKeystoreFormatException as e:
            log_operation_end(
                self.logger,
                "load_keystore",
                success=False,
                keystore_file=keystore_file,
                error=str(e),
            )
            raise KeystoreError(f"Bad keystore format: {str(e)}")
        except Exception as e:
            log_operation_end(
                self.logger,
                "load_keystore",
                success=False,
                keystore_file=keystore_file,
                error=str(e),
            )
            raise KeystoreError(f"Failed to load keystore: {str(e)}")

    def save_keystore(self, keystore_file: Optional[str] = None, password: Optional[str] = None) -> None:
        """Save a keystore to a file.

        Args:
            keystore_file: Path to the keystore file (overrides instance attribute)
            password: Keystore password (overrides instance attribute)

        Raises:
            KeystoreError: If the keystore cannot be saved
        """
        keystore_file = keystore_file or self.keystore_file
        password = password or self.password

        if not keystore_file:
            raise KeystoreError("Keystore file not specified")
        if not password:
            raise KeystoreError("Keystore password not specified")
        if not self._keystore:
            raise KeystoreError("No keystore loaded")

        log_operation_start(
            self.logger, "save_keystore", keystore_file=keystore_file
        )

        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(os.path.abspath(keystore_file)), exist_ok=True)

            # Save keystore
            self._keystore.save(keystore_file, password)

            log_operation_end(
                self.logger,
                "save_keystore",
                success=True,
                keystore_file=keystore_file,
            )
        except Exception as e:
            log_operation_end(
                self.logger,
                "save_keystore",
                success=False,
                keystore_file=keystore_file,
                error=str(e),
            )
            raise KeystoreError(f"Failed to save keystore: {str(e)}")

    def list_aliases(self) -> List[str]:
        """List all aliases in the keystore.

        Returns:
            List of aliases

        Raises:
            KeystoreError: If no keystore is loaded
        """
        if not self._keystore:
            raise KeystoreError("No keystore loaded")

        return list(self._keystore.entries.keys())

    def get_certificate(self, alias: str) -> x509.Certificate:
        """Get a certificate from the keystore.

        Args:
            alias: Certificate alias

        Returns:
            Certificate object

        Raises:
            KeystoreError: If the certificate cannot be retrieved
        """
        if not self._keystore:
            raise KeystoreError("No keystore loaded")

        log_certificate_operation(
            self.logger, "get_certificate", alias=alias
        )

        try:
            # Get certificate from keystore
            if alias not in self._keystore.entries:
                raise KeystoreError(f"Certificate not found: {alias}")

            entry = self._keystore.entries[alias]

            # Convert to cryptography certificate
            if hasattr(entry, "cert"):
                # TrustedCertEntry
                cert_bytes = entry.cert
            elif hasattr(entry, "cert_chain") and entry.cert_chain:
                # PrivateKeyEntry
                cert_bytes = entry.cert_chain[0][1]
            else:
                raise KeystoreError(f"Entry does not contain a certificate: {alias}")

            return x509.load_der_x509_certificate(cert_bytes, default_backend())
        except Exception as e:
            raise KeystoreError(f"Failed to get certificate: {str(e)}")

    def get_certificate_pem(self, alias: str) -> str:
        """Get a certificate from the keystore in PEM format.

        Args:
            alias: Certificate alias

        Returns:
            Certificate in PEM format

        Raises:
            KeystoreError: If the certificate cannot be retrieved
        """
        cert = self.get_certificate(alias)
        return cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")

    def get_certificate_chain(self, alias: str) -> List[x509.Certificate]:
        """Get a certificate chain from the keystore.

        Args:
            alias: Certificate alias

        Returns:
            List of certificates in the chain

        Raises:
            KeystoreError: If the certificate chain cannot be retrieved
        """
        if not self._keystore:
            raise KeystoreError("No keystore loaded")

        log_certificate_operation(
            self.logger, "get_certificate_chain", alias=alias
        )

        try:
            # Get certificate from keystore
            if alias not in self._keystore.entries:
                raise KeystoreError(f"Certificate not found: {alias}")

            entry = self._keystore.entries[alias]

            # Get certificate chain
            if hasattr(entry, "cert_chain") and entry.cert_chain:
                # PrivateKeyEntry
                return [
                    x509.load_der_x509_certificate(cert[1], default_backend())
                    for cert in entry.cert_chain
                ]
            elif hasattr(entry, "cert"):
                # TrustedCertEntry
                return [x509.load_der_x509_certificate(entry.cert, default_backend())]
            else:
                raise KeystoreError(f"Entry does not contain a certificate: {alias}")
        except Exception as e:
            raise KeystoreError(f"Failed to get certificate chain: {str(e)}")

    def get_certificate_info(self, alias: str) -> Dict[str, str]:
        """Get detailed information about a certificate.

        Args:
            alias: Certificate alias

        Returns:
            Dictionary with certificate information

        Raises:
            KeystoreError: If the certificate information cannot be retrieved
        """
        cert = self.get_certificate(alias)
        cert_pem = cert.public_bytes(serialization.Encoding.PEM).decode("utf-8")

        # Use OpenSSL for detailed information
        return self.openssl.get_certificate_info(cert_pem)

    def add_certificate(self, alias: str, cert_pem: str) -> None:
        """Add a certificate to the keystore.

        Args:
            alias: Certificate alias
            cert_pem: Certificate in PEM format

        Raises:
            KeystoreError: If the certificate cannot be added
        """
        if not self._keystore:
            raise KeystoreError("No keystore loaded")

        log_certificate_operation(
            self.logger, "add_certificate", alias=alias
        )

        try:
            # Convert PEM to DER
            cert = load_pem_x509_certificate(cert_pem.encode("utf-8"), default_backend())
            cert_der = cert.public_bytes(serialization.Encoding.DER)

            # Add certificate to keystore
            self._keystore.entries[alias] = jks.TrustedCertEntry.new(alias, cert_der)

            # Save keystore
            self.save_keystore()
        except Exception as e:
            raise KeystoreError(f"Failed to add certificate: {str(e)}")

    def add_certificate_chain(self, alias: str, cert_chain_pem: List[str]) -> None:
        """Add a certificate chain to the keystore.

        Args:
            alias: Certificate alias
            cert_chain_pem: List of certificates in PEM format

        Raises:
            KeystoreError: If the certificate chain cannot be added
        """
        if not self._keystore:
            raise KeystoreError("No keystore loaded")
        if not cert_chain_pem:
            raise KeystoreError("Certificate chain is empty")

        log_certificate_operation(
            self.logger, "add_certificate_chain", alias=alias
        )

        try:
            # Use keytool for this operation since it's more reliable for chains
            with tempfile.NamedTemporaryFile(suffix=".pem", mode="w") as temp_file:
                # Write certificate chain to temporary file
                for cert_pem in cert_chain_pem:
                    temp_file.write(cert_pem)
                    temp_file.write("\n")
                temp_file.flush()

                # Import certificate chain
                self.keytool.import_certificate(
                    self.keystore_file, self.password, alias, temp_file.name
                )

            # Reload keystore to reflect changes
            self.load_keystore()
        except Exception as e:
            raise KeystoreError(f"Failed to add certificate chain: {str(e)}")

    def delete_certificate(self, alias: str) -> None:
        """Delete a certificate from the keystore.

        Args:
            alias: Certificate alias

        Raises:
            KeystoreError: If the certificate cannot be deleted
        """
        if not self._keystore:
            raise KeystoreError("No keystore loaded")

        log_certificate_operation(
            self.logger, "delete_certificate", alias=alias
        )

        try:
            # Check if certificate exists
            if alias not in self._keystore.entries:
                raise KeystoreError(f"Certificate not found: {alias}")

            # Delete certificate
            del self._keystore.entries[alias]

            # Save keystore
            self.save_keystore()
        except KeystoreError:
            raise
        except Exception as e:
            raise KeystoreError(f"Failed to delete certificate: {str(e)}")

    def rename_alias(self, old_alias: str, new_alias: str) -> None:
        """Rename a certificate alias.

        Args:
            old_alias: Old certificate alias
            new_alias: New certificate alias

        Raises:
            KeystoreError: If the alias cannot be renamed
        """
        if not self._keystore:
            raise KeystoreError("No keystore loaded")

        log_certificate_operation(
            self.logger,
            "rename_alias",
            alias=old_alias,
            new_alias=new_alias,
        )

        try:
            # Check if old alias exists
            if old_alias not in self._keystore.entries:
                raise KeystoreError(f"Certificate not found: {old_alias}")

            # Check if new alias already exists
            if new_alias in self._keystore.entries:
                raise KeystoreError(f"Certificate already exists: {new_alias}")

            # Rename alias
            self._keystore.entries[new_alias] = self._keystore.entries[old_alias]
            self._keystore.entries[new_alias].alias = new_alias
            del self._keystore.entries[old_alias]

            # Save keystore
            self.save_keystore()
        except KeystoreError:
            raise
        except Exception as e:
            raise KeystoreError(f"Failed to rename alias: {str(e)}")

    def search_certificates(
        self, subject: Optional[str] = None, issuer: Optional[str] = None, serial: Optional[str] = None
    ) -> List[str]:
        """Search for certificates in the keystore.

        Args:
            subject: Subject to search for
            issuer: Issuer to search for
            serial: Serial number to search for

        Returns:
            List of matching aliases

        Raises:
            KeystoreError: If no keystore is loaded
        """
        if not self._keystore:
            raise KeystoreError("No keystore loaded")

        log_operation_start(
            self.logger,
            "search_certificates",
            subject=subject,
            issuer=issuer,
            serial=serial,
        )

        matches = []

        for alias in self.list_aliases():
            try:
                cert = self.get_certificate(alias)
                match = True

                if subject and subject.lower() not in str(cert.subject).lower():
                    match = False
                if issuer and issuer.lower() not in str(cert.issuer).lower():
                    match = False
                if serial and serial.lower() != hex(cert.serial_number)[2:].lower():
                    match = False

                if match:
                    matches.append(alias)
            except Exception as e:
                self.logger.warning(
                    f"Error processing certificate during search",
                    alias=alias,
                    error=str(e),
                )

        log_operation_end(
            self.logger,
            "search_certificates",
            success=True,
            matches=len(matches),
        )

        return matches

    def create_empty_keystore(self, keystore_file: str, password: str) -> None:
        """Create an empty keystore.

        Args:
            keystore_file: Path to the keystore file
            password: Keystore password

        Raises:
            KeystoreError: If the keystore cannot be created
        """
        log_operation_start(
            self.logger, "create_empty_keystore", keystore_file=keystore_file
        )

        try:
            # Create empty keystore
            keystore = jks.KeyStore.new("jks", [])
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(os.path.abspath(keystore_file)), exist_ok=True)

            # Save keystore
            keystore.save(keystore_file, password)

            # Load the new keystore
            self.keystore_file = keystore_file
            self.password = password
            self._keystore = keystore

            log_operation_end(
                self.logger,
                "create_empty_keystore",
                success=True,
                keystore_file=keystore_file,
            )
        except Exception as e:
            log_operation_end(
                self.logger,
                "create_empty_keystore",
                success=False,
                keystore_file=keystore_file,
                error=str(e),
            )
            raise KeystoreError(f"Failed to create empty keystore: {str(e)}")
