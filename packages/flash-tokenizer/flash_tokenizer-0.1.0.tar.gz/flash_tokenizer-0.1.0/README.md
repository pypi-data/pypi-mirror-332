# flash-tokenizer

Flash BERT tokenizer implementation with C++ backend.

## Installation

```bash
pip install flash-tokenizer
```

Or install from source:

```bash
git clone https://github.com/springkim/flash-tokenizer.git
cd flash-tokenizer
pip install .
```

## Usage

```python
from flash_tokenizer import FlashBertTokenizer

# Initialize the tokenizer with a vocabulary file
tokenizer = FlashBertTokenizer("path/to/vocab.txt", do_lower_case=True)

# Tokenize text
tokens = tokenizer.tokenize("Hello, world!")
print(tokens)

# Convert tokens to IDs
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)

# Or use the tokenizer directly
ids = tokenizer("Hello, world!")
print(ids)
```
