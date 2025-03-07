# GitLab Repository Setup Guide (ʘ‿ʘ)✧

This guide explains how to set up the GitLab repository for the `pytruststore` package.

## Initial Repository Setup 🚀

The GitLab repository has been created at: https://gitlab.com/bdmorin/pytruststore

To push the local repository to GitLab, follow these steps:

```bash
# Navigate to the project directory
cd /Users/bdmorin/src/pytruststore

# Initialize git repository (if not already done)
git init

# Add all files to git
git add .

# Create initial commit
git commit -m "Initial commit (⌐■_■)"

# Add GitLab remote
git remote add origin https://gitlab.com/bdmorin/pytruststore.git

# Push to GitLab
git push -u origin main
```

## Setting Up Protected Variables 🔐

For the CI/CD pipeline to publish to PyPI, you need to set up a protected variable:

1. Go to your GitLab project: https://gitlab.com/bdmorin/pytruststore
2. Navigate to Settings → CI/CD → Variables
3. Add a new variable:
   - Key: `PYPI_API_TOKEN`
   - Value: Your PyPI API token
   - Type: Variable
   - Environment scope: All (default)
   - Protect variable: ✓ (checked)
   - Mask variable: ✓ (checked)
4. Click "Add variable"

## Obtaining a PyPI API Token 🔑

To get a PyPI API token:

1. Create a PyPI account if you don't have one: https://pypi.org/account/register/
2. Log in to your PyPI account
3. Go to Account Settings → API tokens
4. Create a new API token:
   - Token name: `gitlab-ci-pytruststore`
   - Scope: Project: pytruststore
   - Click "Create token"
5. Copy the token (it will only be shown once!)
6. Add this token as the `PYPI_API_TOKEN` variable in GitLab CI/CD settings

## Protected Branches and Tags 🛡️

To ensure only authorized users can push to main branch and create release tags:

1. Go to your GitLab project: https://gitlab.com/bdmorin/pytruststore
2. Navigate to Settings → Repository → Protected branches
3. Protect the `main` branch:
   - Branch: `main`
   - Allowed to merge: Maintainers
   - Allowed to push: Maintainers
   - Click "Protect"

4. Navigate to Settings → Repository → Protected tags
5. Protect release tags:
   - Tag: `v*` (to protect all version tags)
   - Allowed to create: Maintainers
   - Click "Protect"

## Repository Structure 📁

The repository has the following structure:

```
pytruststore/
├── .gitlab-ci.yml         # GitLab CI/CD configuration
├── LICENSE                # Apache 2.0 license
├── README.md              # Project documentation
├── TASKS.md               # Development task tracking
├── docs/                  # Documentation files
│   ├── development_guide.md
│   ├── gitlab_setup.md    # This file
│   ├── index.md           # Documentation index
│   ├── local_development.md
│   ├── pypi_publishing_guide.md
│   ├── pypi_workflow.md
│   ├── troubleshooting.md
│   └── uv_installation.md
├── pytruststore/          # Main package code
│   ├── __init__.py
│   ├── __main__.py
│   ├── alias.py
│   ├── cli_wrapper.py
│   ├── keystore.py
│   ├── logging_config.py
│   ├── utils.py
│   └── validation.py
├── logs/                  # Log files
│   └── .gitkeep
├── pyproject.toml         # Project configuration
├── tests/                 # Test files
│   ├── __init__.py
│   └── test_keystore.py
└── uv.lock                # uv dependency lock file
```

## CI/CD Pipeline 🔄

The CI/CD pipeline is configured in `.gitlab-ci.yml` and includes:

1. **Lint**: Checks code quality using Ruff
2. **Test**: Runs unit tests with pytest
3. **Security Scanning**: Performs SAST analysis
4. **Build**: Creates distribution packages
5. **Publish**: Uploads packages to PyPI (only on tags)

For more details, see the [PyPI Workflow](pypi_workflow.md) documentation.

## First Release Process 🎉

To make the first release:

1. Ensure all code is committed and pushed to GitLab
2. Create and push a tag with the version number:

```bash
git tag v0.1.0
git push origin v0.1.0
```

3. Monitor the CI/CD pipeline in GitLab
4. Once completed, verify the package is available on PyPI: https://pypi.org/project/pytruststore/

## Troubleshooting 🔧

If you encounter issues with the GitLab setup:

1. **Push access denied**: Ensure you have the correct permissions on the repository
2. **CI/CD pipeline fails**: Check the pipeline logs for specific errors
3. **PyPI publishing fails**: Verify the API token is correctly set up and has the right permissions

For more troubleshooting tips, see the [Troubleshooting Guide](troubleshooting.md).
