from transformers import GPT2Tokenizer

# Pricing model
PRICING_8K = {
    "prompt": 0.03 / 1000,  # price per prompt token for 8k context length models
    "sampled": 0.06 / 1000  # price per sampled token for 8k context length models
}

PRICING_32K = {
    "prompt": 0.06 / 1000,  # price per prompt token for 32k context length models
    "sampled": 0.12 / 1000  # price per sampled token for 32k context length models
}

def count_tokens(text):
    """
    Estimate the number of tokens in a text string using GPT-2's tokenizer from HuggingFace.
    """
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
    tokens = tokenizer.tokenize(text)
    return len(tokens)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        text = f.read()

    tokens = count_tokens(text)
    cost_8k_prompt = tokens * PRICING_8K["prompt"]
    cost_8k_sampled = tokens * PRICING_8K["sampled"]
    cost_32k_prompt = tokens * PRICING_32K["prompt"]
    cost_32k_sampled = tokens * PRICING_32K["sampled"]

    print(f"Estimated number of tokens: {tokens}")
    print(f"Estimated cost for 8k context models:")
    print(f"  Prompt tokens: ${cost_8k_prompt:.2f}")
    print(f"  Sampled tokens: ${cost_8k_sampled:.2f}")
    print(f"Estimated cost for 32k context models:")
    print(f"  Prompt tokens: ${cost_32k_prompt:.2f}")
    print(f"  Sampled tokens: ${cost_32k_sampled:.2f}")
