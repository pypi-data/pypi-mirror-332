# PyTrustStore Documentation

Welcome to the PyTrustStore documentation. This tool helps you work with Java keystore files, providing various operations for validation, querying, importing certificates, and managing aliases.

## Available Documentation

- [uv Installation Guide](uv_installation.md) - Guide for installing the uv package manager
- [Development Guide](development_guide.md) - Comprehensive guide for developers
- [Local Development Guide](local_development.md) - Guide for working with PyTrustStore directly from the repository
- [PyPI Publishing Guide](pypi_publishing_guide.md) - Information about publishing packages to PyPI
- [PyPI Workflow](pypi_workflow.md) - Automated workflow for publishing to PyPI using GitLab CI/CD
- [GitLab Setup Guide](gitlab_setup.md) - Guide for setting up the GitLab repository
- [Troubleshooting Guide](troubleshooting.md) - Solutions for common issues

## Quick Links

- [GitLab Repository](https://gitlab.com/bdmorin/pytruststore)
- [Project README](../README.md)
- [Development Tasks](../TASKS.md)
- [Changelog](../CHANGELOG.md)

## Features

- Validate keystores against remote TLS resources
- Query keystores for certificates and aliases
- Get detailed information about keystore resources
- Import server certificates and their CA chains
- Make aliases explanatory and easy to understand

## Getting Started

### Using the Published Package

Once PyTrustStore is published to PyPI:

```bash
# Using pip
pip install pytruststore

# Using uv
uv tool install pytruststore
```

### Working from the Repository

To use PyTrustStore directly from the repository:

```bash
# Clone the repository
git clone https://gitlab.com/bdmorin/pytruststore.git
cd pytruststore

# Initialize with uv and install in development mode
uv init --existing
uv develop

# Run the tool
uv run -m pytruststore <command> <options>
```

### System-Wide Installation Without PyPI

To install PyTrustStore on your system without publishing to PyPI:

```bash
# Navigate to the repository directory
cd /path/to/pytruststore

# Install using pip directly from the local directory
pip install .

# Or with uv
uv pip install .
```

See the [Local Development Guide](local_development.md#installing-system-wide-without-pypi) for more installation options.

For detailed usage examples, see the [README](../README.md).

## For Developers

If you're interested in contributing to PyTrustStore, please refer to the [Development Guide](development_guide.md) for detailed instructions on setting up your development environment and making changes to the codebase.
