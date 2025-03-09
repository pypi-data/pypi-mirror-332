from flash_tokenizer import FlashBertTokenizer
import os

# Get the path to the vocabulary file
vocab_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "res", "vocab_char_16424.txt")

# Initialize the tokenizer
tokenizer = FlashBertTokenizer(vocab_file, do_lower_case=True)

# Test the tokenizer
text = "Hello, world!"
tokens = tokenizer.tokenize(text)
print(f"Tokens: {tokens}")

ids = tokenizer.convert_tokens_to_ids(tokens)
print(f"IDs: {ids}")

direct_ids = tokenizer(text)
print(f"Direct IDs: {direct_ids}")

# Verify that direct tokenization matches the two-step process
assert ids == direct_ids, "Direct tokenization does not match the two-step process"

print("All tests passed!")

# pip install build twine
# python -m build
# pip install dist/*.whl