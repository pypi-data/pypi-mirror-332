# souvenir python

Translated [souvenir](https://github.com/j5pr/souvenir) to python.

A structured ID generation and parsing library using prefixes.

This library primariy provides the `Id` class, which stores a 128-bit identifier
with its corresponding type (tag). The string representation of an `Id` is the
type's tag and the 128-bit value encoded into a variant of
[Crockford Base 32](https://www.crockford.com/base32.html).

## Setup

### User

```
pip install souvenir-python
```

### Dev

```
pip install ".[dev]"
```

## License

This project is licensed under the MIT License.
