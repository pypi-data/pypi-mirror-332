# Flowgate

Flowgate is a kafka client library for building event-driven systems.

## Setup

### Using just (recommended)

First, install [just](https://just.systems/):

```bash
# On macOS
brew install just

# On Linux
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash
```

Then set up the project:

```bash
just setup
```

### Using uv directly

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install the package
uv venv .venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

## Development

### Available commands

```bash
just                # List all available commands
just setup          # Set up the development environment
just test           # Run tests
just test-ci        # Run tests in CI mode
just lint           # Run linting checks
just build          # Build the package
just publish        # Build and publish the package
just sync           # Sync dependencies
just clean          # Clean up build artifacts
```

### Running tests

```bash
just test
# With specific arguments
just test -xvs tests/test_specific.py
```

### Linting

```bash
just lint
```

### Building and publishing

```bash
just build
just publish
```

## Optional dependencies

Flowgate supports the following optional dependencies:

- MongoDB: `uv pip install -e ".[mongo]"`
- Redis: `uv pip install -e ".[redis]"`
- cnamedtuple: `uv pip install -e ".[cnamedtuple]"`

```bash
pip install -e ".[dev]"
```

