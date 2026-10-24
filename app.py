import gradio as gr
gr.close_all()

def greet(name):
    return "Hello, " + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(label="Name:")],
    outputs=[gr.Textbox()],
)

demo.launch()
