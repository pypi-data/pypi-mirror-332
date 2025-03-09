# flash-tokenizer

Flash BERT tokenizer implementation with C++ backend.

## Installation

```bash
pip install flash-tokenizer
```

```bash
git clone https://github.com/springkim/flash-tokenizer.git
cd flash-tokenizer
pip install .
```

## Usage

```python
from flash_tokenizer import FlashBertTokenizer
tokenizer = FlashBertTokenizer("path/to/vocab.txt", do_lower_case=True)
# Tokenize text
ids = tokenizer("Hello, world!")
print(ids)
```
