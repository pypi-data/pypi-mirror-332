# vsce

A TUI tool for managing VS Code extensions.

## Installation

```bash
pip install vsce
```

## Usage

```bash
code-insiders --list-extensions | vsce  # Initial population of the list
vsce  # Run the interactive TUI
```

### Running Directly (For Development)

```bash
python vsce/main.py  # Run directly
code-insiders --list-extensions | python vsce/main.py # Initial population
```

Clean the extension list (useful if you manually uninstall extensions):

```bash
python vsce/main.py clean
```
### Development

```bash
git clone https://github.com/yourusername/vsce # Replace with your repo
cd vsce
uv venv
uv pip install -e .[dev]