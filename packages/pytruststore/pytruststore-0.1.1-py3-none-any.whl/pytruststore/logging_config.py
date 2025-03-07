"""Logging configuration for PyTrustStore."""

import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Union

import structlog
from rich.console import Console
from rich.logging import RichHandler

# Create logs directory if it doesn't exist
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Configure console for rich output
console = Console()


def configure_logging(
    log_level: str = "INFO",
    log_file: Optional[str] = None,
    operation_id: Optional[str] = None,
) -> None:
    """Configure logging for the application.

    Args:
        log_level: The log level to use (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file to log to (in addition to the default logs)
        operation_id: Optional operation ID to include in logs
    """
    # Convert string log level to numeric value
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)

    # Configure structlog processors
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
    ]

    # Add operation ID if provided
    if operation_id:
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(operation_id=operation_id)

    # Configure structlog
    structlog.configure(
        processors=processors + [structlog.stdlib.ProcessorFormatter.wrap_for_formatter],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    # Create default log file based on date
    if not log_file:
        timestamp = datetime.now().strftime("%Y%m%d")
        log_file = LOGS_DIR / f"pytruststore-{timestamp}.log"

    # Configure handlers
    handlers = [
        # Rich console handler
        RichHandler(
            console=console,
            rich_tracebacks=True,
            markup=True,
            show_time=True,
            show_level=True,
            show_path=True,
        ),
        # File handler
        logging.FileHandler(log_file),
    ]

    # Configure logging
    logging.basicConfig(
        level=numeric_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=handlers,
    )

    # Log configuration info
    logger = get_logger("logging_config")
    logger.info(
        "Logging configured",
        log_level=log_level,
        log_file=str(log_file),
        operation_id=operation_id,
    )


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """Get a logger with the given name.

    Args:
        name: The name of the logger

    Returns:
        A structlog logger
    """
    return structlog.get_logger(name)


def log_operation_start(
    logger: structlog.stdlib.BoundLogger, operation: str, **kwargs
) -> None:
    """Log the start of an operation.

    Args:
        logger: The logger to use
        operation: The name of the operation
        **kwargs: Additional context to include in the log
    """
    logger.info(f"Starting operation: {operation}", operation=operation, **kwargs)


def log_operation_end(
    logger: structlog.stdlib.BoundLogger,
    operation: str,
    success: bool = True,
    **kwargs,
) -> None:
    """Log the end of an operation.

    Args:
        logger: The logger to use
        operation: The name of the operation
        success: Whether the operation was successful
        **kwargs: Additional context to include in the log
    """
    status = "succeeded" if success else "failed"
    logger.info(
        f"Operation {operation} {status}",
        operation=operation,
        success=success,
        **kwargs,
    )


def log_keystore_operation(
    logger: structlog.stdlib.BoundLogger,
    operation: str,
    keystore_file: str,
    **kwargs,
) -> None:
    """Log a keystore operation.

    Args:
        logger: The logger to use
        operation: The name of the operation
        keystore_file: The keystore file being operated on
        **kwargs: Additional context to include in the log
    """
    # Mask password if present in kwargs
    if "password" in kwargs:
        kwargs["password"] = "********"

    logger.info(
        f"Keystore operation: {operation}",
        operation=operation,
        keystore_file=keystore_file,
        **kwargs,
    )


def log_certificate_operation(
    logger: structlog.stdlib.BoundLogger,
    operation: str,
    alias: Optional[str] = None,
    **kwargs,
) -> None:
    """Log a certificate operation.

    Args:
        logger: The logger to use
        operation: The name of the operation
        alias: The alias of the certificate being operated on
        **kwargs: Additional context to include in the log
    """
    logger.info(
        f"Certificate operation: {operation}",
        operation=operation,
        alias=alias,
        **kwargs,
    )


def log_cli_execution(
    logger: structlog.stdlib.BoundLogger,
    tool: str,
    command: str,
    **kwargs,
) -> None:
    """Log a CLI tool execution.

    Args:
        logger: The logger to use
        tool: The CLI tool being executed (keytool, openssl)
        command: The command being executed
        **kwargs: Additional context to include in the log
    """
    # Mask password if present in command
    if "-storepass" in command or "-keypass" in command:
        # Simple masking - in a real app, this would be more sophisticated
        command = command.replace("-storepass", "-storepass ********")
        command = command.replace("-keypass", "-keypass ********")

    logger.info(
        f"Executing {tool} command",
        tool=tool,
        command=command,
        **kwargs,
    )
