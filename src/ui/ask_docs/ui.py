import os

import gradio as gr
from dotenv import load_dotenv, find_dotenv, dotenv_values


def create_ai_key_ui():
    with gr.Column():  ## for open API key
        with gr.Row():
            with gr.Column(scale=4):
                apikey_text = gr.Textbox(
                    placeholder='Enter your OpenAI API key',
                    show_label=False,
                    interactive=True,
                    container=False)

            with gr.Column(scale=1):
                update_apikey_btn = gr.Button('Update API Key')
    return apikey_text, update_apikey_btn


def create_pdf_ui():
    with gr.Blocks(title="Chat with PDF",
                   theme=gr.themes.Monochrome()) as pdf_ui:
        with gr.Row():
            chatbot = gr.Chatbot(value=[], elem_id='chatbot', height=680)
            show_img = gr.Image(label='PDF Preview', height=680)

        with gr.Row():
            with gr.Column(scale=3):
                text_input = gr.Textbox(
                    show_label=False,
                    placeholder="Ask your pdf?",
                    container=False)

            with gr.Column(scale=1):
                submit_btn = gr.Button('Send')

            with gr.Column(scale=1):
                upload_btn = gr.UploadButton("📁 Upload PDF", file_types=[".pdf"])
    return pdf_ui, chatbot, show_img, text_input, submit_btn, upload_btn


if __name__ == '__main__':
    demo, chatbot, show_img, text_input, submit_btn, upload_btn = create_pdf_ui()
    demo.queue()
    demo.launch()
