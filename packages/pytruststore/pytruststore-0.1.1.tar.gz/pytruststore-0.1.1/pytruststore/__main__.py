"""Command-line interface for PyTrustStore."""

import os
import sys
from typing import Dict, List, Optional, Tuple

import click
from rich.console import Console
from rich.panel import Panel

from pytruststore.alias import AliasManager
from pytruststore.keystore import KeystoreManager
from pytruststore.logging_config import configure_logging, get_logger
from pytruststore.utils import (
    generate_operation_id,
    print_alias_suggestions,
    print_certificate_chain,
    print_certificate_info,
    print_keystore_aliases,
    print_validation_results,
)
from pytruststore.validation import TLSValidator

# Initialize console
console = Console()

# Configure logging
configure_logging()

# Initialize logger
logger = get_logger(__name__)


# Common options
keystore_option = click.option(
    "--keystore",
    "-k",
    required=True,
    help="Path to the keystore file",
    type=click.Path(exists=False),
)
password_option = click.option(
    "--password",
    "-p",
    required=True,
    help="Keystore password",
    envvar="KEYSTORE_PASSWORD",
)
alias_option = click.option(
    "--alias",
    "-a",
    required=True,
    help="Certificate alias",
)
verbose_option = click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable verbose output",
)


@click.group()
@click.version_option()
@click.option(
    "--log-level",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]),
    default="INFO",
    help="Set the logging level",
)
@click.option(
    "--log-file",
    type=click.Path(),
    help="Log to a specific file",
)
@click.pass_context
def cli(ctx: click.Context, log_level: str, log_file: Optional[str]) -> None:
    """PyTrustStore: A Python application for working with Java keystore files.

    This tool provides various operations for working with Java keystores, including
    validation, querying, importing certificates, and managing aliases.
    """
    # Generate operation ID
    operation_id = generate_operation_id()
    
    # Configure logging
    configure_logging(log_level, log_file, operation_id)
    
    # Initialize context
    ctx.ensure_object(dict)
    ctx.obj["operation_id"] = operation_id


@cli.command()
@keystore_option
@password_option
@click.option(
    "--url",
    "-u",
    required=True,
    help="URL to validate against",
)
@verbose_option
@click.pass_context
def validate(
    ctx: click.Context,
    keystore: str,
    password: str,
    url: str,
    verbose: bool,
) -> None:
    """Validate a keystore against a remote TLS resource.

    This command establishes a TLS connection to the specified URL, retrieves the
    server's certificate chain, and compares it with the certificates in the keystore.
    """
    try:
        # Initialize keystore manager
        keystore_manager = KeystoreManager(keystore, password)
        keystore_manager.load_keystore()
        
        # Initialize validator
        validator = TLSValidator(keystore_manager)
        
        # Validate against keystore
        console.print(f"Validating [cyan]{url}[/cyan] against keystore [cyan]{keystore}[/cyan]...")
        result, details = validator.validate_against_keystore(url)
        
        # Print results
        print_validation_results(details)
        
        # Exit with appropriate status code
        sys.exit(0 if result else 1)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"Validation failed", error=str(e))
        sys.exit(1)


@cli.command()
@keystore_option
@password_option
@click.option(
    "--detailed",
    "-d",
    is_flag=True,
    help="Show detailed information",
)
@verbose_option
@click.pass_context
def list(
    ctx: click.Context,
    keystore: str,
    password: str,
    detailed: bool,
    verbose: bool,
) -> None:
    """List all aliases in a keystore.

    This command lists all aliases in the specified keystore. If the --detailed
    option is specified, it also shows expiry information for each certificate.
    """
    try:
        # Initialize keystore manager
        keystore_manager = KeystoreManager(keystore, password)
        keystore_manager.load_keystore()
        
        # Get aliases
        aliases = keystore_manager.list_aliases()
        
        if not aliases:
            console.print("[yellow]No aliases found in keystore[/yellow]")
            return
        
        # Get expiry information if detailed
        expiry_info = None
        if detailed:
            alias_manager = AliasManager(keystore_manager)
            expiry_info = alias_manager.get_alias_expiry_info()
        
        # Print aliases
        print_keystore_aliases(aliases, expiry_info)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"List operation failed", error=str(e))
        sys.exit(1)


@cli.command()
@keystore_option
@password_option
@alias_option
@click.option(
    "--chain",
    "-c",
    is_flag=True,
    help="Show certificate chain",
)
@verbose_option
@click.pass_context
def info(
    ctx: click.Context,
    keystore: str,
    password: str,
    alias: str,
    chain: bool,
    verbose: bool,
) -> None:
    """Get detailed information about a certificate.

    This command retrieves detailed information about a certificate in the keystore.
    If the --chain option is specified, it also shows the certificate chain.
    """
    try:
        # Initialize keystore manager
        keystore_manager = KeystoreManager(keystore, password)
        keystore_manager.load_keystore()
        
        if chain:
            # Get certificate chain
            cert_chain = keystore_manager.get_certificate_chain(alias)
            print_certificate_chain(cert_chain)
        else:
            # Get certificate
            cert = keystore_manager.get_certificate(alias)
            print_certificate_info(cert)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"Info operation failed", error=str(e))
        sys.exit(1)


@cli.command(name="import")
@keystore_option
@password_option
@click.option(
    "--url",
    "-u",
    required=True,
    help="URL to import certificates from",
)
@click.option(
    "--prefix",
    "-x",
    help="Prefix for certificate aliases",
)
@click.option(
    "--overwrite",
    "-o",
    is_flag=True,
    help="Overwrite existing certificates",
)
@verbose_option
@click.pass_context
def import_certificates(
    ctx: click.Context,
    keystore: str,
    password: str,
    url: str,
    prefix: Optional[str],
    overwrite: bool,
    verbose: bool,
) -> None:
    """Import server certificates from a URL.

    This command establishes a TLS connection to the specified URL, retrieves the
    server's certificate chain, and adds these certificates to the keystore.
    """
    # Call the import_url function to avoid code duplication
    import_url(ctx, keystore, password, url, prefix, overwrite, verbose)


@cli.command()
@keystore_option
@password_option
@click.option(
    "--url",
    "-u",
    required=True,
    help="URL to import certificates from",
)
@click.option(
    "--prefix",
    "-x",
    help="Prefix for certificate aliases",
)
@click.option(
    "--overwrite",
    "-o",
    is_flag=True,
    help="Overwrite existing certificates",
)
@verbose_option
@click.pass_context
def import_url(
    ctx: click.Context,
    keystore: str,
    password: str,
    url: str,
    prefix: Optional[str],
    overwrite: bool,
    verbose: bool,
) -> None:
    """Import server certificates from a URL.

    This command establishes a TLS connection to the specified URL, retrieves the
    server's certificate chain, and adds these certificates to the keystore.
    """
    try:
        # Initialize keystore manager
        keystore_manager = KeystoreManager(keystore, password)
        
        # Create keystore if it doesn't exist
        if not os.path.exists(keystore):
            console.print(f"Keystore [cyan]{keystore}[/cyan] does not exist, creating...")
            keystore_manager.create_empty_keystore(keystore, password)
        else:
            keystore_manager.load_keystore()
        
        # Initialize validator
        validator = TLSValidator(keystore_manager)
        
        # Import certificates
        console.print(f"Importing certificates from [cyan]{url}[/cyan]...")
        imported = validator.import_server_certificates(url, keystore_manager, prefix, overwrite)
        
        # Print results
        console.print(f"[green]Successfully imported {len(imported)} certificates[/green]")
        for subject, alias in imported.items():
            console.print(f"  [cyan]{alias}[/cyan]: {subject}")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"Import operation failed", error=str(e))
        sys.exit(1)


@cli.command()
@keystore_option
@password_option
@alias_option
@click.option(
    "--new-alias",
    "-n",
    required=True,
    help="New certificate alias",
)
@verbose_option
@click.pass_context
def rename(
    ctx: click.Context,
    keystore: str,
    password: str,
    alias: str,
    new_alias: str,
    verbose: bool,
) -> None:
    """Rename a certificate alias.

    This command renames a certificate alias in the keystore.
    """
    try:
        # Initialize keystore manager
        keystore_manager = KeystoreManager(keystore, password)
        keystore_manager.load_keystore()
        
        # Rename alias
        console.print(f"Renaming alias [cyan]{alias}[/cyan] to [cyan]{new_alias}[/cyan]...")
        keystore_manager.rename_alias(alias, new_alias)
        
        console.print(f"[green]Successfully renamed alias[/green]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"Rename operation failed", error=str(e))
        sys.exit(1)


@cli.command()
@keystore_option
@password_option
@click.option(
    "--dry-run",
    "-d",
    is_flag=True,
    help="Show what would be renamed without making changes",
)
@verbose_option
@click.pass_context
def auto_rename(
    ctx: click.Context,
    keystore: str,
    password: str,
    dry_run: bool,
    verbose: bool,
) -> None:
    """Auto-rename all aliases to be more descriptive.

    This command renames all aliases in the keystore to be more descriptive,
    based on certificate attributes.
    """
    try:
        # Initialize keystore manager
        keystore_manager = KeystoreManager(keystore, password)
        keystore_manager.load_keystore()
        
        # Initialize alias manager
        alias_manager = AliasManager(keystore_manager)
        
        if dry_run:
            # Get suggestions
            console.print("Generating alias suggestions...")
            suggestions = alias_manager.suggest_alias_improvements()
            
            if not suggestions:
                console.print("[yellow]No aliases need renaming[/yellow]")
                return
            
            # Print suggestions
            print_alias_suggestions(suggestions)
        else:
            # Rename aliases
            console.print("Renaming aliases...")
            renamed = alias_manager.rename_to_descriptive_aliases()
            
            if not renamed:
                console.print("[yellow]No aliases were renamed[/yellow]")
                return
            
            # Print results
            console.print(f"[green]Successfully renamed {len(renamed)} aliases[/green]")
            for old_alias, new_alias in renamed.items():
                console.print(f"  [cyan]{old_alias}[/cyan] -> [green]{new_alias}[/green]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"Auto-rename operation failed", error=str(e))
        sys.exit(1)


@cli.command()
@keystore_option
@password_option
@click.option(
    "--subject",
    "-s",
    help="Subject to search for",
)
@click.option(
    "--issuer",
    "-i",
    help="Issuer to search for",
)
@click.option(
    "--serial",
    "-n",
    help="Serial number to search for",
)
@verbose_option
@click.pass_context
def search(
    ctx: click.Context,
    keystore: str,
    password: str,
    subject: Optional[str],
    issuer: Optional[str],
    serial: Optional[str],
    verbose: bool,
) -> None:
    """Search for certificates in a keystore.

    This command searches for certificates in the keystore based on various criteria.
    """
    try:
        # Initialize keystore manager
        keystore_manager = KeystoreManager(keystore, password)
        keystore_manager.load_keystore()
        
        # Check if at least one search criterion is specified
        if not subject and not issuer and not serial:
            console.print("[yellow]At least one search criterion must be specified[/yellow]")
            return
        
        # Search certificates
        console.print("Searching certificates...")
        matches = keystore_manager.search_certificates(subject, issuer, serial)
        
        if not matches:
            console.print("[yellow]No matching certificates found[/yellow]")
            return
        
        # Print results
        console.print(f"[green]Found {len(matches)} matching certificates[/green]")
        for alias in matches:
            console.print(f"  [cyan]{alias}[/cyan]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"Search operation failed", error=str(e))
        sys.exit(1)


@cli.command()
@keystore_option
@password_option
@alias_option
@click.option(
    "--output",
    "-o",
    required=True,
    help="Output file path",
    type=click.Path(),
)
@click.option(
    "--chain",
    "-c",
    is_flag=True,
    help="Export certificate chain",
)
@verbose_option
@click.pass_context
def export(
    ctx: click.Context,
    keystore: str,
    password: str,
    alias: str,
    output: str,
    chain: bool,
    verbose: bool,
) -> None:
    """Export a certificate from a keystore.

    This command exports a certificate from the keystore to a file.
    """
    try:
        # Initialize keystore manager
        keystore_manager = KeystoreManager(keystore, password)
        keystore_manager.load_keystore()
        
        if chain:
            # Get certificate chain
            cert_chain = keystore_manager.get_certificate_chain(alias)
            
            # Convert to PEM format
            pem_chain = []
            for cert in cert_chain:
                pem = cert.public_bytes(encoding=click.get_current_context().obj.get("encoding", "PEM")).decode("utf-8")
                pem_chain.append(pem)
            
            # Write to file
            with open(output, "w") as f:
                f.write("\n".join(pem_chain))
        else:
            # Get certificate
            pem = keystore_manager.get_certificate_pem(alias)
            
            # Write to file
            with open(output, "w") as f:
                f.write(pem)
        
        console.print(f"[green]Successfully exported certificate to {output}[/green]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"Export operation failed", error=str(e))
        sys.exit(1)


@cli.command()
@click.pass_context
def version(ctx: click.Context) -> None:
    """Show version information."""
    from pytruststore import __version__
    
    console.print(Panel.fit(
        f"[bold cyan]PyTrustStore[/bold cyan] [green]v{__version__}[/green]\n\n"
        f"A Python application for working with Java keystore files.\n\n"
        f"[bold]Features:[/bold]\n"
        f"- Validate keystores against remote TLS resources\n"
        f"- Query keystores for certificates and aliases\n"
        f"- Get detailed information about keystore resources\n"
        f"- Import server certificates and their CA chains\n"
        f"- Make aliases explanatory and easy to understand\n\n"
        f"[bold]Author:[/bold] GLIC Team\n"
        f"[bold]License:[/bold] Apache License 2.0",
        title="About",
        border_style="cyan",
    ))


def main() -> None:
    """Main entry point for the application."""
    try:
        cli()
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        logger.error(f"Unhandled exception", error=str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
