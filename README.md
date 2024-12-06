# medicalLLama3.1 : Doctor AI Assistant (Gradio App)

This project is a Gradio-based AI assistant that provides medical advice based on user-reported symptoms. The AI assistant is powered by a large language model and is deployed as a containerized application using Docker.

![Uploading image.png…]()


## Features
- Enter a description of your symptoms or medical query.
- Receive a response from the AI, simulating a doctor’s advice based on the input.
- Dockerized application for easy deployment.

## Fine-Tuning

We provide a Jupyter notebook (`llama3.1_finetuning_unsolth.ipynb`) for fine-tuning the model. The notebook includes steps for preparing the data, training and saving the model, and inference tests. 
## Setup Instructions

### Clone this repository:

```bash
git clone https://github.com/your-username/doctor-ai-app.git
cd doctor-ai-app
```

### To use the fine-tuned model from Hugging Face:
```
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="your-username/doctor-ai-model",
    filename="unsloth.Q8_0.gguf",
)
```
### Run the app locally:
To run the Gradio app locally, simply execute:
```
python doctor_ai_app.py
```
### Run the app in Docker:
If you prefer to run the app using Docker, follow these steps:
```
docker build -t doctor-ai-app .

docker run -p 7860:7860 doctor-ai-app

```




