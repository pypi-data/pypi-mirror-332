"""TLS validation functionality for PyTrustStore."""

import re
import socket
import ssl
import tempfile
import urllib.parse
from typing import Dict, List, Optional, Tuple, Union

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.x509 import load_pem_x509_certificate

from pytruststore.cli_wrapper import OpenSSLWrapper
from pytruststore.keystore import KeystoreManager
from pytruststore.logging_config import (
    get_logger,
    log_operation_start,
    log_operation_end,
)

# Initialize logger
logger = get_logger(__name__)


class ValidationError(Exception):
    """Exception raised for errors in validation operations."""

    pass


class TLSValidator:
    """Validator for TLS connections and certificates."""

    def __init__(
        self,
        keystore_manager: Optional[KeystoreManager] = None,
        openssl_path: str = "openssl",
    ):
        """Initialize TLSValidator.

        Args:
            keystore_manager: KeystoreManager instance
            openssl_path: Path to openssl executable
        """
        self.keystore_manager = keystore_manager
        self.openssl = OpenSSLWrapper(openssl_path)
        self.logger = get_logger(__name__)

    def fetch_server_certificates(self, url: str) -> List[str]:
        """Fetch certificates from a server.

        Args:
            url: URL to connect to

        Returns:
            List of certificates in PEM format

        Raises:
            ValidationError: If the certificates cannot be fetched
        """
        log_operation_start(
            self.logger, "fetch_server_certificates", url=url
        )

        try:
            # Parse URL and add scheme if missing
            if not url.startswith(('http://', 'https://')):
                url = f"https://{url}"
                self.logger.debug(f"Added https:// scheme to URL: {url}")
                
            parsed_url = urllib.parse.urlparse(url)
            hostname = parsed_url.hostname
            port = parsed_url.port or 443

            if not hostname:
                raise ValidationError(f"Invalid URL: {url}")

            # Use OpenSSL to get certificate chain
            cert_chain = self.openssl.get_certificate_chain(hostname, port)

            log_operation_end(
                self.logger,
                "fetch_server_certificates",
                success=True,
                url=url,
                certificates=len(cert_chain),
            )

            return cert_chain
        except Exception as e:
            log_operation_end(
                self.logger,
                "fetch_server_certificates",
                success=False,
                url=url,
                error=str(e),
            )
            raise ValidationError(f"Failed to fetch server certificates: {str(e)}")

    def validate_against_keystore(
        self, url: str, keystore_manager: Optional[KeystoreManager] = None
    ) -> Tuple[bool, Dict[str, str]]:
        """Validate a server's certificates against a keystore.

        Args:
            url: URL to connect to
            keystore_manager: KeystoreManager instance (overrides instance attribute)

        Returns:
            Tuple of (validation result, validation details)

        Raises:
            ValidationError: If the validation cannot be performed
        """
        keystore_manager = keystore_manager or self.keystore_manager
        if not keystore_manager:
            raise ValidationError("No keystore manager specified")
        if not keystore_manager._keystore:
            raise ValidationError("No keystore loaded")

        log_operation_start(
            self.logger,
            "validate_against_keystore",
            url=url,
            keystore=keystore_manager.keystore_file,
        )

        try:
            # Add scheme if missing (fetch_server_certificates will handle this too, but we need the updated URL)
            if not url.startswith(('http://', 'https://')):
                url = f"https://{url}"
                self.logger.debug(f"Added https:// scheme to URL: {url}")
                
            # Fetch server certificates
            server_certs = self.fetch_server_certificates(url)
            if not server_certs:
                raise ValidationError(f"No certificates found for {url}")

            # Parse server certificates
            server_cert_objs = [
                load_pem_x509_certificate(cert.encode("utf-8"), default_backend())
                for cert in server_certs
            ]

            # Get all certificates from keystore
            keystore_certs = {}
            for alias in keystore_manager.list_aliases():
                try:
                    cert = keystore_manager.get_certificate(alias)
                    # Use subject and issuer as key to avoid duplicate certificates
                    key = (str(cert.subject), str(cert.issuer))
                    keystore_certs[key] = (alias, cert)
                except Exception as e:
                    self.logger.warning(
                        f"Error processing certificate during validation",
                        alias=alias,
                        error=str(e),
                    )

            # Check if server certificates are in keystore
            validation_details = {}
            all_found = True

            for i, cert in enumerate(server_cert_objs):
                cert_found = False
                key = (str(cert.subject), str(cert.issuer))

                if key in keystore_certs:
                    alias, _ = keystore_certs[key]
                    cert_found = True
                    validation_details[f"cert_{i}"] = {
                        "subject": str(cert.subject),
                        "issuer": str(cert.issuer),
                        "found": True,
                        "alias": alias,
                    }
                else:
                    # Check by comparing public key
                    for alias, keystore_cert in keystore_certs.values():
                        if cert.public_key().public_bytes(
                            serialization.Encoding.DER,
                            serialization.PublicFormat.SubjectPublicKeyInfo,
                        ) == keystore_cert.public_key().public_bytes(
                            serialization.Encoding.DER,
                            serialization.PublicFormat.SubjectPublicKeyInfo,
                        ):
                            cert_found = True
                            validation_details[f"cert_{i}"] = {
                                "subject": str(cert.subject),
                                "issuer": str(cert.issuer),
                                "found": True,
                                "alias": alias,
                                "note": "Matched by public key",
                            }
                            break

                if not cert_found:
                    all_found = False
                    validation_details[f"cert_{i}"] = {
                        "subject": str(cert.subject),
                        "issuer": str(cert.issuer),
                        "found": False,
                    }

            validation_details["all_found"] = all_found
            validation_details["url"] = url
            validation_details["keystore"] = keystore_manager.keystore_file

            log_operation_end(
                self.logger,
                "validate_against_keystore",
                success=True,
                url=url,
                keystore=keystore_manager.keystore_file,
                result=all_found,
            )

            return all_found, validation_details
        except Exception as e:
            log_operation_end(
                self.logger,
                "validate_against_keystore",
                success=False,
                url=url,
                keystore=keystore_manager.keystore_file if keystore_manager else None,
                error=str(e),
            )
            raise ValidationError(f"Failed to validate against keystore: {str(e)}")

    def import_server_certificates(
        self,
        url: str,
        keystore_manager: Optional[KeystoreManager] = None,
        alias_prefix: str = "",
        overwrite: bool = False,
    ) -> Dict[str, str]:
        """Import certificates from a server into a keystore.

        Args:
            url: URL to connect to
            keystore_manager: KeystoreManager instance (overrides instance attribute)
            alias_prefix: Prefix for certificate aliases
            overwrite: Whether to overwrite existing certificates

        Returns:
            Dictionary mapping certificate subjects to aliases

        Raises:
            ValidationError: If the certificates cannot be imported
        """
        keystore_manager = keystore_manager or self.keystore_manager
        if not keystore_manager:
            raise ValidationError("No keystore manager specified")
        if not keystore_manager._keystore:
            raise ValidationError("No keystore loaded")

        log_operation_start(
            self.logger,
            "import_server_certificates",
            url=url,
            keystore=keystore_manager.keystore_file,
            alias_prefix=alias_prefix,
            overwrite=overwrite,
        )

        try:
            # Add scheme if missing (fetch_server_certificates will handle this too, but we need the updated URL)
            if not url.startswith(('http://', 'https://')):
                url = f"https://{url}"
                self.logger.debug(f"Added https:// scheme to URL: {url}")
                
            # Fetch server certificates
            server_certs = self.fetch_server_certificates(url)
            if not server_certs:
                raise ValidationError(f"No certificates found for {url}")

            # Parse URL for alias prefix
            parsed_url = urllib.parse.urlparse(url)
            hostname = parsed_url.hostname or "unknown"
            if not alias_prefix:
                alias_prefix = hostname.replace(".", "_")

            # Import certificates
            imported = {}
            existing_aliases = keystore_manager.list_aliases()

            for i, cert_pem in enumerate(server_certs):
                # Parse certificate
                cert = load_pem_x509_certificate(cert_pem.encode("utf-8"), default_backend())
                
                # Generate alias
                if i == 0:
                    # Server certificate
                    alias = f"{alias_prefix}_server"
                else:
                    # CA certificates
                    cn_match = re.search(r"CN=([^,]+)", str(cert.subject))
                    if cn_match:
                        cn = cn_match.group(1).replace(" ", "_")
                        alias = f"{alias_prefix}_ca_{cn}"
                    else:
                        alias = f"{alias_prefix}_ca_{i}"

                # Check if alias exists
                if alias in existing_aliases:
                    if overwrite:
                        keystore_manager.delete_certificate(alias)
                    else:
                        # Generate unique alias
                        base_alias = alias
                        counter = 1
                        while alias in existing_aliases:
                            alias = f"{base_alias}_{counter}"
                            counter += 1

                # Add certificate to keystore
                keystore_manager.add_certificate(alias, cert_pem)
                imported[str(cert.subject)] = alias

            log_operation_end(
                self.logger,
                "import_server_certificates",
                success=True,
                url=url,
                keystore=keystore_manager.keystore_file,
                imported=len(imported),
            )

            return imported
        except Exception as e:
            log_operation_end(
                self.logger,
                "import_server_certificates",
                success=False,
                url=url,
                keystore=keystore_manager.keystore_file if keystore_manager else None,
                error=str(e),
            )
            raise ValidationError(f"Failed to import server certificates: {str(e)}")

    def establish_tls_connection(
        self, url: str, timeout: int = 10
    ) -> Tuple[ssl.SSLSocket, Dict[str, str]]:
        """Establish a TLS connection to a server.

        Args:
            url: URL to connect to
            timeout: Connection timeout in seconds

        Returns:
            Tuple of (SSL socket, connection details)

        Raises:
            ValidationError: If the connection cannot be established
        """
        log_operation_start(
            self.logger, "establish_tls_connection", url=url, timeout=timeout
        )

        try:
            # Parse URL and add scheme if missing
            if not url.startswith(('http://', 'https://')):
                url = f"https://{url}"
                self.logger.debug(f"Added https:// scheme to URL: {url}")
                
            parsed_url = urllib.parse.urlparse(url)
            hostname = parsed_url.hostname
            port = parsed_url.port or 443

            if not hostname:
                raise ValidationError(f"Invalid URL: {url}")

            # Create SSL context
            context = ssl.create_default_context()
            
            # Connect to server
            sock = socket.create_connection((hostname, port), timeout=timeout)
            ssl_sock = context.wrap_socket(sock, server_hostname=hostname)

            # Get connection details
            connection_details = {
                "cipher": ssl_sock.cipher(),
                "version": ssl_sock.version(),
                "peer_cert": ssl_sock.getpeercert(),
            }

            log_operation_end(
                self.logger,
                "establish_tls_connection",
                success=True,
                url=url,
                cipher=connection_details["cipher"],
                version=connection_details["version"],
            )

            return ssl_sock, connection_details
        except Exception as e:
            log_operation_end(
                self.logger,
                "establish_tls_connection",
                success=False,
                url=url,
                error=str(e),
            )
            raise ValidationError(f"Failed to establish TLS connection: {str(e)}")

    def compare_certificates(
        self, cert1: x509.Certificate, cert2: x509.Certificate
    ) -> Tuple[bool, Dict[str, bool]]:
        """Compare two certificates.

        Args:
            cert1: First certificate
            cert2: Second certificate

        Returns:
            Tuple of (match result, comparison details)
        """
        comparison = {}

        # Compare subject
        comparison["subject"] = cert1.subject == cert2.subject

        # Compare issuer
        comparison["issuer"] = cert1.issuer == cert2.issuer

        # Compare public key
        comparison["public_key"] = cert1.public_key().public_bytes(
            serialization.Encoding.DER,
            serialization.PublicFormat.SubjectPublicKeyInfo,
        ) == cert2.public_key().public_bytes(
            serialization.Encoding.DER,
            serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        # Compare serial number
        comparison["serial_number"] = cert1.serial_number == cert2.serial_number

        # Compare not before/after
        comparison["not_before"] = cert1.not_valid_before == cert2.not_valid_before
        comparison["not_after"] = cert1.not_valid_after == cert2.not_valid_after

        # Overall match
        match = all(comparison.values())

        return match, comparison
