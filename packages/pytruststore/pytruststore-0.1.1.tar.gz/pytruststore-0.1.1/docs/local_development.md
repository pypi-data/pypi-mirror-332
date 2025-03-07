# Local Development with PyTrustStore

This guide explains how to work with PyTrustStore directly from the repository without publishing it to PyPI.

## Setting Up for Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-org/pytruststore.git
   cd pytruststore
   ```

2. **Initialize the project with uv**

   ```bash
   uv init --existing
   ```

   This will initialize uv for the existing project, creating necessary configuration files.

3. **Install the project in development mode**

   ```bash
   uv develop
   ```

   This installs the project in development mode, making it available for import while allowing changes to the source code to be immediately reflected.

## Running PyTrustStore Locally

### Option 1: Using uv run

The most straightforward way to run PyTrustStore from the repository:

```bash
# Run the module directly
uv run -m pytruststore <command> <options>

# Examples:
uv run -m pytruststore list --keystore path/to/keystore.jks --password your-password
uv run -m pytruststore validate --keystore path/to/keystore.jks --password your-password --url https://example.com
```

### Option 2: Using Python Directly

If you've activated a virtual environment with the project installed:

```bash
# Create and activate a virtual environment if you haven't already
uv venv
source .venv/bin/activate  # On macOS/Linux

# Install the project in development mode
pip install -e .

# Run the module
python -m pytruststore <command> <options>
```

### Option 3: Using the Entry Point Script

If the project has a console script entry point defined in pyproject.toml:

```bash
# After installing in development mode
uv develop

# Run the command directly
pytruststore <command> <options>
```

## Making Changes

1. Edit the source code in the `pytruststore/` directory
2. Run the tool using one of the methods above to test your changes
3. Run tests to ensure everything works correctly:

   ```bash
   uv run pytest
   ```

4. Run linting to ensure code quality:

   ```bash
   uv run ruff check .
   ```

## Installing System-Wide Without PyPI

If you want to install PyTrustStore on your system without publishing to PyPI, you have several options:

### Option 1: Install from Local Directory

```bash
# Navigate to the repository directory
cd /path/to/pytruststore

# Install using pip directly from the local directory
pip install .

# Or with uv
uv pip install .
```

### Option 2: Install in Development Mode

This allows you to make changes to the code and have them immediately available:

```bash
# Navigate to the repository directory
cd /path/to/pytruststore

# Install in development mode with pip
pip install -e .

# Or with uv
uv pip install -e .
```

### Option 3: Install from Git URL

You can install directly from a Git repository:

```bash
# Install from a GitHub repository
pip install git+https://github.com/your-org/pytruststore.git

# Or with uv
uv pip install git+https://github.com/your-org/pytruststore.git
```

### Option 4: Build and Install Wheel

Build a wheel file and install it:

```bash
# Navigate to the repository directory
cd /path/to/pytruststore

# Build the wheel
python -m build --wheel

# Install the wheel
pip install dist/pytruststore-*.whl

# Or with uv
uv build
uv pip install dist/pytruststore-*.whl
```

After installation, you can run the tool directly:

```bash
pytruststore <command> <options>
```

## Troubleshooting

### Command Not Found

If you get a "command not found" error when trying to run `pytruststore` directly:

1. Make sure you've installed the project in development mode with `uv develop` or one of the system-wide installation methods above
2. Check that the installation directory is in your PATH
3. Try running with the module syntax: `uv run -m pytruststore` or `python -m pytruststore`

### Module Not Found

If you get a "module not found" error:

1. Make sure you're in the project root directory
2. Verify that the project is installed in development mode with `uv develop` or one of the system-wide installation methods above
3. Check that the module name is correct (it should match the directory name)

### Other Issues

For other issues, refer to the [Development Guide](development_guide.md) and the [uv Troubleshooting](development_guide.md#uv-troubleshooting) section.
