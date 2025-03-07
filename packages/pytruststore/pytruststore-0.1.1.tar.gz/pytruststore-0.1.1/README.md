# PyTrustStore 🔐

A Python application for working with Java keystore files.

## Features ✨

- Validate keystores against remote TLS resources
- Query keystores for certificates and aliases
- Get detailed information about keystore resources
- Import server certificates and their CA chains
- Make aliases explanatory and easy to understand

## Installation 📦

### Published Package Installation

Once PyTrustStore is published to PyPI:

```bash
# Using pip
pip install pytruststore

# Install as a global tool with uv
uv tool install pytruststore
```

### Local Development

To work with PyTrustStore directly from the repository:

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

Install PyTrustStore on your system without publishing to PyPI:

```bash
# Navigate to the repository directory
cd /path/to/pytruststore

# Install using pip directly from the local directory
pip install .

# Or build and install a wheel
python -m build --wheel
pip install dist/pytruststore-*.whl
```

For detailed installation instructions, see the [uv Installation Guide](docs/uv_installation.md).  
For local development and system-wide installation options, see the [Local Development Guide](docs/local_development.md).

## Usage 🚀

### From the Repository

When working directly from the repository:

```bash
# List all aliases in a keystore
uv run -m pytruststore list --keystore path/to/keystore.jks --password your-password

# Get detailed information about a certificate
uv run -m pytruststore info --keystore path/to/keystore.jks --password your-password --alias your-alias

# Validate a keystore against a remote TLS resource
uv run -m pytruststore validate --keystore path/to/keystore.jks --password your-password --url https://example.com
```

### Using the Installed Command

If you installed PyTrustStore globally:

```bash
# List all aliases in a keystore
pytruststore list --keystore path/to/keystore.jks --password your-password

# Get detailed information about a certificate
pytruststore info --keystore path/to/keystore.jks --password your-password --alias your-alias

# Validate a keystore against a remote TLS resource
pytruststore validate --keystore path/to/keystore.jks --password your-password --url https://example.com
```

### Using uv Tool Runner (After Publication)

Once PyTrustStore is published to PyPI:

```bash
# List all aliases in a keystore
uvx pytruststore list --keystore path/to/keystore.jks --password your-password

# Import server certificates from a URL
uvx pytruststore import --keystore path/to/keystore.jks --password your-password --url https://example.com
```

### Using in a Project (After Publication)

If you added PyTrustStore to your project:

```bash
# Rename aliases to be more descriptive
uv run pytruststore rename --keystore path/to/keystore.jks --password your-password --alias old-alias --new-alias new-alias

# Auto-rename all aliases to be more descriptive
uv run pytruststore auto-rename --keystore path/to/keystore.jks --password your-password
```

## Development 🛠️

For detailed development instructions, see the [Development Guide](docs/development_guide.md).

```bash
# Clone the repository
git clone https://gitlab.com/bdmorin/pytruststore.git
cd pytruststore

# Initialize the project with uv
uv init --existing

# Install the project in development mode
uv develop

# Add development dependencies
uv add --dev pytest ruff

# Run tests
uv run pytest

# Run linting
uv run ruff check .
```

## Documentation 📚

See the [Documentation Index](docs/index.md) for all available documentation.

- [uv Installation Guide](docs/uv_installation.md) - Guide for installing the uv package manager
- [Development Guide](docs/development_guide.md) - Comprehensive guide for developers
- [Local Development Guide](docs/local_development.md) - Guide for working with the repository
- [Troubleshooting Guide](docs/troubleshooting.md) - Solutions for common issues

## License 📄

Apache License 2.0
