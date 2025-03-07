"""Utility functions for PyTrustStore."""

import os
import re
import tempfile
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.x509 import load_pem_x509_certificate
from rich.console import Console
from rich.table import Table

from pytruststore.logging_config import get_logger

# Initialize logger
logger = get_logger(__name__)

# Initialize console
console = Console()


def generate_operation_id() -> str:
    """Generate a unique operation ID.

    Returns:
        Unique operation ID
    """
    return str(uuid.uuid4())


def format_certificate_subject(subject: x509.Name) -> str:
    """Format a certificate subject for display.

    Args:
        subject: Certificate subject

    Returns:
        Formatted subject string
    """
    subject_parts = []
    
    # Common Name
    cn = subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)
    if cn:
        subject_parts.append(f"CN={cn[0].value}")
    
    # Organization
    org = subject.get_attributes_for_oid(x509.NameOID.ORGANIZATION_NAME)
    if org:
        subject_parts.append(f"O={org[0].value}")
    
    # Organizational Unit
    ou = subject.get_attributes_for_oid(x509.NameOID.ORGANIZATIONAL_UNIT_NAME)
    if ou:
        subject_parts.append(f"OU={ou[0].value}")
    
    # Country
    country = subject.get_attributes_for_oid(x509.NameOID.COUNTRY_NAME)
    if country:
        subject_parts.append(f"C={country[0].value}")
    
    # State/Province
    state = subject.get_attributes_for_oid(x509.NameOID.STATE_OR_PROVINCE_NAME)
    if state:
        subject_parts.append(f"ST={state[0].value}")
    
    # Locality
    locality = subject.get_attributes_for_oid(x509.NameOID.LOCALITY_NAME)
    if locality:
        subject_parts.append(f"L={locality[0].value}")
    
    return ", ".join(subject_parts)


def format_certificate_info(cert: x509.Certificate) -> Dict[str, str]:
    """Format certificate information for display.

    Args:
        cert: Certificate to format

    Returns:
        Dictionary with formatted certificate information
    """
    info = {}
    
    # Subject
    info["subject"] = format_certificate_subject(cert.subject)
    
    # Issuer
    info["issuer"] = format_certificate_subject(cert.issuer)
    
    # Serial Number
    info["serial_number"] = f"{cert.serial_number:x}"
    
    # Validity
    info["not_before"] = cert.not_valid_before.strftime("%Y-%m-%d %H:%M:%S")
    info["not_after"] = cert.not_valid_after.strftime("%Y-%m-%d %H:%M:%S")
    
    # Public Key
    public_key = cert.public_key()
    if hasattr(public_key, "key_size"):
        info["key_size"] = str(public_key.key_size)
    
    # Signature Algorithm
    info["signature_algorithm"] = cert.signature_algorithm_oid._name
    
    # Extensions
    extensions = []
    for extension in cert.extensions:
        extensions.append(f"{extension.oid._name}")
    info["extensions"] = ", ".join(extensions)
    
    return info


def print_certificate_info(cert: x509.Certificate) -> None:
    """Print certificate information to the console.

    Args:
        cert: Certificate to print
    """
    info = format_certificate_info(cert)
    
    table = Table(title="Certificate Information")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    
    for field, value in info.items():
        table.add_row(field.replace("_", " ").title(), value)
    
    console.print(table)


def print_certificate_chain(chain: List[x509.Certificate]) -> None:
    """Print certificate chain to the console.

    Args:
        chain: Certificate chain to print
    """
    table = Table(title="Certificate Chain")
    table.add_column("#", style="cyan")
    table.add_column("Subject", style="green")
    table.add_column("Issuer", style="yellow")
    table.add_column("Expiry", style="magenta")
    
    for i, cert in enumerate(chain):
        subject = format_certificate_subject(cert.subject)
        issuer = format_certificate_subject(cert.issuer)
        expiry = cert.not_valid_after.strftime("%Y-%m-%d")
        
        table.add_row(str(i + 1), subject, issuer, expiry)
    
    console.print(table)


def print_keystore_aliases(aliases: List[str], expiry_info: Optional[Dict[str, Dict[str, str]]] = None) -> None:
    """Print keystore aliases to the console.

    Args:
        aliases: List of aliases
        expiry_info: Optional dictionary mapping aliases to expiry information
    """
    table = Table(title="Keystore Aliases")
    table.add_column("Alias", style="cyan")
    
    if expiry_info:
        table.add_column("Expiry Date", style="green")
        table.add_column("Days Until Expiry", style="yellow")
        table.add_column("Status", style="magenta")
        
        for alias in aliases:
            if alias in expiry_info:
                info = expiry_info[alias]
                status_style = {
                    "expired": "red",
                    "expiring_soon": "yellow",
                    "valid": "green",
                    "error": "red",
                }.get(info["status"], "white")
                
                table.add_row(
                    alias,
                    info["expiry_date"],
                    info["days_until_expiry"],
                    info["status"],
                    style=status_style,
                )
            else:
                table.add_row(alias, "", "", "")
    else:
        for alias in aliases:
            table.add_row(alias)
    
    console.print(table)


def print_validation_results(results: Dict[str, str]) -> None:
    """Print validation results to the console.

    Args:
        results: Validation results
    """
    table = Table(title="Validation Results")
    table.add_column("Certificate", style="cyan")
    table.add_column("Found", style="green")
    table.add_column("Alias", style="yellow")
    table.add_column("Subject", style="magenta")
    
    all_found = results.get("all_found", False)
    
    for key, value in results.items():
        if key.startswith("cert_"):
            found_style = "green" if value["found"] else "red"
            found_text = "Yes" if value["found"] else "No"
            alias = value.get("alias", "")
            subject = value.get("subject", "")
            
            table.add_row(key, found_text, alias, subject, style=found_style)
    
    console.print(table)
    
    if all_found:
        console.print("[green]All certificates found in keystore[/green]")
    else:
        console.print("[red]Some certificates not found in keystore[/red]")


def print_alias_suggestions(suggestions: Dict[str, str]) -> None:
    """Print alias suggestions to the console.

    Args:
        suggestions: Dictionary mapping current aliases to suggested aliases
    """
    table = Table(title="Alias Suggestions")
    table.add_column("Current Alias", style="cyan")
    table.add_column("Suggested Alias", style="green")
    
    for current, suggested in suggestions.items():
        table.add_row(current, suggested)
    
    console.print(table)


def create_temp_file(content: str, suffix: str = ".tmp") -> str:
    """Create a temporary file with the given content.

    Args:
        content: File content
        suffix: File suffix

    Returns:
        Path to the temporary file
    """
    fd, path = tempfile.mkstemp(suffix=suffix)
    try:
        with os.fdopen(fd, "w") as f:
            f.write(content)
        return path
    except Exception as e:
        logger.error(f"Error creating temporary file", error=str(e))
        os.unlink(path)
        raise


def parse_url(url: str) -> Tuple[str, int]:
    """Parse a URL into hostname and port.

    Args:
        url: URL to parse

    Returns:
        Tuple of (hostname, port)

    Raises:
        ValueError: If the URL is invalid
    """
    # Add scheme if missing
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"
    
    # Parse URL
    match = re.match(r"https?://([^:/]+)(?::(\d+))?", url)
    if not match:
        raise ValueError(f"Invalid URL: {url}")
    
    hostname = match.group(1)
    port = int(match.group(2)) if match.group(2) else (443 if url.startswith("https") else 80)
    
    return hostname, port
