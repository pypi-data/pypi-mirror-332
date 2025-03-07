# PyTrustStore Development Guide

This guide will help you set up your development environment and make changes to the PyTrustStore application using uv's modern project management features.

## Setting Up Your Development Environment

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-org/pytruststore.git
   cd pytruststore
   ```

2. **Initialize the project with uv**

   If the project doesn't already have uv configuration:

   ```bash
   uv init --existing
   ```

   This will initialize uv for the existing project, creating necessary configuration files.

3. **Install the project in development mode**

   ```bash
   uv develop
   ```

   This installs the project in development mode, making it available for import while allowing changes to the source code to be immediately reflected.

4. **Add development dependencies**

   ```bash
   uv add --dev pytest ruff
   ```

   This adds development dependencies to the project.

## Project Structure

- `pytruststore/` - Main package directory
  - `__init__.py` - Package initialization
  - `__main__.py` - Entry point for the CLI
  - `keystore.py` - Core keystore operations
  - `validation.py` - Certificate validation logic
  - `alias.py` - Alias management functionality
  - `cli_wrapper.py` - Wrappers for external CLI tools
  - `utils.py` - Utility functions
  - `logging_config.py` - Logging configuration

- `tests/` - Test directory
  - `test_keystore.py` - Tests for keystore operations

## Development Workflow

1. **Make your changes**

   Edit the relevant files in the `pytruststore/` directory.

2. **Run linting**

   ```bash
   uv run ruff check .
   ```

   Fix any linting issues before proceeding.

3. **Run tests**

   ```bash
   uv run pytest
   ```

   Ensure all tests pass. Add new tests for new functionality.

4. **Test your changes manually**

   ```bash
   # Run the CLI directly
   uv run pytruststore <command> <options>
   ```

5. **Lock dependencies**

   ```bash
   uv lock
   ```

   This creates or updates the `uv.lock` file with exact versions of all dependencies.

6. **Build the package**

   ```bash
   uv build
   ```

   This builds the package into a distributable format.

## Adding New Features

1. **Update the relevant module** in the `pytruststore/` directory
2. **Add tests** in the `tests/` directory
3. **Update documentation** in docstrings and README.md
4. **Update TASKS.md** to track your progress

## Dependency Management

### Adding Dependencies

```bash
# Add a runtime dependency
uv add requests

# Add a development dependency
uv add --dev black

# Add a dependency with a specific version
uv add "flask>=2.0.0"

# Add multiple dependencies at once
uv add requests flask pydantic
```

### Removing Dependencies

```bash
# Remove a dependency
uv remove requests
```

### Updating Dependencies

```bash
# Update all dependencies
uv lock --update

# Update a specific dependency
uv add --update requests
```

### Viewing Dependencies

```bash
# List all dependencies
uv list
```

## Common Development Tasks

### Adding a New Command

1. Define the command function in the appropriate module
2. Add the command to `__main__.py` using Click decorators
3. Add tests for the new command
4. Update documentation

### Modifying Keystore Operations

1. Update the `keystore.py` module
2. Ensure proper error handling and logging
3. Update tests in `test_keystore.py`

### Working with Certificates

1. Understand the certificate format and operations in `keystore.py`
2. Use the `cryptography` library for certificate operations
3. Test with real certificates when possible

## Troubleshooting

### General Troubleshooting

- Check the logs in the `logs/` directory
- Use the `--log-level DEBUG` option for more detailed logging
- Ensure Java's `keytool` and `openssl` are available in your PATH

### uv Troubleshooting

- **No virtual environment found error**: If you see `No virtual environment found`, you need to create a virtual environment first:
  ```bash
  uv venv
  ```

- **Permission issues**: If you encounter permission issues when installing packages:
  ```bash
  # On Linux/macOS
  sudo uv tool install --system pytruststore
  ```

- **Dependency conflicts**: If you encounter dependency conflicts:
  ```bash
  # Try updating the lock file
  uv lock --update
  
  # Then sync the environment
  uv sync
  ```

- **Cache issues**: If you suspect cache issues:
  ```bash
  # Clear the uv cache
  uv cache clean
  ```

- **Python version issues**: If you need a specific Python version:
  ```bash
  # Install the required Python version
  uv python install 3.11
  
  # Create a virtual environment with that version
  uv venv --python 3.11
  ```

For more detailed information about the project, refer to the code documentation and comments within each module.
