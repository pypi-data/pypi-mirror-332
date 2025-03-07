# 🍹 emojito

[![PyPI version](https://img.shields.io/pypi/v/emojito-py.svg?style=flat-square&logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/emojito-py/)
[![Python versions](https://img.shields.io/pypi/pyversions/emojito-py.svg?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/emojito-py/)
[![License](https://img.shields.io/pypi/l/emojito-py.svg?style=flat-square)](https://github.com/matijaoe/emojito/blob/main/LICENSE)

> *emojis with a hidden agenda.*

A Python library and CLI tool that lets you secretly encode text into ordinary emojis using Unicode steganography. Hide messages in plain sight and share them anywhere emojis are supported.

Inspired by Paul Butler's article ["Smuggling Arbitrary Data Through an Emoji"](https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/).

## Installation

Install from PyPI:
```bash
pip install emojito-py
```

Or install the latest development version directly from GitHub:
```bash
pip install git+https://github.com/matijaoe/emojito.git@main#egg=emojito-py
```

<details>
<summary>on a mac?</summary>

On macOS, `pipx` is recommended for CLI tools:

```bash
# Install pipx if you don't have it
brew install pipx
pipx ensurepath

# Install from PyPI (recommended)
pipx install emojito-py

# OR install from GitHub (development version)
pipx install git+https://github.com/matijaoe/emojito.git@main#egg=emojito-py
```

This installs the package in an isolated environment while making the CLI commands globally available.
</details>

## Usage

### CLI

#### Encode

```bash
emojito encode '🍹' 'trust no one'
# 🍹󠅤󠅢󠅥󠅣󠅤󠄐󠅞󠅟󠄐󠅟󠅞󠅕️
```

#### Decode

```bash
emojito decode '🍹󠅤󠅢󠅥󠅣󠅤󠄐󠅞󠅟󠄐󠅟󠅞󠅕️' 
# trust no one
```

### Python

```py
from emojito import encode, decode

secret = encode('🍹', 'trust no one')
print(secret) # 🍹󠅤󠅢󠅥󠅣󠅤󠄐󠅞󠅟󠄐󠅟󠅞󠅕️

decoded = decode(secret)
print(decoded) # trust no one
```

## Limitations

- Some platforms may strip variation selectors from emojis
- Maximum message length is 255 bytes
- Works best with single emojis as carriers

## Acknowledgements

- [Paul Butler](https://paulbutler.org/) for the original concept
- [Unicode Consortium](https://home.unicode.org/) for variation selectors
