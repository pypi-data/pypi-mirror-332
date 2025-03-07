# uv Installation Guide

## What is uv?

uv is an extremely fast Python package and project manager, written in Rust. It's designed to replace multiple tools like pip, pip-tools, pipx, poetry, pyenv, virtualenv, and more. uv offers 10-100x faster performance than pip and provides comprehensive project management capabilities.

## Basic Installation

### macOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verify Installation

```bash
uv --version
```

## Using uv with PyTrustStore

uv offers multiple ways to work with Python packages and projects. Here are the recommended approaches for PyTrustStore:

### As a User: Installing PyTrustStore

#### Option 1: Using uv as a Tool Runner (Recommended for Quick Use)

Run PyTrustStore directly without installation using `uvx` (alias for `uv tool run`):

```bash
uvx pytruststore <command> <options>
```

#### Option 2: Installing as a Tool

Install PyTrustStore as a globally available tool:

```bash
uv tool install pytruststore
```

This makes the `pytruststore` command available in your PATH.

#### Option 3: Installing in a Project

If you're using PyTrustStore within a project:

```bash
# Initialize a project if you don't have one
uv init myproject
cd myproject

# Add PyTrustStore as a dependency
uv add pytruststore

# Run PyTrustStore
uv run pytruststore <command> <options>
```

### As a Developer: Setting Up for Development

```bash
# Clone the repository
git clone https://github.com/your-org/pytruststore.git
cd pytruststore

# Initialize the project with uv (if not already using uv)
uv init --existing

# Add development dependencies
uv add --dev pytest ruff

# Install the project in development mode
uv develop

# Run tests
uv run pytest

# Run linting
uv run ruff check
```

## Managing Python Versions

uv can also manage Python versions:

```bash
# Install specific Python versions
uv python install 3.10 3.11 3.12

# Create a virtual environment with a specific Python version
uv venv --python 3.11

# Pin a Python version for a project
uv python pin 3.11
```

For detailed installation options and troubleshooting, refer to the [official documentation](https://docs.astral.sh/uv/).
