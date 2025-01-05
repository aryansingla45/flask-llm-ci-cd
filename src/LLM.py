api_key = "your_api_key"

import google.generativeai as genai

# Configure the API key for Google Generative AI
genai.configure(api_key=api_key)

# Set up generation configuration
generation_config = {
    "temperature": 0.7,  # Adjusted for more deterministic responses
    "top_p": 0.9,
    "top_k": 50,
    "max_output_tokens": 2048,
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

# Start a chat session
chat_session = model.start_chat(
    history=[]
)

def review_code(file_content, pipeline_type):
    prompt = f"Please review the following {pipeline_type} configuration file for syntax errors and return the improvised code.\n\n{file_content}"
    response = chat_session.send_message(prompt)
    return response.text
