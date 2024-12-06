
import streamlit as st
from llama_cpp import Llama

# Load your model
#llm = Llama.from_pretrained(
 #   repo_id="h3lmi/modelgguf",
  #  filename="unsloth.Q8_0.gguf",
#)

# Define the fixed prompt structure
base_prompt = """
### Instruction: You are a doctor. Answer the following query by a patient.
### Input: {}
### Response:
"""

# Define a function to generate model output
def generate_response(patient_query):
    formatted_prompt = base_prompt.format(patient_query)
    output = llm(formatted_prompt, max_tokens=256, echo=False)
    return output['choices'][0]['text']

def main():
    st.title("Doctor AI Assistant")
    st.write("Enter your symptoms to get advice from the AI doctor.")

    # Input box for the user's query
    patient_query = st.text_area("Describe your symptoms here...", height=150)

    # Submit button
    if st.button("Get Advice"):
        if patient_query.strip():
            # Generate response from the model
            with st.spinner("Analyzing your symptoms..."):
                response = generate_response(patient_query)
            st.subheader("Doctor's Response:")
            st.write(response)
        else:
            st.warning("Please enter your symptoms before submitting.")

if __name__ == "__main__":
    main()
