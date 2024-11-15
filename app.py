from transformers import pipeline
import gradio as gr

# Define the model outside the generate function to avoid reloading it each time.
MODEL = "gpt2"
generator = pipeline("text-generation", model=MODEL)

# Define the generate function
def generate(content):
    return generator(content, max_length=50)[0]['generated_text']

# Use `gr.Interface` without Blocks syntax
demo = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(placeholder='Enter the input text to generate'),
    outputs=gr.Textbox(label="Generated Text")
)

# Launch the app
demo.launch()