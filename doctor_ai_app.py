# Install the necessary libraries
# pip install gradio llama-cpp-python

from llama_cpp import Llama
import gradio as gr

# Load your model
llm = Llama.from_pretrained(
    repo_id="h3lmi/modelgguf",
    filename="unsloth.Q8_0.gguf",
)

# Define the fixed prompt structure
base_prompt = """
### Instruction: You are a doctor. Answer the following query by a patient.
### Input: {}
### Response:
"""

# Define a function to generate model output
def generate_response(patient_query):
    formatted_prompt = base_prompt.format(patient_query)
    output = llm(formatted_prompt, max_tokens=256, echo=True)
    return output['choices'][0]['text']

# Create the Gradio interface
interface = gr.Interface(
    fn=generate_response,                          # Function to generate response
    inputs=gr.Textbox(lines=8, placeholder="Describe your symptoms here..."), # Input box
    outputs=gr.Textbox(label="Doctor's Response"), # Output box
    title="Doctor AI Assistant",                 
    description="Enter your symptoms to get advice from the AI doctor.", # description
)

if __name__ == "__main__":
    interface.launch()
