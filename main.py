from transformers import pipeline

MODEL = "openai-community/gpt2"

def generate(content):
    generator = pipeline(model=MODEL)
    # model in ~/.cache/huggingface/hub
    return generator(content)