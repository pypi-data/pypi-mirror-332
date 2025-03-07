# PyTrustStore Troubleshooting Guide

This guide provides solutions for common issues you might encounter when using PyTrustStore.

## URL Validation Issues

### Problem: "Invalid URL" Error

If you receive an error like:

```
Error: Failed to validate against keystore: Failed to fetch server certificates: Invalid URL: pixel.quantserve.com
```

**Solution:**

Add the `https://` scheme to the URL:

```bash
# Instead of this:
uv run -m pytruststore validate --keystore trusted_certs.dat --password password -u pixel.quantserve.com

# Use this:
uv run -m pytruststore validate --keystore trusted_certs.dat --password password -u https://pixel.quantserve.com
```

PyTrustStore requires fully qualified URLs with a scheme (https:// or http://), while the Java `keytool` command accepts hostnames directly.

### Inconsistent Results Between PyTrustStore and Java keytool

If you get different results between PyTrustStore and the Java `keytool` command:

```bash
# PyTrustStore fails:
uv run -m pytruststore validate --keystore trusted_certs.dat --password password -u pixel.quantserve.com

# But Java keytool works:
keytool -printcert -sslserver pixel.quantserve.com -keystore trusted_certs.dat -storepass password
```

**Solution:**

The Java `keytool` command is more lenient with URL formats. Always use fully qualified URLs with PyTrustStore:

```bash
uv run -m pytruststore validate --keystore trusted_certs.dat --password password -u https://pixel.quantserve.com
```

## Installation Issues

### Problem: "No virtual environment found" Error

If you receive an error like:

```
error: No virtual environment found; run `uv venv` to create an environment, or pass `--system` to install into a non-virtual environment
```

**Solution:**

Create a virtual environment first:

```bash
# Create a virtual environment
uv venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# Then install or run
uv pip install pytruststore
```

Or install system-wide (not recommended):

```bash
uv pip install --system pytruststore
```

### Problem: "Command not found" Error

If you get a "command not found" error when trying to run `pytruststore` directly:

**Solution:**

1. Make sure you've installed the project in development mode:

```bash
cd /path/to/pytruststore
uv develop
```

2. Try running with the module syntax:

```bash
uv run -m pytruststore <command> <options>
```

3. Check that the installation directory is in your PATH.

## Keystore Issues

### Problem: "Keystore password was incorrect" Error

If you receive an error about an incorrect keystore password:

**Solution:**

1. Double-check your password.
2. If you're using environment variables, ensure they're set correctly:

```bash
export KEYSTORE_PASSWORD=your-password
uv run -m pytruststore <command> -k path/to/keystore.jks
```

### Problem: "Certificate not found" Error

If you receive an error that a certificate was not found:

**Solution:**

1. List all aliases in the keystore to verify what's available:

```bash
uv run -m pytruststore list -k path/to/keystore.jks -p your-password
```

2. Check if the certificate is in the keystore with a different alias.

## Certificate Issues

### Problem: Missing Certificates in Validation

If you receive a validation result showing missing certificates:

```
┏━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Certificate ┃ Found ┃ Alias ┃ Subject                             ┃
┡━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ cert_0      │ Yes   │ mykey │ <Name(CN=quantserve.com)>           │
│ cert_1      │ No    │       │ <Name(C=US,O=Let's Encrypt,CN=R10)> │
└─────────────┴───────┴───────┴─────────────────────────────────────┘
Some certificates not found in keystore
```

**Solution:**

Import the missing certificates using the `import` command:

```bash
# Import certificates from the URL
uv run -m pytruststore import --keystore trusted_certs.dat --password password --url pixel.quantserve.com
```

This will import all certificates in the chain, including the missing ones. After importing, run the validation again to confirm all certificates are now found:

```bash
uv run -m pytruststore validate --keystore trusted_certs.dat --password password --url pixel.quantserve.com
```

### Problem: Certificate Chain Validation Failures

If you're having issues with certificate chain validation:

**Solution:**

1. Import the entire certificate chain:

```bash
uv run -m pytruststore import --keystore trusted_certs.dat --password password --url pixel.quantserve.com
```

2. Check the certificate information to understand the chain:

```bash
# List all aliases to find the imported certificates
uv run -m pytruststore list --keystore trusted_certs.dat --password password

# Get detailed information about a specific certificate
uv run -m pytruststore info --keystore trusted_certs.dat --password password --alias pixel_quantserve_com_server
```

## Other Issues

### Problem: Java or OpenSSL Not Found

If you receive errors related to Java's `keytool` or `openssl` not being found:

**Solution:**

1. Ensure Java and OpenSSL are installed and in your PATH.
2. On macOS/Linux, check with:

```bash
which keytool
which openssl
```

3. On Windows, check with:

```cmd
where keytool
where openssl
```

### Problem: Logging Issues

If you need more detailed logs for troubleshooting:

**Solution:**

Use the `--log-level` option to increase verbosity:

```bash
uv run -m pytruststore <command> <options> --log-level DEBUG
```

Check the logs in the `logs/` directory for detailed information.
