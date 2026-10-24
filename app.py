import gradio as gr

# Function to process user input
def greet(name, message):
    if not name.strip():
        name = "Guest"

    return f"Hello, {name}!\n\nYour message: {message}"


# Create the Gradio web interface
with gr.Blocks(title="My Gradio Web Application") as demo:
    gr.Markdown("# My First Gradio Web Application")
    gr.Markdown("Enter your details below and click Submit.")

    name_input = gr.Textbox(
        label="Your Name",
        placeholder="Enter your name"
    )

    message_input = gr.Textbox(
        label="Your Message",
        placeholder="Enter your message",
        lines=3
    )

    submit_button = gr.Button("Submit", variant="primary")

    output = gr.Textbox(
        label="Output",
        lines=4
    )

    submit_button.click(
        fn=greet,
        inputs=[name_input, message_input],
        outputs=output
    )


# Launch the application
if __name__ == "__main__":
    demo.launch()
