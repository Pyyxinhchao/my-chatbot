import gradio as gr

def chatbot_response(message):
    return "Bạn muốn mua vé trận nào? (VD: PSG vs Marseille, ngày 12/5)"

demo = gr.Interface(fn=chatbot_response, inputs="text", outputs="text")
demo.launch()
