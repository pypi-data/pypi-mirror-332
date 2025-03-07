"""Alias management functionality for PyTrustStore."""

import re
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID

from pytruststore.keystore import KeystoreManager
from pytruststore.logging_config import (
    get_logger,
    log_certificate_operation,
    log_operation_start,
    log_operation_end,
)

# Initialize logger
logger = get_logger(__name__)


class AliasError(Exception):
    """Exception raised for errors in alias operations."""

    pass


class AliasManager:
    """Manager for keystore alias operations."""

    def __init__(self, keystore_manager: Optional[KeystoreManager] = None):
        """Initialize AliasManager.

        Args:
            keystore_manager: KeystoreManager instance
        """
        self.keystore_manager = keystore_manager
        self.logger = get_logger(__name__)

    def generate_descriptive_alias(
        self, cert: x509.Certificate, existing_aliases: Optional[Set[str]] = None
    ) -> str:
        """Generate a descriptive alias for a certificate.

        Args:
            cert: Certificate to generate alias for
            existing_aliases: Set of existing aliases to avoid conflicts

        Returns:
            Descriptive alias
        """
        # Extract common name
        try:
            common_name = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
            common_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", common_name)
        except (IndexError, ValueError):
            # Fallback to first part of subject
            subject_str = str(cert.subject)
            common_name = subject_str.split(",")[0].split("=")[-1].strip()
            common_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", common_name)

        # Extract expiration date
        expiry_date = cert.not_valid_after
        expiry_str = expiry_date.strftime("%Y-%m-%d")

        # Generate base alias
        base_alias = f"{common_name}_expires_{expiry_str}"

        # Ensure uniqueness if existing aliases provided
        if existing_aliases:
            alias = base_alias
            counter = 1
            while alias in existing_aliases:
                alias = f"{base_alias}_{counter}"
                counter += 1
            return alias
        else:
            return base_alias

    def rename_to_descriptive_aliases(
        self, keystore_manager: Optional[KeystoreManager] = None
    ) -> Dict[str, str]:
        """Rename all aliases in a keystore to be more descriptive.

        Args:
            keystore_manager: KeystoreManager instance (overrides instance attribute)

        Returns:
            Dictionary mapping old aliases to new aliases

        Raises:
            AliasError: If the aliases cannot be renamed
        """
        keystore_manager = keystore_manager or self.keystore_manager
        if not keystore_manager:
            raise AliasError("No keystore manager specified")
        if not keystore_manager._keystore:
            raise AliasError("No keystore loaded")

        log_operation_start(
            self.logger,
            "rename_to_descriptive_aliases",
            keystore=keystore_manager.keystore_file,
        )

        try:
            # Get all aliases
            aliases = keystore_manager.list_aliases()
            if not aliases:
                log_operation_end(
                    self.logger,
                    "rename_to_descriptive_aliases",
                    success=True,
                    keystore=keystore_manager.keystore_file,
                    renamed=0,
                    message="No aliases found in keystore",
                )
                return {}

            # Track existing aliases to avoid conflicts
            existing_aliases = set(aliases)
            renamed = {}
            
            # Process each alias
            for old_alias in aliases:
                # Skip already renamed aliases
                if old_alias in renamed.values():
                    continue

                try:
                    # Get certificate
                    cert = keystore_manager.get_certificate(old_alias)
                    
                    # Generate new alias
                    new_alias = self.generate_descriptive_alias(cert, existing_aliases)
                    
                    # Skip if alias is already descriptive
                    if old_alias == new_alias:
                        continue
                    
                    # Rename alias
                    keystore_manager.rename_alias(old_alias, new_alias)
                    
                    # Update tracking
                    renamed[old_alias] = new_alias
                    existing_aliases.remove(old_alias)
                    existing_aliases.add(new_alias)
                    
                    log_certificate_operation(
                        self.logger,
                        "rename_alias",
                        alias=old_alias,
                        new_alias=new_alias,
                    )
                except Exception as e:
                    self.logger.warning(
                        f"Error renaming alias",
                        alias=old_alias,
                        error=str(e),
                    )

            log_operation_end(
                self.logger,
                "rename_to_descriptive_aliases",
                success=True,
                keystore=keystore_manager.keystore_file,
                renamed=len(renamed),
            )

            return renamed
        except Exception as e:
            log_operation_end(
                self.logger,
                "rename_to_descriptive_aliases",
                success=False,
                keystore=keystore_manager.keystore_file,
                error=str(e),
            )
            raise AliasError(f"Failed to rename aliases: {str(e)}")

    def suggest_alias_improvements(
        self, keystore_manager: Optional[KeystoreManager] = None
    ) -> Dict[str, str]:
        """Suggest improvements for aliases in a keystore.

        Args:
            keystore_manager: KeystoreManager instance (overrides instance attribute)

        Returns:
            Dictionary mapping current aliases to suggested aliases

        Raises:
            AliasError: If the suggestions cannot be generated
        """
        keystore_manager = keystore_manager or self.keystore_manager
        if not keystore_manager:
            raise AliasError("No keystore manager specified")
        if not keystore_manager._keystore:
            raise AliasError("No keystore loaded")

        log_operation_start(
            self.logger,
            "suggest_alias_improvements",
            keystore=keystore_manager.keystore_file,
        )

        try:
            # Get all aliases
            aliases = keystore_manager.list_aliases()
            if not aliases:
                log_operation_end(
                    self.logger,
                    "suggest_alias_improvements",
                    success=True,
                    keystore=keystore_manager.keystore_file,
                    suggestions=0,
                    message="No aliases found in keystore",
                )
                return {}

            # Track existing aliases to avoid conflicts
            existing_aliases = set(aliases)
            suggestions = {}
            
            # Process each alias
            for current_alias in aliases:
                try:
                    # Get certificate
                    cert = keystore_manager.get_certificate(current_alias)
                    
                    # Generate suggested alias
                    suggested_alias = self.generate_descriptive_alias(cert, existing_aliases)
                    
                    # Skip if alias is already descriptive
                    if current_alias == suggested_alias:
                        continue
                    
                    # Add suggestion
                    suggestions[current_alias] = suggested_alias
                except Exception as e:
                    self.logger.warning(
                        f"Error generating suggestion for alias",
                        alias=current_alias,
                        error=str(e),
                    )

            log_operation_end(
                self.logger,
                "suggest_alias_improvements",
                success=True,
                keystore=keystore_manager.keystore_file,
                suggestions=len(suggestions),
            )

            return suggestions
        except Exception as e:
            log_operation_end(
                self.logger,
                "suggest_alias_improvements",
                success=False,
                keystore=keystore_manager.keystore_file,
                error=str(e),
            )
            raise AliasError(f"Failed to suggest alias improvements: {str(e)}")

    def check_alias_uniqueness(
        self, alias: str, keystore_manager: Optional[KeystoreManager] = None
    ) -> Tuple[bool, Optional[str]]:
        """Check if an alias is unique in a keystore.

        Args:
            alias: Alias to check
            keystore_manager: KeystoreManager instance (overrides instance attribute)

        Returns:
            Tuple of (is unique, suggested unique alias if not unique)

        Raises:
            AliasError: If the check cannot be performed
        """
        keystore_manager = keystore_manager or self.keystore_manager
        if not keystore_manager:
            raise AliasError("No keystore manager specified")
        if not keystore_manager._keystore:
            raise AliasError("No keystore loaded")

        try:
            # Get all aliases
            aliases = keystore_manager.list_aliases()
            
            # Check if alias exists
            if alias not in aliases:
                return True, None
            
            # Generate unique alias
            base_alias = alias
            counter = 1
            unique_alias = f"{base_alias}_{counter}"
            
            while unique_alias in aliases:
                counter += 1
                unique_alias = f"{base_alias}_{counter}"
            
            return False, unique_alias
        except Exception as e:
            raise AliasError(f"Failed to check alias uniqueness: {str(e)}")

    def get_alias_expiry_info(
        self, keystore_manager: Optional[KeystoreManager] = None
    ) -> Dict[str, Dict[str, str]]:
        """Get expiry information for all aliases in a keystore.

        Args:
            keystore_manager: KeystoreManager instance (overrides instance attribute)

        Returns:
            Dictionary mapping aliases to expiry information

        Raises:
            AliasError: If the expiry information cannot be retrieved
        """
        keystore_manager = keystore_manager or self.keystore_manager
        if not keystore_manager:
            raise AliasError("No keystore manager specified")
        if not keystore_manager._keystore:
            raise AliasError("No keystore loaded")

        log_operation_start(
            self.logger,
            "get_alias_expiry_info",
            keystore=keystore_manager.keystore_file,
        )

        try:
            # Get all aliases
            aliases = keystore_manager.list_aliases()
            if not aliases:
                log_operation_end(
                    self.logger,
                    "get_alias_expiry_info",
                    success=True,
                    keystore=keystore_manager.keystore_file,
                    aliases=0,
                    message="No aliases found in keystore",
                )
                return {}

            # Get expiry information for each alias
            expiry_info = {}
            now = datetime.now()
            
            for alias in aliases:
                try:
                    # Get certificate
                    cert = keystore_manager.get_certificate(alias)
                    
                    # Get expiry date
                    expiry_date = cert.not_valid_after
                    days_until_expiry = (expiry_date - now).days
                    
                    # Determine status
                    if days_until_expiry < 0:
                        status = "expired"
                    elif days_until_expiry < 30:
                        status = "expiring_soon"
                    else:
                        status = "valid"
                    
                    # Add to results
                    expiry_info[alias] = {
                        "expiry_date": expiry_date.strftime("%Y-%m-%d"),
                        "days_until_expiry": str(days_until_expiry),
                        "status": status,
                    }
                except Exception as e:
                    self.logger.warning(
                        f"Error getting expiry info for alias",
                        alias=alias,
                        error=str(e),
                    )
                    expiry_info[alias] = {
                        "expiry_date": "unknown",
                        "days_until_expiry": "unknown",
                        "status": "error",
                        "error": str(e),
                    }

            log_operation_end(
                self.logger,
                "get_alias_expiry_info",
                success=True,
                keystore=keystore_manager.keystore_file,
                aliases=len(expiry_info),
            )

            return expiry_info
        except Exception as e:
            log_operation_end(
                self.logger,
                "get_alias_expiry_info",
                success=False,
                keystore=keystore_manager.keystore_file,
                error=str(e),
            )
            raise AliasError(f"Failed to get alias expiry information: {str(e)}")
