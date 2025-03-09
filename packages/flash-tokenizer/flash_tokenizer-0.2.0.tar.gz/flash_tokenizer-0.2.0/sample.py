from flash_tokenizer import FlashBertTokenizer
import os

vocab_file = "./res/vocab_char_16424.txt"

tokenizer = FlashBertTokenizer(vocab_file, do_lower_case=True, max_input_chars_per_word=256)

text = "Hello, world!"

direct_ids = tokenizer(text)
print(f"input_ids: {direct_ids}")
