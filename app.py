from flask import Flask, render_template, request, redirect, url_for, session
import os
import yaml
from src.LLM import review_code
from src.utils.review_utils import load_file
import google.generativeai as genai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'your_secret_key_here'  # Needed for session management

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize LLM once with API key
api_key = "AIzaSyCtuuxWl4_WlBXjbRsMMU9Rh_ccp-KX5qc"
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []

    # Recreate the ChatSession with the stored history
    chat_session = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    ).start_chat(history=session['chat_history'])

    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                
                # Load and review the file content
                file_content = load_file(file_path, request.form['pipeline_type'])
                review = review_code(file_content if isinstance(file_content, str) else yaml.dump(file_content), request.form['pipeline_type'])
                session['last_review'] = review  # Save the review result for further queries
                
                return render_template('index.html', review=review)
        
        if 'query' in request.form:
            query = request.form['query']
            response = chat_session.send_message(query)
            session['chat_history'] = chat_session.history  # Update session with new chat history
            return render_template('index.html', review=session.get('last_review'), response=response.text)
    
    return render_template('index.html')

@app.route('/clear_session', methods=['POST'])
def clear_session():
    session.pop('chat_history', None)
    session.pop('last_review', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
