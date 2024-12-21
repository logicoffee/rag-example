import gradio as gr
from lib import generate_answer, get_or_init_vector_store, retrieve_context

with gr.Blocks() as demo:
    vector_store = gr.State(None)

    with gr.Row():
        input = gr.Textbox(label="質問")
        button = gr.Button("回答生成", variant="primary")
    output = gr.Textbox(label="回答")

    @button.click(inputs=[vector_store, input], outputs=output)
    def handle_click_button(vector_store, input):
        context = retrieve_context(vector_store, input)
        return generate_answer(input, context)

    @demo.load(inputs=None, outputs=vector_store)
    def initialize():
        return get_or_init_vector_store()


demo.launch(server_name="0.0.0.0")
