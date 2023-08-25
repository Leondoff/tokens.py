

# OpenAI GPT-4 Token Cost Estimator

This script estimates the number of tokens in a given text chunk and calculates the potential cost based on OpenAI's GPT-4 pricing model.

## Overview

The script uses the HuggingFace Transformers library to tokenize the text using the GPT-2 tokenizer, which should be a close approximation to the GPT-3/4 tokenizer. The script then calculates the estimated cost for the provided text for both prompt and sampled tokens and for both 8k and 32k context length models.

## Requirements

- Python 3
- HuggingFace Transformers library (install via `pip install transformers`)

## Usage

1. Clone or download the repository.
2. Ensure you have the required Python packages installed.
3. Replace the content of `input.txt` with the text you want to estimate the token count and cost for.
4. Run the script using `python3 tokens.py`.
5. The script will display the estimated token count and the associated cost based on the GPT-4 pricing model.

## Pricing Model (as of last update)

For 8k context length models:
- $0.03/1k prompt tokens
- $0.06/1k sampled tokens

For 32k context length models:
- $0.06/1k prompt tokens
- $0.12/1k sampled tokens

(Note: Always refer to OpenAI's official documentation for up-to-date pricing.)

## License

This script is provided under the MIT License. Feel free to use, modify, and distribute as needed.

