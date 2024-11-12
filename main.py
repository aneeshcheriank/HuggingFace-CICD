from transformers import pipeline

def generate(content):
    generator = pipeline(model="HuggingFaceH4/zephyr-7b-beta")
    # model in ~/.cache/huggingface/hub
    # Zephyr-beta is a conversational model, so let's pass it a chat instead of a single string
    return generator([{"role": "user", "content": content}], do_sample=False, max_new_tokens=2)