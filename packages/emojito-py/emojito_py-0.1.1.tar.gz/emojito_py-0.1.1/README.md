# 🍹 emojito

[![PyPI version](https://badge.fury.io/py/emojito-py.svg)](https://pypi.org/project/emojito-py/)

*emojis with a hidden agenda.*

emojito is a Python library and CLI tool that lets you secretly encode text into emojis, hiding messages in plain sight. It works by using Unicode steganography to invisibly embed information into ordinary emoji characters, enabling you to discreetly share hidden messages in chats, posts, or anywhere emojis are supported.

Inspired by Paul Butler's article ["Smuggling Arbitrary Data Through an Emoji"](https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/).

## Installation

Install from PyPI:
```bash
pip install emojito-py
```

Or install the latest development version directly from GitHub:
```bash
pip install git+https://github.com/matijaoe/emojito.git
```

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

#### Encode

```py
from emojito import encode, decode

secret = encode('🍹', 'trust no one')
print(secret) # **🍹󠅤󠅢󠅥󠅣󠅤󠄐󠅞󠅟󠄐󠅟󠅞󠅕️**

decoded = decode(secret)
print(decoded) # trust no one
```
