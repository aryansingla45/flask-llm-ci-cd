from flask import Flask, render_template, request, redirect, url_for, session
import os
import yaml
from src.LLM import review_code
from src.utils.review_utils import load_file
import google.generativeai as genai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'just my random string'  # Needed for session management

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
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                
                # Load and review the file content
                file_content = load_file(file_path, request.form['pipeline_type'])
                review = review_code(file_content if isinstance(file_content, str) else yaml.dump(file_content), request.form['pipeline_type'])
                session['last_review'] = review  # Save the review result for displaying on the next page
                
                return redirect(url_for('review'))
    
    return render_template('index.html')

@app.route('/review', methods=['GET'])
def review():
    review = session.get('last_review')
    return render_template('review.html', review=review)

if __name__ == "__main__":
    app.run(debug=True)
