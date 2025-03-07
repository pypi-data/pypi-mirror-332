"""Wrapper for CLI tools like keytool and openssl."""

import json
import re
import shlex
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from pytruststore.logging_config import get_logger, log_cli_execution

# Initialize logger
logger = get_logger(__name__)


class CLIError(Exception):
    """Exception raised for errors in CLI tool execution."""

    def __init__(self, message: str, command: str, returncode: int, output: str):
        """Initialize CLIError.

        Args:
            message: Error message
            command: Command that was executed
            returncode: Return code from the command
            output: Command output
        """
        self.message = message
        self.command = command
        self.returncode = returncode
        self.output = output
        super().__init__(f"{message} (return code: {returncode})")


class KeytoolWrapper:
    """Wrapper for Java keytool CLI."""

    def __init__(self, keytool_path: str = "keytool"):
        """Initialize KeytoolWrapper.

        Args:
            keytool_path: Path to keytool executable
        """
        self.keytool_path = keytool_path
        self.logger = get_logger(__name__)

    def execute(
        self, args: List[str], capture_output: bool = True, check: bool = True
    ) -> subprocess.CompletedProcess:
        """Execute keytool with the given arguments.

        Args:
            args: Arguments to pass to keytool
            capture_output: Whether to capture stdout/stderr
            check: Whether to check the return code

        Returns:
            CompletedProcess instance with return code, stdout, and stderr

        Raises:
            CLIError: If the command fails and check is True
        """
        cmd = [self.keytool_path] + args
        cmd_str = " ".join([shlex.quote(arg) for arg in cmd])

        # Log the command (with password masked)
        masked_cmd = cmd_str
        if "-storepass" in masked_cmd:
            masked_cmd = re.sub(r"-storepass\s+\S+", "-storepass ********", masked_cmd)
        if "-keypass" in masked_cmd:
            masked_cmd = re.sub(r"-keypass\s+\S+", "-keypass ********", masked_cmd)

        log_cli_execution(self.logger, "keytool", masked_cmd)

        try:
            result = subprocess.run(
                cmd,
                capture_output=capture_output,
                text=True,
                check=False,
            )

            if check and result.returncode != 0:
                raise CLIError(
                    "Keytool command failed",
                    masked_cmd,
                    result.returncode,
                    result.stderr,
                )

            return result
        except subprocess.SubprocessError as e:
            self.logger.error("Keytool execution failed", error=str(e), cmd=masked_cmd)
            raise CLIError(
                "Keytool execution failed", masked_cmd, -1, str(e)
            ) from e

    def list_keystore(
        self, keystore_file: str, password: str, detailed: bool = False
    ) -> str:
        """List certificates in a keystore.

        Args:
            keystore_file: Path to the keystore file
            password: Keystore password
            detailed: Whether to show detailed information

        Returns:
            Output from keytool -list command
        """
        args = ["-list", "-keystore", keystore_file, "-storepass", password]
        if detailed:
            args.append("-v")

        result = self.execute(args)
        return result.stdout

    def get_certificate(
        self, keystore_file: str, password: str, alias: str
    ) -> str:
        """Get a certificate from a keystore.

        Args:
            keystore_file: Path to the keystore file
            password: Keystore password
            alias: Certificate alias

        Returns:
            Certificate in PEM format
        """
        # First export to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".cer") as temp_file:
            args = [
                "-exportcert",
                "-keystore",
                keystore_file,
                "-storepass",
                password,
                "-alias",
                alias,
                "-file",
                temp_file.name,
                "-rfc",
            ]
            self.execute(args)

            # Read the certificate
            return Path(temp_file.name).read_text()

    def import_certificate(
        self,
        keystore_file: str,
        password: str,
        alias: str,
        cert_file: str,
        trust: bool = True,
    ) -> bool:
        """Import a certificate into a keystore.

        Args:
            keystore_file: Path to the keystore file
            password: Keystore password
            alias: Alias to use for the certificate
            cert_file: Path to the certificate file
            trust: Whether to trust the certificate

        Returns:
            True if the import was successful
        """
        args = [
            "-importcert",
            "-keystore",
            keystore_file,
            "-storepass",
            password,
            "-alias",
            alias,
            "-file",
            cert_file,
        ]

        if trust:
            args.append("-noprompt")

        try:
            self.execute(args)
            return True
        except CLIError as e:
            if "already exists" in e.output:
                self.logger.warning(
                    "Certificate already exists in keystore",
                    alias=alias,
                    keystore=keystore_file,
                )
                return False
            raise

    def delete_certificate(
        self, keystore_file: str, password: str, alias: str
    ) -> bool:
        """Delete a certificate from a keystore.

        Args:
            keystore_file: Path to the keystore file
            password: Keystore password
            alias: Certificate alias

        Returns:
            True if the deletion was successful
        """
        args = [
            "-delete",
            "-keystore",
            keystore_file,
            "-storepass",
            password,
            "-alias",
            alias,
        ]

        try:
            self.execute(args)
            return True
        except CLIError as e:
            if "does not exist" in e.output:
                self.logger.warning(
                    "Certificate does not exist in keystore",
                    alias=alias,
                    keystore=keystore_file,
                )
                return False
            raise

    def parse_list_output(self, output: str) -> Dict[str, Dict[str, str]]:
        """Parse the output of keytool -list -v.

        Args:
            output: Output from keytool -list -v

        Returns:
            Dictionary mapping aliases to certificate information
        """
        result = {}
        current_alias = None
        current_info = {}
        in_certificate = False

        for line in output.splitlines():
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Check for alias
            alias_match = re.match(r"Alias name: (.+)", line)
            if alias_match:
                # Save previous entry if it exists
                if current_alias:
                    result[current_alias] = current_info

                # Start new entry
                current_alias = alias_match.group(1)
                current_info = {"alias": current_alias}
                in_certificate = False
                continue

            # Skip certificate content
            if "Certificate chain length:" in line:
                in_certificate = True
                continue

            if in_certificate and "-----BEGIN CERTIFICATE-----" in line:
                continue
            if in_certificate and "-----END CERTIFICATE-----" in line:
                in_certificate = False
                continue
            if in_certificate:
                continue

            # Extract key-value pairs
            kv_match = re.match(r"([^:]+):\s*(.+)", line)
            if kv_match:
                key = kv_match.group(1).strip().lower().replace(" ", "_")
                value = kv_match.group(2).strip()
                current_info[key] = value

        # Save the last entry
        if current_alias:
            result[current_alias] = current_info

        return result


class OpenSSLWrapper:
    """Wrapper for OpenSSL CLI."""

    def __init__(self, openssl_path: str = "openssl"):
        """Initialize OpenSSLWrapper.

        Args:
            openssl_path: Path to openssl executable
        """
        self.openssl_path = openssl_path
        self.logger = get_logger(__name__)

    def execute(
        self, args: List[str], capture_output: bool = True, check: bool = True
    ) -> subprocess.CompletedProcess:
        """Execute openssl with the given arguments.

        Args:
            args: Arguments to pass to openssl
            capture_output: Whether to capture stdout/stderr
            check: Whether to check the return code

        Returns:
            CompletedProcess instance with return code, stdout, and stderr

        Raises:
            CLIError: If the command fails and check is True
        """
        cmd = [self.openssl_path] + args
        cmd_str = " ".join([shlex.quote(arg) for arg in cmd])

        log_cli_execution(self.logger, "openssl", cmd_str)

        try:
            result = subprocess.run(
                cmd,
                capture_output=capture_output,
                text=True,
                check=False,
            )

            if check and result.returncode != 0:
                raise CLIError(
                    "OpenSSL command failed",
                    cmd_str,
                    result.returncode,
                    result.stderr,
                )

            return result
        except subprocess.SubprocessError as e:
            self.logger.error("OpenSSL execution failed", error=str(e), cmd=cmd_str)
            raise CLIError(
                "OpenSSL execution failed", cmd_str, -1, str(e)
            ) from e

    def get_server_certificate(self, host: str, port: int = 443) -> str:
        """Get a server's certificate.

        Args:
            host: Hostname
            port: Port number

        Returns:
            Certificate in PEM format
        """
        args = ["s_client", "-connect", f"{host}:{port}", "-showcerts"]
        result = self.execute(args, check=False)

        # Extract certificate from output
        cert_pattern = r"-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----"
        certs = re.findall(cert_pattern, result.stdout, re.DOTALL)

        if not certs:
            raise CLIError(
                "No certificates found in OpenSSL output",
                " ".join(args),
                result.returncode,
                result.stdout,
            )

        return certs[0]  # Return the first certificate (server cert)

    def get_certificate_chain(self, host: str, port: int = 443) -> List[str]:
        """Get a server's certificate chain.

        Args:
            host: Hostname
            port: Port number

        Returns:
            List of certificates in PEM format
        """
        args = ["s_client", "-connect", f"{host}:{port}", "-showcerts"]
        result = self.execute(args, check=False)

        # Extract certificates from output
        cert_pattern = r"-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----"
        return re.findall(cert_pattern, result.stdout, re.DOTALL)

    def get_certificate_info(self, cert_pem: str) -> Dict[str, str]:
        """Get information about a certificate.

        Args:
            cert_pem: Certificate in PEM format

        Returns:
            Dictionary with certificate information
        """
        # Write certificate to temporary file
        with tempfile.NamedTemporaryFile(suffix=".pem", mode="w") as temp_file:
            temp_file.write(cert_pem)
            temp_file.flush()

            # Get certificate information
            args = ["x509", "-in", temp_file.name, "-text", "-noout"]
            result = self.execute(args)

            # Parse output
            info = {}
            current_section = None

            for line in result.stdout.splitlines():
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Check for section headers
                if line.endswith(":"):
                    current_section = line[:-1].lower().replace(" ", "_")
                    info[current_section] = []
                    continue

                # Add line to current section
                if current_section:
                    info[current_section].append(line)

            # Extract subject and issuer
            subject_match = re.search(r"Subject: (.+)", result.stdout)
            if subject_match:
                info["subject"] = subject_match.group(1).strip()

            issuer_match = re.search(r"Issuer: (.+)", result.stdout)
            if issuer_match:
                info["issuer"] = issuer_match.group(1).strip()

            # Extract validity
            not_before_match = re.search(r"Not Before: (.+)", result.stdout)
            if not_before_match:
                info["not_before"] = not_before_match.group(1).strip()

            not_after_match = re.search(r"Not After : (.+)", result.stdout)
            if not_after_match:
                info["not_after"] = not_after_match.group(1).strip()

            return info

    def verify_certificate(
        self, cert_pem: str, ca_file: Optional[str] = None
    ) -> bool:
        """Verify a certificate against a CA file.

        Args:
            cert_pem: Certificate in PEM format
            ca_file: Path to CA file

        Returns:
            True if the certificate is valid
        """
        # Write certificate to temporary file
        with tempfile.NamedTemporaryFile(suffix=".pem", mode="w") as temp_file:
            temp_file.write(cert_pem)
            temp_file.flush()

            # Verify certificate
            args = ["verify"]
            if ca_file:
                args.extend(["-CAfile", ca_file])
            args.append(temp_file.name)

            try:
                self.execute(args)
                return True
            except CLIError:
                return False
