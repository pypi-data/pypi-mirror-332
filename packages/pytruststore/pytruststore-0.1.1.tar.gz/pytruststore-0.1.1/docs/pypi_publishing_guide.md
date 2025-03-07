# PyPI Publishing Guide (ʘ‿ʘ)✧

This guide explains how to publish PyTrustStore to the Python Package Index (PyPI).

## What is PyPI? 🤔

PyPI (Python Package Index) is the official repository for Python packages. It allows you to share your Python code with the community, making it installable via pip or other package managers like uv.

## Prerequisites 📋

Before publishing to PyPI, you need:

1. A PyPI account (register at https://pypi.org/account/register/)
2. The necessary Python packaging tools:
   ```bash
   pip install build twine
   ```
3. A properly configured `pyproject.toml` file (already set up in this repository)

## Publishing Process 🚀

### 1. Prepare Your Package

Ensure your package is ready for publication:

- Update the version number in `pyproject.toml`
- Make sure all tests pass
- Update documentation if needed
- Update CHANGELOG.md with the new version's changes

### 2. Build Distribution Packages

Build both wheel and source distribution packages:

```bash
python -m build
```

This will create distribution files in the `dist/` directory:
- `pytruststore-x.y.z-py3-none-any.whl` (wheel package)
- `pytruststore-x.y.z.tar.gz` (source distribution)

### 3. Upload to PyPI

Use Twine to upload your packages to PyPI:

```bash
twine upload dist/*
```

You'll be prompted for your PyPI username and password. For more secure authentication, you can use an API token instead of your password.

### 4. Verify the Upload

After uploading, verify that your package appears on PyPI:
https://pypi.org/project/pytruststore/

## Using API Tokens (Recommended) 🔐

Instead of using your password, you can create an API token:

1. Go to https://pypi.org/manage/account/
2. Navigate to "API tokens"
3. Click "Add API token"
4. Set the token scope (project-specific is more secure)
5. Copy the token (it will only be shown once!)

When using twine, enter `__token__` as your username and the token as your password:

```bash
twine upload dist/* -u __token__ -p pypi-your-token-here
```

Or set environment variables:

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-your-token-here
twine upload dist/*
```

## Automated Publishing with GitLab CI/CD 🤖

This repository is configured to automatically publish to PyPI when a new tag is pushed. See the [PyPI Workflow](pypi_workflow.md) documentation for details.

To trigger a release:

```bash
# Update version in pyproject.toml to 0.1.1
git add pyproject.toml
git commit -m "Bump version to 0.1.1 (╯°□°）╯︵ ┻━┻"
git tag v0.1.1
git push origin main v0.1.1
```

## Package Versioning 📊

Follow semantic versioning (MAJOR.MINOR.PATCH):

- MAJOR: Incompatible API changes
- MINOR: Add functionality (backwards-compatible)
- PATCH: Bug fixes (backwards-compatible)

Example: `0.1.0` → `0.1.1` for a bug fix, `0.1.0` → `0.2.0` for new features.

## Common Issues and Solutions 🔧

### "File already exists" Error

If you try to upload a version that already exists on PyPI, you'll get an error. You cannot overwrite existing files on PyPI, so you must increment the version number.

### "Invalid classifier" Warning

Ensure all classifiers in `pyproject.toml` are valid according to PyPI's list: https://pypi.org/classifiers/

### "Description content type" Warning

If you get warnings about description content type, ensure your README.md is properly formatted.

## Testing Your Package Before Publishing 🧪

You can test your package locally before publishing:

```bash
# Build the package
python -m build

# Install locally from the wheel file
pip install dist/pytruststore-*.whl

# Test the installed package
pytruststore --version
```

Or use TestPyPI, a separate instance of PyPI for testing:

```bash
# Register at https://test.pypi.org/account/register/
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ pytruststore
```

## Additional Resources 📚

- [Python Packaging User Guide](https://packaging.python.org/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [PyPI Help](https://pypi.org/help/)
- [TestPyPI](https://test.pypi.org/)

## Checklist for Publishing ✅

- [ ] Update version in `pyproject.toml`
- [ ] Update CHANGELOG.md
- [ ] Run tests to ensure everything works
- [ ] Build distribution packages
- [ ] Upload to PyPI
- [ ] Verify package on PyPI
- [ ] Create a new Git tag
- [ ] Push tag to GitLab
