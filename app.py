from transformers import pipeline
import gradio as gr

# Define the model outside the generate function to avoid reloading it each time.
MODEL = "gpt2"
generator = pipeline("text-generation", model=MODEL)

# Define the generate function
def generate(content):
    return generator(content, max_length=50)[0]['generated_text']

# Use `Blocks` properly to structure the UI
with gr.Blocks() as demo:
    text_box = gr.Textbox(placeholder='Enter the input text to generate')
    output_box = gr.Textbox(label="Generated Text")
    
    # Link input and output to the function
    generate_button = gr.Button("Generate")
    generate_button.click(fn=generate, inputs=text_box, outputs=output_box)

# Launch the app
demo.launch()